import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 600)

def nothing(x):
    pass

def Angle(v1,v2):
    dot = np.dot(v1,v2)
    x_modulus = np.sqrt((v1 * v1).sum())
    y_modulus = np.sqrt((v2 * v2).sum())
    cos_angle = dot / x_modulus / y_modulus
    angle = np.degrees(np.arccos(cos_angle))
    return angle

def FindDistance(A,B):
    sum = np.sqrt(np.power((A[0][0]-B[0][0]),2)) + np.power((A[0][1]-B[0][1]),2)
    return sum

cv2.namedWindow('HSV_TrackBar')

h,s,v = 100,100,100

cv2.createTrackbar('h', 'HSV_TrackBar',0,179,nothing)
cv2.createTrackbar('s', 'HSV_TrackBar',0,255,nothing)
cv2.createTrackbar('v', 'HSV_TrackBar',0,255,nothing)


while(True):
    start_time = time.time()
    ret, frame = cap.read()
    
    blur = cv2.blur(frame,(3,3))
    
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    
    mask2 = cv2.inRange(hsv,np.array([2,50,50]),np.array([15,255,255]))
    
    kernel_square = np.ones((11,11),np.uint8)
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    
    dilation = cv2.dilate(mask2,kernel_ellipse,iterations=1)
    erosion = cv2.erode(dilation,kernel_square,iterations=1)
    dilation2 = cv2.dilate(erosion,kernel_ellipse,iterations=1)
    filtered = cv2.medianBlur(dilation2,5)
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(8,8))
    dilation3 = cv2.dilate(filtered,kernel_ellipse,iterations = 1)
    median = cv2.medianBlur(dilation2,5)
    ret,thresh = cv2.threshold(median,127,255,0)
    
    contours, hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    max_area = 100
    ci = 0
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if(area > max_area):
            max_area = area
            ci = i
    
    cnts = contours[ci]
    hull = cv2.convexHull(cnts)
    
    hull2 = cv2.convexHull(cnts,returnPoints = False)
    defects = cv2.convexityDefects(cnts,hull2)
    
    FarDefect = []
    
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnts[s][0])
        end = tuple(cnts[e][0])
        far = tuple(cnts[f][0])
        FarDefect.append(far)
        cv2.line(frame,start,end,[0,255,0],1)
        cv2.circle(frame,far,10,[100,255,255],3)
    
    moments = cv2.moments(cnts)
    
    if moments['m00'] != 0:
        cx = int(moments['m10'] / moments['m00'])
        cy = int(moments['m01'] / moments['m00'])
    centerMass = (cx,cy)
    
    
    cv2.circle(frame,centerMass,7,[100,0,255],2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Center',tuple(centerMass),font,2,(255,255,255),2)
    
    distanceBetweenDefectsToCenter = []
    for i in range(0,len(FarDefect)):
        x = np.array(FarDefect[i])
        centerMass = np.array(centerMass)
        distance = np.sqrt(np.power(x[0]-centerMass[0],2)+np.power(x[1]-centerMass[1],2))
        distanceBetweenDefectsToCenter.append(distance)
        
    sortedDefectsDistances = sorted(distanceBetweenDefectsToCenter)
    AverageDefectDistance = np.mean(sortedDefectsDistances[0:2])
    
    finger = []
    
    for i in range(0,len(hull)-1):
        if (np.absolute(hull[i][0][0] - hull[i+1][0][0]) > 80) or ( np.absolute(hull[i][0][1] - hull[i+1][0][1]) > 80):
            if hull[i][0][1] < 500:
                finger.append(hull[i][0])
    
    finger = sorted(finger,key=lambda x: x[1])
    fingers = finger[0:5]
    
    fingerDistance = []
    
    for i in range(0,len(fingers)):
        distance = np.sqrt(np.power(fingers[i][0]-centerMass[0],2)+np.power(fingers[i][1]-centerMass[0],2))
        fingerDistance.append(distance)
    
    result = 0
    for i in range(0,len(fingers)):
        if fingerDistance[i] > AverageDefectDistance + 130:
            result = result + 1
    
    #Print number of pointed fingers
    cv2.putText(frame,str(result),(100,100),font,2,(255,255,255),2)
    
    
    x,y,w,h = cv2.boundingRect(cnts)
    img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.drawContours(frame,[hull],-1,(255,255,255),2)
    
    ##show image ####
    
    cv2.imshow('Dilation',frame)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()








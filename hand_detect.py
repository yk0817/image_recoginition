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


while(1):
    start_time = time.time()
    print(cap.read())
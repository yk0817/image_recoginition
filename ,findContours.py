import cv2

img = cv2.imread("./test2.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE )

print("contours=",len(contours),  "hierarchy=",len(hierarchy) )

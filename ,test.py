# -*- coding: utf-8 -*-
import cv2
import random
import time


cap = cv2.VideoCapture(0)

cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 640)


while(True):
    start_time = time.time()
    # print(cap)
    ret, frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("camera", color)
    
    for loop_count in range(0, 10):
        hsv = cv2.cvtColor(color,cv2.cv.CV_BGR2HSV)
        # u"範囲にあれば全てのビットを１にする"
        mask = cv2.inRange(hsv, Scalar(0, 20, 20), Scalar(25, 255, 255), skin)
        print(mask)




# cap.release()
# cv2.destroyAllWindows()

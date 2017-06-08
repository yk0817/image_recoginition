# -*- coding: utf-8 -*-
import cv2
import random
import time
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 640)


while(True):
    start_time = time.time()
    # print(cap)
    ret, frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("camera", color)
    count_num = 0

    for loop_count in range(0, 10):
        hsv = cv2.cvtColor(color,cv2.cv.CV_BGR2HSV)
        # u"範囲にあれば全てのビットを１にする"
        color_lower_array = np.array([0,20,20])
        color_max_array = np.array([25,255,255])
        mask = cv2.inRange(hsv, color_lower_array, color_max_array)
        # print(mask)
        # u"フィルタリング構造を返す"
        structElem = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        # u"closingのタプルの扱いが謎"
        closing = cv2.morphologyEx(structElem, cv2.MORPH_CLOSE,(3,3))
        # cv2.imshow("camera", closing)
        find_contours,hierarchy = cv2.findContours(closing,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        # print(find_contour)
        largetstArea = 0
        for find_contour in find_contours:
            area = cv2.contourArea(find_contour)
            # print(find_contour[0][0][0])
            count_num += 1
            # if area > largetstArea:
            #     largetstArea = area

        



# cap.release()
# cv2.destroyAllWindows()

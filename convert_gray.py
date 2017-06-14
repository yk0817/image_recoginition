# -*- coding: utf-8 -*-
import cv2
import sys


img = cv2.imread("./hand.jpg")
# print(im.shape)
orgHeight, orgWidth = img.shape[:2]
size = (orgHeight/3, orgWidth/3)
halfImg = cv2.resize(img, size,interpolation=cv2.INTER_LINEAR)


gray = cv2.cvtColor(halfImg,cv2.COLOR_RGB2GRAY)
cv2.imshow("result",gray)
cv2.imwrite("output_gray.png", gray); 
cv2.waitKey(0)
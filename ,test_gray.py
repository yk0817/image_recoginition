# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("./test2.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('image', img)
cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
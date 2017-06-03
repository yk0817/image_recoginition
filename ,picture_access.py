# -*- coding: utf-8 -*-
import cv2
import numpy as np


# readImage

img = cv2.imread('./test3.jpg')

# pixelValue = img[90,100]

def pixelValue(width_pixel,height_pixel):
    return  img[width_pixel,height_pixel]


# print 'pixelValue = ' + str(pixelValue

for i in range(0,200):
    for j in range(0,200):
        print(pixelValue(i,j))
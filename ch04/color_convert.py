# coding: utf-8
# u"教科書----p47"
# http://rasp.hateblo.jp/entry/2016/01/22/230852
# u"resize"
import cv2
import math
import numpy as np
import sys

file_src = '../hand.jpg'
file_dst = '../hand.jpg'
img_src = cv2.imread(file_src,1)
img_dst= cv2.imread(file_dst,1)

height = img.shape[0]
width = img.shape[1]
cv2.namedWindow('src',cv2.WINDOW_NORMAL)
cv2.namedWindow('dst',cv2.WINDOW_NORMAL)

image_dst = cv2.flip(img_src, flipCode=0)

cv2.imshow('src',img_src)
cv2.imshow('dst',img_dst)

ch = cv2.waitKey(0)
cv2.destroyAllWindows
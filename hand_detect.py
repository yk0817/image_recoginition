import cv2
import numpy as np
import time

# ビデオキャプチャ
cap = cv2.VideoCapture(0)

#フレームサイズ減らす
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120);

def nothing(x):
    pass


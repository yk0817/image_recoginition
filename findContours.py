# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("./test2.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE )
# print("ret=",len(ret),  "hierarchy=",len(hierarchy) )

# print(ret[0][0])
# print(ret[0][1])
# print(len(ret[0][0]))

cv2.drawContours(img, ret[0], -1,(255,  0,  0),3)
cv2.drawContours(img, ret[1], -1,(  0,255,  0),3)
cv2.drawContours(img, ret[2], -1,(  0,  0,255),3)
cv2.drawContours(img, ret[3], -1,(255,255,  0),3)
cv2.drawContours(img, ret[4], -1,(  0,255,255),3)
cv2.drawContours(img, ret[5], -1,(255,  0,255),3)
cv2.drawContours(img, ret[6], -1,(  0,  0,  0),3)
cv2.imshow('image', img)
cv2.waitKey(0)


if key == 27:            #u'escの処理'
    cv2.destroyAllWindows()   
elif k == ord('s'):      #u'sの入力の処理''
    cv2.imwrite('forsave.jpg', img)
    cv2.destroyAllWindows()

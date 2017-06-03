import cv2

img = cv2.imread("./test2.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# ret, contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE )
ret,hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE )
# print("ret=",len(ret),  "hierarchy=",len(hierarchy) )

print(ret[0][0])
print(ret[0][1])
# print(len(ret[0][0]))

cv2.drawContours(img, ret[0], -1,(255,  0,  0),3)
cv2.drawContours(img, ret[1], -1,(  0,255,  0),3)
cv2.drawContours(img, ret[2], -1,(  0,  0,255),3)
cv2.drawContours(img, ret[3], -1,(255,255,  0),3)
cv2.drawContours(img, ret[4], -1,(  0,255,255),3)
cv2.drawContours(img, ret[5], -1,(255,  0,255),3)
cv2.drawContours(img, ret[6], -1,(  0,  0,  0),3)


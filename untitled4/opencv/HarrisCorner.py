import cv2
import numpy as np

img=cv2.imread('wifi.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
dst=cv2.cornerHarris(gray,10,3,0.1)
dst=cv2.dilate(dst,None)

img[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('dst',img)
if cv2.waitKey(0)&0xff==27:
    cv2.destroyAllWindows()
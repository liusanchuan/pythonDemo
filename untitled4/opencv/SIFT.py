import cv2
import numpy as np
img=cv2.imread('wifi.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift=cv2.SURF()
cv2=sift.detect(gray,None)
img=cv2.drawKeypoints(gray,img)
cv2.imshow(",",img)
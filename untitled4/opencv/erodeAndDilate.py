import cv2
import numpy as np

img=cv2.imread('j.png')
for i in range(0,img.shape[0],5):
    for j in range(0,img.shape[1],5):
        img[i,j]=[0,0,0]
cv2.imshow("", img)

kernel=np.ones((2,2),np.uint8)
erosion=cv2.dilate(img,kernel,iterations=1)
erosion=cv2.erode(erosion,kernel,iterations=1)
cv2.imshow("se",erosion)
# erosion=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow("none",erosion)
gradient=cv2.morphologyEx(erosion,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("1231",gradient)

if cv2.waitKey(0)&0xff==27:
    cv2.destroyAllWindows()
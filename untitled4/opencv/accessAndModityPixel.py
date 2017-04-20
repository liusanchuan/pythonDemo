import cv2
import numpy as np

img=cv2.imread('123.jpg')

for i in range(img.shape[0]-10):

        img[i,i]=[255,255,255]
        img[i+5,i]=[255,255,255]
        img[i-5,i]=[255,255,255]

print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))
print(img.dtype)

#Copy the Region of one area
noise=img[163:199,201:267]
img[0:36,0:66]=noise
b,g,r=cv2.split(img)
cv2.imshow('img',r)


print(img.shape)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
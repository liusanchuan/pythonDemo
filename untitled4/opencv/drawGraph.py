import numpy as np
import cv2
im=np.zeros((512,512,3),np.uint8)
img=cv2.line(im,(0,0),(511,511),(255,0,0),1)
img=cv2.rectangle(img,(384,0),(510,128),(0,255,0),2)
img=cv2.circle(img,(447,63),63,(0,0,225),1)
pts=np.array([[40,55],
              [20,30],
              [70,20],
              [50,10]
              ],np.int32)
pts=pts.reshape((-1,1,2))
img=cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow('img',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
else:
    cv2.imwrite('messigray.jpg',img)

cv2.destroyAllWindows()
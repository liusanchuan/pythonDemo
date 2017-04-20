import numpy as np
import cv2
from matplotlib import pyplot as plt
img1=cv2.imread('123.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread('123.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img1,cmap='gray')
plt.show()
cv2.imshow('image',img1)
# cv2.imshow('image',img2)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
else:
    cv2.imwrite('messigray.jpg',img1)

cv2.destroyAllWindows()

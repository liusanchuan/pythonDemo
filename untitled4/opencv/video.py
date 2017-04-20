import numpy as np
import cv2
# cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("C:/Users/Administrator/Videos/NN III Animatic-HD.mp4")
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2RGBA)

    cv2.imshow('frame',gray)
    if cv2.waitKey(25)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

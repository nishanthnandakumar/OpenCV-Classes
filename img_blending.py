import numpy as np
import cv2

img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('cup.jpg')

dst = cv2.addWeighted(img1,0.7,img2,0.3,0) #dst = alpha . img1 + beta . img2 + gamma

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

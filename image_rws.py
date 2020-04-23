import numpy as np
import cv2
import sys

img = cv2.imread('messi.jpg',0)#if directory is not known use cv.samples.findFile to search
# 0,1,-1 can be passed for grayscale coloured and unchanged images

if img is None:
    sys.exit("Could not read the image")

cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()

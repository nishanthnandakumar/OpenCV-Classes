import numpy as np
import cv2

cap = cv2.VideoCapture(0) #To specify the camera pass arguments as 0,1,2

while(True):
    #Capture frame-by frame
    ret, frame = cap.read()

    # Our operations on the frame come next
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Change coloured video to grayscale

    #Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#when everything is done, release the Capture
cap.release()
cv2.destroyAllWindows()

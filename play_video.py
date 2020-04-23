import numpy as np
import cv2

cap = cv2.VideoCapture('output.avi') #To specify the file location

while(cap.isOpened()):
    #Capture frame-by frame
    ret, frame = cap.read()

    # Our operations on the frame come next
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Change coloured video to grayscale

    #Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):    #use appropriate time for wait key if less too fast or too slow. use 25 for optimum
        break

#when everything is done, release the Capture
cap.release()
cv2.destroyAllWindows()

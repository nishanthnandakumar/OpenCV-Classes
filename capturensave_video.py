import numpy as np
import cv2

cap = cv2.VideoCapture(0) #To specify the camera

#Define the codec and creaye VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID') #used to specify the video codec
out = cv2.VideoWriter('output1.avi',fourcc, 20.0, (640,480)) #video writer object is created output file name, fourcc code, no. of frames per second, frame size
#last one is isColor flag if true then expect color frame or grayscale

while(cap.isOpened()):
    #Capture frame-by frame
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.flip(frame,0)

        #write the flipped frame
        out.write(frame)

        #Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):    #use appropriate time for wait key if less too fast or too slow. use 25 for optimum
            break
    else:
        break


#when everything is done, release the Capture
cap.release()
out.release()
cv2.destroyAllWindows()

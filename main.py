import cv2
import sys
import logging as log
import datetime as dt
from time import sleep

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)



cap = cv2.VideoCapture('fishies.mp4')

#while(cap.isOpened()):
    
video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    ret2, frame2 = cap.read()
    # Capture frame-by-frame
    if (ret2==False):
        break

    cond=0
    while(cond==0):
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if anterior != len(faces):
            anterior = len(faces)
            log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))
        cond=len(faces)
    


    cv2.imshow('frame',frame2)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
        
    

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()





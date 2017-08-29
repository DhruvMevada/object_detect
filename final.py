import cv2
import numpy as np

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    if(ret):
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            
            if(Id==5):
                Id="Dhruv"
            
            else:
                Id="Unknown"
            cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)    
            cv2.imshow('im',im) 
    else:
        print("Error")
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

import cv2
import os
cam = cv2.VideoCapture('video1.avi')
cam.open('video1.avi')
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id=raw_input('enter your id - ')
sampleNum=0
print("1")
while(True):
    print("1")
    #img =cam.read()
    ret,img =  cam.read()
    
    if(ret):
        print("2")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        vehicles = detector.detectMultiScale(gray, 1.3, 5)
        print("3")
        for (x,y,w,h) in vehicles:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            print("3")
           
            sampleNum=sampleNum+1
            cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
    
            cv2.imshow('frame',img)
    else:
        print("5")
        print "Please provide Camera Access"
        break
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
   
    elif sampleNum>100:
        break
cam.release()
cv2.destroyAllWindows()

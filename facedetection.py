# open source computer vision opencv
import cv2
trainedfacemodel=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # already trained load
webcamb=cv2.VideoCapture(0) # capture video... webcamp opening irruim webcamp
while True:
    workingcorrectly,video =webcamb.read() # read all from webcam and give (true or false)|| frame
    blacknwhite =cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    face=trainedfacemodel.detectMultiScale(blacknwhite) # detecting face ...
    for(x,y,w,h) in face:
        cv2.rectangle(video,(x,y),(x+w,y+h),(0,0,255),2) # first providing the img in the name of video
    cv2.imshow("Nameofwindowgunal",video) # show the image in new window 
    key=cv2.waitKey(1) # wait until enter any button
    if key==27:
        break # quit() or break...
    

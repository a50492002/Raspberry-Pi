import cv2
import os
import sys
import time
from datetime import datetime

def img(n,s=None):
    if s==None:
        #x=0 if n-10<0 else n-10
        x=n-10
        return x;
    else:
        #x=s if n+10>s else n+10
        x=n+10
        return x;
    


alt2='haarcascade_frontalface_alt2.xml' # 人臉檢測器（快速Harr）
default='haarcascade_frontalface_default.xml' # 人臉檢測器（預設）
alt='haarcascade_frontalface_alt.xml'# 人臉檢測器
faceCascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/'+alt2)
#faceCascade = cv2.CascadeClassifier(v2.data.haarcascades+alt2)

# Video source
#capture = cv2.VideoCapture("WIN_20191004_18_03_52_Pro.mp4") # 測試影片(單人)
#capture = cv2.VideoCapture("WIN_20191005_11_01_06_Pro.mp4") # 測試影片(多人)
capture = cv2.VideoCapture(0) # 攝像頭0
#set
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

color = (0, 255, 0)

# get video fps
fps=round(capture.get(cv2.CAP_PROP_FPS))
#fps = 30
vw = capture.get(cv2.CAP_PROP_FRAME_WIDTH) # float
#vw = 1280
vh = capture.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
#vh = 720
print(fps,vw,vh)

count = 0
while(True):
    success, frame = capture.read()
    if success:
        Start = time.time()
        nowtime=datetime.now()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#轉灰階
        
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(36, 36)
        )
        
        if len(faces) > 0:  
            i=1
            for face in faces:
                x, y, w, h = face
                img_name = 'image/{0}.jpg'.format(str(nowtime)+'_'+str(i))
                #image = frame[img(y) : img((y+h),vh), img(x) : img((x+w),vw)]
                image = frame[y:y+h,x:x+w]
                cv2.imwrite(img_name, image)
                
                cv2.rectangle(frame, (img(x), img(y)), (img((x+w),vw),img((y+h),vh)), color, 2)
                i+=1
        #img_name = 'image/{0}.jpg'.format(str(nowtime))
        #cv2.imwrite(img_name, frame)
        print(str(time.time()-Start)+' sec, get '+str(len(faces))+' Face')
        cv2.imshow('I see you!',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()
capture.release()

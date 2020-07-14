import cv2
import os
import sys
import time
from datetime import datetime

alt2='haarcascade_frontalface_alt2.xml' # 人臉檢測器（快速Harr）
default='haarcascade_frontalface_default.xml' # 人臉檢測器（預設）
alt='haarcascade_frontalface_alt.xml'# 人臉檢測器
faceCascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/'+alt2)

# Video source
#capture = cv2.VideoCapture("WIN_20191004_18_03_52_Pro.mp4") # 測試影片(單人)
capture = cv2.VideoCapture("WIN_20191005_11_01_06_Pro.mp4") # 測試影片(多人)
#capture = cv2.VideoCapture(0) # 攝像頭0
color = (0, 255, 0)

# get video fps
fps=round(capture.get(cv2.CAP_PROP_FPS))
vw = capture.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
vh = capture.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
print(fps,vw,vh)

def img(n,s=None):
    if s==None:
        #x=0 if n-10<0 else n-10
        x=n-10
        return x;
    else:
        #x=s if n+10>s else n+10
        x=n+10
        return x;
    
count = 0
while capture.isOpened():
    success, frame = capture.read()
    if count%fps==0:
        if success:
            Start = time.time()
            nowtime=datetime.now()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#轉灰階
            
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
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
                    #cv2.rectangle(frame, (img(x), img(y)), (img((x+w),vw),img((y+h),vh)), color, 2)
                    i+=1
                #img_name = 'image/{0}.jpg'.format(str(nowtime))
                #cv2.imwrite(img_name, fr ame)
                print(str(time.time()-Start)+' sec, get '+str(len(faces))+' Face')
        else:
            break
    count += 1
cv2.destroyAllWindows()
capture.release()

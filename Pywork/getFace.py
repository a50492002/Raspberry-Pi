import cv2
import os
import sys
import time
from datetime import datetime

alt2='haarcascade_frontalface_alt2.xml' # 人臉檢測器（快速Harr）
default='haarcascade_frontalface_default.xml' # 人臉檢測器（預設）
alt='haarcascade_frontalface_alt.xml'# 人臉檢測器
faceCascade = cv2.CascadeClassifier('/home/pi/pywork/opencv/data/haarcascades/'+alt2)

# Video source
#capture = cv2.VideoCapture("WIN_20191004_18_03_52_Pro.mp4") # 測試影片(單人)
capture = cv2.VideoCapture("WIN_20191005_11_01_06_Pro.mp4") # 測試影片(多人)
#capture = cv2.VideoCapture(0) # 攝像頭0

# get video fps
fps=round(capture.get(cv2.CAP_PROP_FPS))

count = 0
number = 0
while capture.isOpened():
    success, frame = capture.read()
    if count%fps==0:
        if success:
            
            nowtime=datetime.now()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#轉灰階
            
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=1,
                minSize=(36, 36),
                flags=cv2.CASCADE_DO_CANNY_PRUNING
            )
            
            if len(faces) > 0:  
                i=1
                for face in faces:
                    x, y, w, h = face
                    img_name = '%s.jpg'%('image/'+str(nowtime)+'_'+str(i))
                    image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                    cv2.imwrite(img_name, image)
                    i+=1
            number += 1
        else:
            break
    count += 1
cv2.destroyAllWindows()
capture.release()

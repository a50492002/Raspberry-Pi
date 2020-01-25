import numpy as np
import cv2 as cv
import os
import sys
import time
from datetime import datetime

net = cv.dnn.readNet('face-detection-adas-0001.xml',
                     'face-detection-adas-0001.bin')
net.setPreferableTarget(cv.dnn.DNN_TARGET_MYRIAD)

cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FPS,15)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

fps=round(cap.get(cv.CAP_PROP_FPS))
#fps = 30
vw = cap.get(cv.CAP_PROP_FRAME_WIDTH) # float
#vw = 1280
vh = cap.get(cv.CAP_PROP_FRAME_HEIGHT) # float
#vh = 720
print(fps,vw,vh)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    Start = time.time()
    nowtime=datetime.now()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    blob = cv.dnn.blobFromImage(frame, size=(672, 384), ddepth=cv.CV_8U) #預設 size=(672, 384)
    net.setInput(blob)
    out = net.forward()
    # Draw detected faces on the frame.
    i = 0
    for detection in out.reshape(-1, 7):
        confidence = float(detection[2])
        xmin = int(detection[3] * frame.shape[1])
        ymin = int(detection[4] * frame.shape[0])
        xmax = int(detection[5] * frame.shape[1])
        ymax = int(detection[6] * frame.shape[0])
        dx = xmax - xmin 
        dy = ymax - ymin
        if confidence > 0.5 and dx >= 36 and dy >= 36:
            image = frame[ ymin : ymax, xmin : xmax ]
            img_name = 'Image/{0}.jpg'.format(nowtime.strftime("%Y%m%d_%H:%M:%S")+'_'+str(i))
            print('{0}'.format(nowtime.strftime("%Y/%m/%d %H:%M:%S")+' '+str(i)))
            cv.imwrite(img_name,image)
            i+=1
# When everything done, release the capture
cv.destroyAllWindows()
cap.release()

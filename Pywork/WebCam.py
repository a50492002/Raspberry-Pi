import cv2
import os
import sys

capture = cv2.VideoCapture(0) # 攝像頭0
#set
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

count = 0
while(True):
    success, frame = capture.read()
    if success:
        cv2.imshow('I see you!',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()
capture.release()


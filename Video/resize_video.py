import cv2 as cv
import numpy as np

vid = cv.VideoCapture("naruto_sasuke_reunion.mp4")

if (vid.isOpened() == False):
    print("Error opening video file")

while(vid.isOpened()):
    width = 1000
    height = 700
    ret, frame = vid.read()
    # resize syntax --> image/video, (width, height), interpolation_type
    frame = cv.resize(frame, (width, height), interpolation=cv.INTER_CUBIC)
    cv.imshow("Naruto-Sasuke Reunion",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv.destroyAllWindows()
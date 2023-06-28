import cv2 as cv
import numpy as np

# cv2.VideoCapture(0): Means first camera or webcam.
# cv2.VideoCapture(1):  Means second camera or webcam.
vid = cv.VideoCapture("naruto_sasuke_reunion.mp4")

if (vid.isOpened() == False):
    print("Error opening video file")

while(vid.isOpened()):
    ret, frame = vid.read()
    cv.imshow("Naruto-Sasuke Reunion",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        # if you give someother waitkey instead of giving & and some letter the video won't be played
        # only if q is pressed the player will be terminated
        break
vid.release()
cv.destroyAllWindows()
import cv2 as cv

video = cv.VideoCapture("naruto_sasuke_reunion.mp4")

if (video.isOpened() == False):
	print("Error reading video file")
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
# size = (1000,700) doesn't work as we have to give a proper resolution for the video that is gonna be saved
# VideoWriter syntax --> videoname with extension, fourcc, fps, framesize
# fourcc is a 4 character code of codec used to compress the frames
out = cv.VideoWriter('naruto_sasuke_reunion.avi', cv.VideoWriter_fourcc(*'MJPG'), 60, size)

while(True):
    ret, frame = video.read()
    out.write(frame)
    cv.imshow('Frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
    	break

video.release()
out.release()
cv.destroyAllWindows()
print("The video was successfully saved")

import cv2 as cv
import numpy as np

img = np.zeros((720,720,3), dtype='uint8')
img[:]=(0,0,0)
img2 = cv.imread("naruto.png",1)
# cv.line(image, startpoint, endpoint, color, thickness, others)
cv.line(img, (0,0), (800,800), (256,256,256),10)
cv.imshow('Drawing a Line',img)
cv.waitKey()
cv.destroyAllWindows()
cv.line(img2, (0,0), (800,800), (256,256,256),10)
cv.imshow('Drawing in Image',img2)
cv.waitKey()
cv.destroyAllWindows()
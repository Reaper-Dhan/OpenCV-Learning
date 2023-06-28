import cv2 as cv
import numpy as np

img = cv.imread("naruto.png")
cols = img.shape[1]
rows = img.shape[0]
center = (cols/2,rows/2)
angle = 180
x = cv.getRotationMatrix2D(center, angle, 1)
rotate = cv.warpAffine(img, x, (cols,rows))
cv.imshow('Rotated Image',rotate)
cv.waitKey()
cv.destroyAllWindows()
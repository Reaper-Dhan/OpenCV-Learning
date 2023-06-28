import cv2 as cv
import numpy as np

img = np.zeros((800,800,3), dtype='uint8')
# cv.rectangle(image, startpoint, endpoint, color, thickness, others)
# if thickness is positive then it will produce only the border of the shape while negative produces a fill of the shape
cv.rectangle(img, (100,150), (700,450), (256,256,256), -3, lineType=4, shift=0)
cv.imshow('Drawing a rectangle',img)
cv.waitKey()
cv.destroyAllWindows()
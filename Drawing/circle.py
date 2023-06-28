import cv2 as cv
import numpy as np

img = np.zeros((800,800,3), dtype='uint8')
# cv.circle(image, center_coordinates, radius, color, thickness)
# thickness --> -1 --> outline, +ve --> opaque
cv.circle(img, (250, 250), 150 , (256,256,256), -1)
cv.imshow('Drawing a circle',img)
cv.waitKey()
cv.destroyAllWindows()
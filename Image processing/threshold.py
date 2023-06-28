import cv2 as cv
import numpy as np

img = cv.imread("naruto.png",0)
threshold = 100
(T_value, binary_threshold) = cv.threshold(img, threshold, 255, cv.THRESH_BINARY)
cv.imshow("Threshold Image",binary_threshold)
cv.waitKey()
cv.destroyAllWindows()

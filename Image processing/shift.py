import cv2 as cv
import numpy as np

img = cv.imread("naruto.png")
cols = img.shape[1]
rows = img.shape[0]
x = np.float32([[1,0,150], [0,1,-70]])
shifted = cv.warpAffine(img, x, (cols,rows))
cv.imshow('Shifted Image',shifted)
cv.waitKey()
cv.destroyAllWindows()
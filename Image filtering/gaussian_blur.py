import cv2 as cv
import numpy as np

img = cv.imread("naruto.png")
# The Gaussian blur is a way to apply a low-pass filter in skimage.
# It is often used to remove Gaussian (i. e., random) noise from the image.
# GaussianBlur syntax --> img, matrix(size), others
blur1 = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
blur2 = cv.GaussianBlur(img, (15,15), cv.BORDER_DEFAULT)
cv.imshow("Gaussian Blur",np.hstack((blur1,blur2)))
cv.waitKey()
cv.destroyAllWindows()
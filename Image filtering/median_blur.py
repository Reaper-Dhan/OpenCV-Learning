import cv2 as cv
import numpy as np

img = cv.imread("naruto.png")
# The Median blur operation is similar to the other averaging methods.
# Here, the central element of the image is replaced by the median of all the pixels in the kernel area.
# medianBlur syntax --> image, kernal(amount of kernalization), others
blur1 = cv.medianBlur(img, 5)
blur2 = cv.medianBlur(img, 15)
cv.imshow("Median Blur",np.hstack((blur1,blur2)))
cv.waitKey()
cv.destroyAllWindows()
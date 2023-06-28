import cv2 as cv
import numpy as np

img = cv.imread("naruto.png")
print("The size of the image is...\n",np.shape(img))
new = cv.resize(img, (400,400))
print("\nThe size of the image after resizing is...\n",np.shape(new))
cv.imshow("Resized Image",new)
cv.waitKey()
cv.destroyAllWindows()
import cv2 as cv
import numpy as np

img = cv.imread("naruto_noise.png")
# A bilateral filter is used for smoothening images and reducing noise, while preserving edges.
# bilateralFilter syntax --> image, diameter of each pixel neighborhood, color, space
clear = cv.bilateralFilter(img, 100, 100, 100)
img_text = cv.putText(img, "NOISY", (10,650), cv.FONT_HERSHEY_SIMPLEX, 1.1, color=(255,255,255), thickness=5)
img_text = cv.putText(clear, "CLEAR", (10,650), cv.FONT_HERSHEY_SIMPLEX, 1.1, color=(255,255,255), thickness=5)
cv.imshow("Bilateral Filter", np.hstack((img,clear)))
cv.waitKey()
cv.destroyAllWindows()

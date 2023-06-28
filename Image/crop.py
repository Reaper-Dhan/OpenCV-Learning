import cv2 as cv

img = cv.imread("naruto.png")
crop = img[0:360, 0:360]
cv.imshow('Cropped Image', crop)
cv.waitKey()
cv.destroyAllWindows()
import cv2 as cv

img = cv.imread("naruto.png",1)
cv.imshow("Original Image",img)
cv.waitKey()
cv.destroyAllWindows()
cv.imwrite("naruto_bgr.jpg",img)

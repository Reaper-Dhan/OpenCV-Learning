import cv2 as cv

img1 = cv.imread("naruto.png") # original
img2 = cv.imread("naruto.png",0) # grayscale
img3 = cv.imread("naruto.png",1) # good color (BGR channel)
cv.imshow("Original Image",img1)
cv.waitKey()
cv.destroyAllWindows()
cv.imshow("Grayscale Image",img2)
cv.waitKey()
cv.destroyAllWindows()
cv.imshow("BGR Image",img3)
cv.waitKey()
cv.destroyAllWindows()
# IMPORTANT TO LEARN THIS
# THIS TECHNIQUE IS USED TO DETECT FEATURES LIKE LICENsE PLATE, AADHAR CARD, PEDESTRIANS, ETC.,.
# ESPECIALLY MINUTE DETAILS IN A MEDIA
# THIS IS ALSO CALLED AS CONTOUR DETECTION
import cv2 as cv
import numpy as np

img = cv.imread("naruto.png")
# Canny usually detects the edges of the image accurately
# Canny syntax --> image, Threshold_lower, Threshold_upper, aperture_size, L2Gradient
# Threshold_upper and Threshold_lower is the amount of edges that it want to display
edge = cv.Canny(img, 10, 20)
cv.imshow("Canny Edge Detector", edge)
cv.waitKey()
cv.destroyAllWindows()
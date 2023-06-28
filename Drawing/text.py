import cv2 as cv
import numpy as np

img = np.ones((800,800,3), dtype='uint8')
font = cv.FONT_HERSHEY_COMPLEX
# putText format is... image,text,position,font,font-size,color,line-size,line-type
cv.putText(img, 'Naruto Uzumaki',(150,400), font, 2, (255,255,255), 6, cv.LINE_4)
cv.imshow('Writing Text',img)
cv.waitKey()
cv.destroyAllWindows()
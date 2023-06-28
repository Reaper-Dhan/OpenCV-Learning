import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io

img = io.imread("naruto.png")
x = int(input("Enter a number for x-axis :"))
y = int(input("Enter a number for y-axis :"))
r = cv.resize(img,(x,y))
t = ["Orginal Image","Resized Image"]
im=[img,r]
for i in range(2):
  plt.subplot(1,2,i+1)
  plt.title(t[i])
  plt.imshow(im[i])
  plt.axis('off')
plt.show()
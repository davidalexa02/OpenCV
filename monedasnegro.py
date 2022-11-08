import numpy as np
import cv2 as cv

# Load two images
img1 = cv.imread('monedasazul.jpg')
imgre=cv.resize(img1,(800,800))

rows,cols,channels = imgre.shape
roi = imgre[0:rows, 0:cols]
hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
lower_blue = np.array([85,50,50])
upper_blue = np.array([130,255,255])
mask = cv.inRange(hsv, lower_blue, upper_blue)
res = cv.bitwise_not(mask)
cv.imshow('roi',res)
cv.waitKey(0)
cv.destroyAllWindows()
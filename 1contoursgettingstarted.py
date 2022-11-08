import numpy as np
import cv2 as cv
from matplotlib import pyplot as plet
im = cv.imread('circulocuadrado.jpg')
%matplotlib auto
plet.imshow(im)
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
#pierde la tercera dimension porque pierde el brillo?
plet.imshow(imgray)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
#para esta version se necesitaran 3 valores: img2, contours y hierarchy
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#cv.RETR_TREE: 
#contours tiene los contornos
#hierarchy le sirve para ver si hay algun contorno que este en un nivel hierarjico superior a otro
# cnt=contours[1]
# cv.drawContours(im, [cnt], 0, (0,255,0), 3)
cv.drawContours(im, contours, 0, (0,255,0), 3)
cv.drawContours(im, contours, 1, (255,0,0), 3)
cv.drawContours(im, contours, 2, (0,0,255), 3)
cv.drawContours(im, contours, 3, (0,255,255), 3)
cv.drawContours(im, contours, 4, (255,255,0), 3)
cv.drawContours(im, contours, 5, (255,0,255), 3)
plet.imshow(im)
#thresh=cv.bitwise_not(thresh1)
#thresh=thresh1
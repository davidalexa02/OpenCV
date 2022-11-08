# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:17:57 2022

@author: CleanPC - Service IT
"""

import numpy as np
import cv2 as cv
AMARILLO=(0,255,255)
# BLANCO=(0,0,0)
# NEGRO=(255,255,255)
im = cv.imread('imagencontours.jpg')
imm= cv.imread('monedasazul.jpg')
imgre=cv.resize(im,(800,800))
immgre=cv.resize(imm,(800,800))
cv.imshow('imgre',imgre)
imghsv = cv.cvtColor(imgre, cv.COLOR_BGR2HSV)
img2hsv = cv.cvtColor(immgre, cv.COLOR_BGR2HSV)
#pierde la tercera dimension porque pierde el brillo?

# define range of blue color in HSV
lower_blue = np.array([80,50,50])
upper_blue = np.array([160,255,255])
# white=np.array([0,0,0])
# black=np.array([255,255,255])
# Threshold the HSV image to get only blue colors
mask = cv.inRange(imghsv, lower_blue, upper_blue)
res = cv.bitwise_not(mask)
img2_fg = cv.bitwise_and(imgre,imgre,mask = res)
# dst=cv.add(img2_fg,immgre)
cv.imshow('mask',mask)
ret, thresh = cv.threshold(mask, 127, 255, 0)
# dilate thresholded image - merges top/bottom 
# kernel = np.ones((3,3), np.uint8)
# dilated = cv.dilate(thresh, kernel, iterations=3)
# cv.imshow('threshold dilated',dilated)
cv.imshow('thresh',thresh)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#para esta version se necesitaran 3 valores: img2, contours y hierarchy
# cv.drawContours(img2_fg, contours,0,AMARILLO , 3)

for i in range(len(contours)):
    M=cv.moments(contours[i])
    cx=int(M['m10']/M['m00'])
    cy=int(M['m01']/M['m00'])
    centro=(cx,cy)
    print(centro)
#como meter la pelicula en los 4 puntos(hay que aproximar primero)
epsilon = 0.08*cv.arcLength(contours[0],True)
approx = cv.approxPolyDP(contours[0],epsilon,True)
cv.drawContours(img2_fg, [approx], 0,AMARILLO, 3)
cv.imshow('img2_fg',img2_fg)
rows,cols,ch = immgre.shape
pts2 = np.float32([[0,0],[0,cols],[cols,rows],[cols,0]])
W = approx.reshape(4,2)
approx2=np.float32(W)
Me = cv.getPerspectiveTransform(pts2,approx2)
dst2 = cv.warpPerspective(immgre,Me,(800,800))
added=cv.add(img2_fg,dst2)
cv.imshow('dst2',dst2)
cv.imshow('dst2',added)
#como encontrar contor mas facil?
# cv.imshow('imgre',imgre)
# cv.imshow('added',added)
cv.waitKey(0)
cv.destroyAllWindows()
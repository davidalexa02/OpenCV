import numpy as np
import cv2 as cv
from matplotlib import pyplot as plet
img = cv.imread('imagencontours.jpg')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
%matplotlib auto
# ret,thresh = cv.threshold(imgray,127,255,0)
# im2,contours,hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cnt0 = contours[0]
# cnt1 = contours[1]
# cnt2 = contours[2]
# cnt3 = contours[3]
# cnt4 = contours[4]
# cnt5 = contours[5]
# colors=[(0,255,0),(255,0,0),(0,0,255),(0,255,255),(255,255,0),(255,0,255)]
# posiciones=[(405,317),(539,216),(273,216),(407,217),(405,115),(405,216)]
# for i in range(len(contours)):
#     cv.drawContours(img, contours[i], i, 
#                     (0,0,0), 3)
#     M=cv.moments(contours[i])
#     cx=int(M['m10']/M['m00'])
#     cy=int(M['m01']/M['m00'])
#     centro=(cx,cy)
#     print("el contorno ",i," tiene el area ",cv.contourArea(contours[i])," con el perimetro ",cv.arcLength(contours[i],True)
# ," y el centro en ",centro)
#     font=cv.FONT_HERSHEY_SIMPLEX
#     cv.putText(img, str(i), posiciones[i], font, 2, (0,255,0),2,cv.LINE_AA)
    
plet.imshow(img)
# M0 = cv.moments(cnt0)
# print( M0 )
# print("  ")
# M1 = cv.moments(cnt1)
# print( M1 )
# print("  ")
# M2 = cv.moments(cnt2)
# print( M2 )
# print("  ")
# M3 = cv.moments(cnt3)
# print( M3 )
# print("  ")
# M4 = cv.moments(cnt4)
# print( M4 )
# print("  ")
# M5 = cv.moments(cnt5)
# print( M1 )
# print("  ")
# area5 = cv.contourArea(cnt5)
# print(area5)
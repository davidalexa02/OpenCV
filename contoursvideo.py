# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:38:13 2022

@author: CleanPC - Service IT
"""

import numpy as np
import cv2 as cv
import csv
# from decimal import Decimal, getcontext

# getcontext().prec = 2*n
AMARILLO=(0,255,255)
# BLANCO=(0,0,0)
# NEGRO=(255,255,255)
cap = cv.VideoCapture('video11.mp4')
cap2 = cv.VideoCapture('pelotaroja.mp4')
cap.set(cv.CAP_PROP_POS_MSEC,5000)

# def take_second(elem):
#     return elem[1]

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while(1):
    # Take each frame
    ret,im = cap.read()
    ret2,imm= cap2.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    if not ret2:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #se cambia el espacio de color y se buscan los pixels de color rojo
    
    # cv.imshow('video',im)
    imgrere=cv.resize(im,(800,800))
    imgrerot=cv.resize(imm,(800,800))
    imgre=cv.rotate(imgrere,cv.ROTATE_90_CLOCKWISE)
    rows,cols,ch = imgrerot.shape
    pts2 = np.float32([[cols,0],[0,0],[0,rows],[cols,rows]])
    hsv = cv.cvtColor(imgre, cv.COLOR_BGR2HSV)
    lower_blue = np.array([80,50,50])
    upper_blue = np.array([160,255,255])
    # Se localizan los puntos rojos
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    res = cv.bitwise_not(mask)
    img2_fg = cv.bitwise_and(imgre,imgre,mask = res)
    cv.imshow('mask',mask)
    ret, thresh = cv.threshold(mask, 124, 255, 0)
    
    
    cv.imshow('thresh',thresh)
    im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #se utilizan los momentos de orden 0 y 1 para calcular las coordenadas x e y del centro de la pelota
    
    
    for i in range(len(contours)):
        epsilon = 0.08*cv.arcLength(contours[i],True)
        approx = cv.approxPolyDP(contours[i],epsilon,True)
        
        ap=len(approx)
        # cv.drawContours(img2_fg, [approx], 0,AMARILLO, 3)
        cv.imshow('img2_fg',img2_fg)
        W = approx.reshape(ap,2)
        # approx2 = sorted(W, key=take_second)
    approx2=np.float32(W)
    # with open("approx.csv", "a", newline ='') as csvfile:
    #     wr = csv.writer(csvfile, dialect='excel', delimiter=',' )
    #     wr.writerow(approx2)
        # sort coordenadas:
            
    ap2=len(approx2)
        
        # #de izquierda a derecha
        # for i in range(ap2):
        #     for j in range(0,ap2-i-1):
        #     #si es la columna mas grande esta a la derecha
        #         if(approx2[j][0]>approx2[j+1][0]):
        #             # arr=
        #             approx2[j][0],approx2[j+1][0]=approx2[j+1][0],approx2[j][0]
        #             approx2[j][1],approx2[j+1][1]=approx2[j+1][1],approx2[j][1]
                    
        
                    
        # arr.append(np.amin(approx2, axis=0))
        # arr.append(max(approx2))
        #de arriba abajo
    # for i in range(ap2):
    #     for j in range(0,ap2-i-1):
    #         #si es la columna mas grande esta a la derecha
    #         if(approx2[j][1]>approx2[j+1][1]):
    #             approx2[j][0],approx2[j+1][0]=approx2[j+1][0],approx2[j][0]
    #             approx2[j][1],approx2[j+1][1]=approx2[j+1][1],approx2[j][1]
                    
        #de izquierda a derecha
    # for i in range(ap2):
    #         for j in range(0,ap2-i-1):
    #         #si es la columna mas grande esta a la derecha
    #             if(approx2[j][0]>approx2[j+1][0]):
    #                 # arr=
    #                 approx2[j][0],approx2[j+1][0]=approx2[j+1][0],approx2[j][0]
    #                 approx2[j][1],approx2[j+1][1]=approx2[j+1][1],approx2[j][1]
                    
        
        # arr2.append(min(approx2))
        # arr2.append(max(approx2))
        # arrt.append(arr, arr2, axis=0)
        
        
        # leftmost = tuple(contours[contours[:,:,0].argmin()][0])
        # rightmost = tuple(contours[contours[:,:,0].argmax()][0])
        # topmost = tuple(contours[contours[:,:,1].argmin()][0])
        # bottommost = tuple(contours[contours[:,:,1].argmax()][0])
        
        
        # pts1 = np.float32([[approx2[0][0],approx2[0][1]],[approx2[1][0],approx2[1][1]],[approx2[2][0],approx2[2][1]],[approx2[3][0],approx2[3][1]]])
   
    # pts
    Me = cv.getPerspectiveTransform(pts2,approx2)
    dst2 = cv.warpPerspective(imgrerot,Me,(800,800))
    added=cv.add(img2_fg,dst2)
    cv.imshow('dst2',dst2)
    cv.imshow('dst',added)
    
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
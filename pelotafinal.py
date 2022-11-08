# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:18:41 2022

@author: CleanPC - Service IT
"""

import cv2 as cv
import numpy as np
import csv

RED = (0,0,255)
posiciones=[]

cap = cv.VideoCapture('pelotaroja.mp4')
cap.set(cv.CAP_PROP_POS_MSEC,3000)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while(1):
    # Take each frame
    ret,im = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #se cambia el espacio de color y se buscan los pixels de color rojo
    imgre=cv.resize(im,(800,800))
    hsv = cv.cvtColor(imgre, cv.COLOR_BGR2HSV)
    rojo_inferior = np.array([150,200,95])
    rojo_superior = np.array([190,240,115])
    # Se localizan los puntos rojos
    pelota = cv.inRange(hsv, rojo_inferior, rojo_superior)
    #se utilizan los momentos de orden 0 y 1 para calcular las coordenadas x e y del centro de la pelota
    m = cv.moments(pelota)
    if m['m00']!=0:
        x = m['m10']/m['m00']
        y = m['m01']/m['m00']
        posiciones = [int(x),int(y)]
        # guardar en csv
        with open("Phj.csv", "a", newline ='') as csvfile:
            wr = csv.writer(csvfile, dialect='excel', delimiter=',')
            wr.writerow(posiciones)
        # se crea una copia de la pelota con una marca en el centro
        marcado=imgre.copy()
        #frame con fondo negro
        # marcado = np.zeros((800,800,3), np.uint8)
        # marcado.fill(0)
        cv.circle(marcado, (int(x),int(y)),50,RED,cv.FILLED)
    
    cv.imshow('in',marcado)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()

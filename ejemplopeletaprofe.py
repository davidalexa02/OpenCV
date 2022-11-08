# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:12:03 2022

@author: acamacho

Ejemplo de utilizaciĂłn de momentos 
"""
import numpy as np
import cv2 as cv

RED = (0,0,255)
# se lee un video se un sitio web
cap = cv.VideoCapture('pelotaroja.mp4')

#se adelanta el video 3 segundos
cap.set(cv.CAP_PROP_POS_MSEC,3000)
#cap.get(cv.CAP_PROP_POS_FRAMES)

#se lee una imagen del video
ret, im = cap.read()

#se cambia el espacio de color y se buscan los pixels de color rojo
hsv = cv.cvtColor(im, cv.COLOR_BGR2HSV)
rojo_inferior = np.array([150,200,95])
rojo_superior = np.array([190,240,115])
# Se localizan los puntos rojos
pelota = cv.inRange(hsv, rojo_inferior, rojo_superior)

#se utilizan los momentos de orden 0 y 1 para calcular las coordenadas x e y del centro de la pelota
m = cv.moments(pelota)
x = m['m10']/m['m00']
y = m['m01']/m['m00']

# se crea una copia de la pelota con una marca en el centro
marcado=im.copy()

cv.circle(marcado, (int(x),int(y)),50,RED,cv.FILLED)
k1 = cv.waitKey(5) & 0xFF
#se muestra la marca parpadeante
while k1!=27:
    cv.imshow('out',im)
    k1=cv.waitKey(1000)     # Esc key to stop
    cv.imshow('out',marcado)
    k1= cv.waitKey(1000)     # Esc key to stop

cap.release()
cv.destroyAllWindows()

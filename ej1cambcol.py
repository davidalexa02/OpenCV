import cv2 as cv
import numpy as np

img1 = cv.imread('monedasazul.jpg')
#redimensionar la imagen en caso de que sea muy grande
imgre=cv.resize(img1,(400,400))
#se busca los pixeles de color azul para eliminar el fondo azul
hsv = cv.cvtColor(imgre, cv.COLOR_BGR2HSV)
lower_blue = np.array([85,50,50])
upper_blue = np.array([130,255,255])
#se localizan los puntos azules
mask = cv.inRange(hsv, lower_blue, upper_blue)
#mask muestra con fondo blanco los pixeles azules detectados
cv.imshow('mask',mask)
#se elimina el fondo azul
res = cv.bitwise_not(mask)
cv.imshow('res',res)
img2_fg = cv.bitwise_and(imgre,imgre,mask = res)
cv.imshow('img2_fg',img2_fg)
#se guardan el numero de filas y columnas con pixeles de la imagen original
rows,cols,channels = imgre.shape

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while(1):
    # Take each frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    roi2 = frame[0:rows, 0:cols]
    cv.imshow('roi2',roi2)
    img1_bg = cv.bitwise_and(roi2,roi2,mask = mask)
    cv.imshow('img1_fg',img1_bg)
    dst = cv.add(img1_bg,img2_fg)
    frame[0:rows, 0:cols ] = dst
    cv.imshow('final',frame)
    #cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
'''
cv.waitKey(0)'''
cv.destroyAllWindows()

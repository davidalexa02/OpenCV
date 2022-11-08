# -*- coding: utf-8 -*-
"""
Created on Sun May  8 18:41:19 2022

@author: CleanPC - Service IT
"""

import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('C:\\Users\\CleanPC - Service IT\\anaconda3\\envs\\database\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
filter=0


cap = cv.VideoCapture(0) #webcame video
# cap = cv.VideoCapture('jj.mp4') #any Video file also
cap.set(cv.CAP_PROP_FPS, 30)



def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image

    # loop over all pixels and apply the blending equation
    # https://www.youtube.com/watch?v=WfdYYNamHZ8 more about the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][1] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src



while (1):
    #mantener pulsada la tecla 0 para hacer desaparecer el filtro
    if cv.waitKey(1) & 0xFF == ord('0'):
        filter=0
    #mantener pulsada la tecla 1 para poner la mascara 1
    if cv.waitKey(1) & 0xFF == ord('1'):
        ojos = cv.imread('sunglasses.png', -1)
        boca = cv.imread('cigarro.png',-1)
        filter=1
    #mantener pulsada la tecla 2 para poner la mascara 2
    if cv.waitKey(1) & 0xFF == ord('2'):
        ojos = cv.imread('sunglasses.png', -1)
        boca = cv.imread('cigarro.png',-1)
        filter=1
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(img, 1.2, 5, 0, (120, 120), (350, 350))
    if filter!=0:
        for (x, y, w, h) in faces:
            if h > 0 and w > 0:
    
                ojos_symin = int(y + 1.5 * h / 5)
                ojos_symax = int(y + 2.5 * h / 5)
                sh_ojos = ojos_symax - ojos_symin
    
                boca_symin = int(y + 4 * h / 6)
                boca_symax = int(y + 5.5 * h / 6)
                sh_boca = boca_symax - boca_symin
    
                face_ojos_roi_color = img[ojos_symin:ojos_symax, x:x+w]
                face_boca_roi_color = img[boca_symin:boca_symax, x:x+w]
    
                ojos = cv.resize(ojos, (w, sh_ojos),interpolation=cv.INTER_CUBIC)
                boca = cv.resize(boca, (w, sh_boca),interpolation=cv.INTER_CUBIC)
                transparentOverlay(face_ojos_roi_color,ojos)
                transparentOverlay(face_boca_roi_color,boca,(int(w/2),int(sh_boca/2)))

    cv.imshow('Fake Snapchat', img)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        cv.imwrite('img.jpg', img)
        break
    
    # Modelo para hacer lo de las teclas:
    # if cv2.waitKey(1) & 0xFF == ord('c'):
    #     break

cap.release()

cv.destroyAllWindows()
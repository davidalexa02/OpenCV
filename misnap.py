# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:32:52 2022

@author: CleanPC - Service IT
"""

import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('C:\\Users\\CleanPC - Service IT\\anaconda3\\envs\\database\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
filter=0

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FPS, 30)

def Capatransparente(src, overlay, pos=(0, 0), scale=1):
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
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
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
        cara = cv.imread('fire.png', -1)
        filter=2
    #mantener pulsada la tecla 3 para poner la mascara 3
    if cv.waitKey(1) & 0xFF == ord('3'):
        cara = cv.imread('mascaraa.png', -1)
        filter=3
    if cv.waitKey(1) & 0xFF == ord('4'):
        cara = cv.imread('chef.png', -1)
        filter=4
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(img, 1.2, 5, 0, (120, 120), (350, 350))
    if filter==1:
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
                Capatransparente(face_ojos_roi_color,ojos)
                Capatransparente(face_boca_roi_color,boca,(int(w/2),int(sh_boca/2)),0.9)
                
    elif filter==2:
        for (x, y, w, h) in faces:
            if h > 0 and w > 0:
    
                face_roi_color = img[y-h:y, x:x+w]
                cara = cv.resize(cara, (w, h),interpolation=cv.INTER_CUBIC)
                Capatransparente(face_roi_color,cara)
                
    elif filter==3:
        for (x, y, w, h) in faces:
            if h > 0 and w > 0:
    
                face_roi_color = img[int(y-(h/1.2)):y+h, int(x-(w/2)):x+w]
                cara = cv.resize(cara, (int(1.9*w), int(2.1*h)),interpolation=cv.INTER_CUBIC)
                Capatransparente(face_roi_color,cara)
    
    elif filter==4:
        for (x, y, w, h) in faces:
            if h > 0 and w > 0:
    
                face_roi_color = img[int(y-h):y, int(x):x+w]
                cara = cv.resize(cara, (int(w), int(h)),interpolation=cv.INTER_CUBIC)
                Capatransparente(face_roi_color,cara)
                
    cv.imshow('Fake Snapchat', img)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        cv.imwrite('img.jpg', img)
        break
    
    

cap.release()

cv.destroyAllWindows()
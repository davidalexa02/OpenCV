import numpy as np
import cv2 as cv
import math
lado=80
# Define colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (0,0,255)
#globals:
fichas=[]
cuadradosnegros=[]
c_or=None
mover=False
ficha=None
    
# functions:

def tablero(cuadradosnegros,fichas):
    img = np.zeros((lado*8,lado*8,3), np.uint8)
    img.fill(255)
    for cuadrado in cuadradosnegros:
        cv.rectangle(img,(cuadrado[0][0],cuadrado[0][1]),(cuadrado[1][0],cuadrado[1][1]),BLACK,cv.FILLED)
    for f in fichas:
        cv.circle(img,(f[0],f[1]),40,RED,cv.FILLED)
    cv.imshow('image',img)
    
    
def mousework(event,x,y,flags,param):
    global fichas,cuadradosnegros,cuadrado,mover,ficha
    if((event == cv.EVENT_LBUTTONDOWN) and (mover==False)):
        for k,cua in enumerate(cuadradosnegros):
            if(cua[0][0]<x<cua[1][0] and cua[0][1]<y<cua[1][1] and cua[2]!=None):
                c_or=k
                ficha=cua[2]
                mover=True
    elif ((event == cv.EVENT_MOUSEMOVE) and (mover==True)):
        fichas[ficha]=[x,y]
        tablero(cuadradosnegros,fichas)
    elif ((event == cv.EVENT_LBUTTONUP) and (mover==True)):
        mover=False
        o=0
        for k,cua in enumerate(cuadradosnegros):
            if(cua[0][0]<x<cua[1][0] and cua[0][1]<y<cua[1][1] and cua[2]==None):
                cua[2]=ficha
                fichas[ficha]=[cua[0][0] +40,cua[0][1]+40]
                cua[c_or][2]=None
                o=1
                break
        if o==0:
            fichas[ficha]=[cua[c_or][0][0]+40,cua[c_or][0][1]+40]
        ficha=None
        
# posiciones cuadrados negros

for i in range(0,8):
   for j in range(0,8):
      t=i+j
      if t % 2!=0:
        cuadradosnegros.append([[i*lado,j*lado],[(i+1)*lado,(j+1)*lado],None])
        
# posiciones fichas

for i in range(0,8):
   for j in range(0,2):
      t=i+j
      if t % 2!=0:
        fichas.append([(i+1)*lado-40,(j+1)*lado-40])

cv.namedWindow('image')
cv.setMouseCallback('image',mousework)

while True:
    tablero(cuadradosnegros,fichas)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()

#------------------------------




#TEORIA ACERCA DE LAS DOS PARTES:

# Variante que pense yo:
    
# lado = 70
# i son lineas
# j son columnas
# si i es numero par entonces se haran con los primeros dos puntos p0 y p1
# si i es numero impar entonces se haran con los otros puntos p2 y p3
# para linea par : la posicion x empezara desde 0 y sumarse con 140 cada vez que pasa
#   a una nueva columna ,la posicion y tiene su valor incrementado con 140 cada vez 
#   que se pasa a una nueva linea
# para linea impar: lo mismo que para las linea pares pero se utilizan los otros puntos
# 
# for y for...
# if 

#math floor es para poner dama en su sitio


#Variante profesor

# lado = 50 pixels o cm
# for j=1:8
#    for i=1:8
#        posicionx = i*50 
#        posiciony = j*50
#        cuadrado(posicionx,posiciony)
#
#        pintar=not(pintar)
#        if pintar
#            rectangle



#las posiciones originales de las fichas se registran en una matriz
#cuando se haya actualizado la posicion de una ficha se actualiza el elemento (las coordenadas originales) de la matriz
#cuando se pulsa con el boton izquierdo del raton sobre el circulo se mueve
#tiene que verse si el cursor esta dentro del circulo
#despues, al hacer clic derecho sobre una casilla negra, debera soltarse la ficha ahi
#si se hace click derecho sobre una casilla blanca se devuelve la ficha donde estaba
#las casillas blancas estan dibujadas sobre un fondo negro
#se redibuja despues de cada evento
#los circulos estan posicionados sobre el tablero, no los cuadrados
#el cursor debe arrastrar hasta los huecos negros, entre los cuadrados blancos
#matriz de las posiciones de los huecos negros
#matriz de las posiciones de las fichas
#elemento extraido de matriz fichas
#elemento extraido de matriz cuadrados
#comprobar si se mueve
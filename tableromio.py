import numpy as np
import cv2 as cv
import math

lado=80
# Define colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (0,0,255)

tableros=[]
fichas=[]
mover = False
ficha = 0

def mousework(event,x,y,flags,param):
    global fichas,mover,ficha,ix,iy
    if((event == cv.EVENT_LBUTTONDOWN) and (mover==False)):
        for k,f in enumerate(fichas):
            x0=f[0]
            y0=f[1]
            posx1=x0-40
            posx2=x0+40
            posy1=y0-40
            posy2=y0+40
            if(x>=posx1 and x<=posx2 and y>=posy1 and y<=posy2):
                ficha=k
                fichas[ficha]=(x,y)
                ix=x0
                iy=y0
                mover=True
    elif ((event == cv.EVENT_MOUSEMOVE) and (mover==True)):
        fichas[ficha]=(x,y)
        tablero(tableros,fichas)
    elif ((event == cv.EVENT_LBUTTONUP) and (mover==True)):
        mover=False
        o=0
        
        for k,f in enumerate(fichas):
            x0=f[0]
            y0=f[1]
            if(k!=ficha):
                if(x>=x0-40 and x<=x0+40 and y>=y0-40 and y<=y0+40):
                    fichas[ficha]=(ix,iy)
                    o=1
                    break
                
        for cuadradonegro in tableros:
            x1=cuadradonegro[0]
            y1=cuadradonegro[1]
            x2=cuadradonegro[2]
            y2=cuadradonegro[3]
            if(x<=x1 and x>=x2 and y<=y1 and y>=y2):
                fichas[ficha] = (ix,iy)
                o=1
                break
        
        if o==0:
            nx=lado*math.floor(x/lado) + 40
            ny=lado*math.floor(y/lado) + 40
            fichas[ficha]=(nx,ny)
            
def tablero(tableros,fichas):
    img = np.zeros((lado*8,lado*8,3), np.uint8)
    img.fill(255)
    for cuadradosnegros in tableros:
        cv.rectangle(img,(cuadradosnegros[0],cuadradosnegros[1]),(cuadradosnegros[2],cuadradosnegros[3]),BLACK,cv.FILLED)
    for f in fichas:
        cv.circle(img,(f[0],f[1]),40,RED,cv.FILLED)
    cv.imshow('image',img)

#Posiciones cuadrados negros en el tablero:
for i in range(0,8):
   for j in range(0,8):
      t=i+j
      if t % 2!=0:
        x1=i*lado
        y1=j*lado
        x2=(i+1)*lado
        y2=(j+1)*lado
        tableros.append([x1,y1,x2,y2])
      

            
#Posiciones fichas en el tablero:
for i in range(0,8):
   for j in range(0,2):
      t=i+j
      if t % 2!=0:
          x0=(i+1)*lado-40
          y0=(j+1)*lado-40
          fichas.append([x0,y0])
      
cv.namedWindow('image')
cv.setMouseCallback('image',mousework)

while True:
    tablero(tableros,fichas)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()



#cv.rectangle(img,(i*lado,j*lado),((i+1)*lado,(j+1)*lado),BLACK,cv.FILLED)
#cv.circle(img,((i+1)*lado-40,(j+1)*lado-40),40,RED,cv.FILLED)

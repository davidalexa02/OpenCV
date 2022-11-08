import numpy as np
import cv2 as cv
# Create a black image
lado=80
img = np.zeros((lado*8,lado*8,3), np.uint8)
img.fill(255)
# Define colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Draw a white filled rectangle

for i in range(0,8):
   for j in range(0,8):
      t=i+j
      if t % 2!=0:
        cv.rectangle(img,(i*lado,j*lado),((i+1)*lado,(j+1)*lado),BLACK,cv.FILLED)
            

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
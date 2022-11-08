import numpy as np
import cv2 as cv

img = cv.imread('imagenes/messi5.jpg')
#img.itemset((10,10,2),100)
#print(img.item(10,10,2))
#print( img.shape )
#print( img.size )
#print( img.dtype )
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
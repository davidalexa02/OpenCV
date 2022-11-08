import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('hojab.jpg',0)
#blur = cv.GaussianBlur(img,(5,5),0)
#ret3,th3 = cv.threshold(blur,255,255,cv.THRESH_OTSU)

ret2,th2 = cv.threshold(img,110,255,cv.THRESH_BINARY)
thre=cv.resize(th2, (800,700))
cv.imshow('reg',thre)
#plt.imshow(thre )
cv.waitKey(0)
cv.destroyAllWindows()

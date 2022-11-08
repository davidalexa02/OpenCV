import argparse
import cv2
import numpy as np

drawing = False # true if mouse is pressed
ix,iy = -1,-1
refPt = []
img = ""
clone = ""
ROIRegion = []

# mouse callback function
def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,img,clone,refPt, ROIRegion
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        refPt = [(x, y)]
        ROIRegion.append(refPt)
        #clone = img.copy()

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = clone.copy()
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),3)
            a=x
            b=y
            if a != x | b != y:
                cv2.rectangle(img,(ix,iy),(x,y),(0,0,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        refPt.append((x,y))
        img = clone.copy()
        cv2.rectangle(img, (ix,iy),(x,y), (0, 255, 0), 2)


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])
img = np.array(img)
clone = img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rectangle)
while(1):
    cv2.imshow('image',img)

    k = cv2.waitKey(1) & 0xFF
    if k == ord("r"):
        del ROIRegion[-1]
        del refPt[-1]
        img = clone.copy()

    elif k == 27:
        break

#Crop image to ROI
for region in range(len(ROIRegion)):
    cv2.rectangle(img, ROIRegion[region][0],ROIRegion[region][1], (0, 255, 0), 2)
    roi = clone[ROIRegion[region][0][1]:ROIRegion[region][1][1], ROIRegion[region][0][0]:ROIRegion[region][1][0]]
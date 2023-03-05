import cv2 as cv 
import sys
import numpy as np
blank = np.zeros([500,500,3],dtype=np.uint8)
# we are giving 3 to have three color channels 
img=cv.imread("images/blue_lock.jpg")
img = cv.resize(img,(200,600))
# blank[200:300,300:400] = 0,0,255
# cv.imshow('blank',blank)
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
# filling the rectangle
# ? (width,hight)
# cv.circle(blank,(250,250),50,(255,255),thickness=cv.FILLED)
# cv.imshow('img',img)
cv.imshow('rectangle',blank)
if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()

import cv2 as cv 
import numpy as np
import os

os.chdir('/home/whoami/Documents/opencv/images')
# creating a empty image

img = cv.imread('cats.jpg')
img = cv.resize(img,(400,400),interpolation=cv.INTER_LINEAR)

blank = np.zeros(img.shape,dtype='uint8')
# cv.imshow('blank',blank)
cv.imshow('cats',img)
# grayscale it 
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# bluring the image

# blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)
canny = cv.Canny(img,125,175)
cv.imshow('canny',canny)

# we can also use thresholding

# ret,thres = cv.threshold(img,125,255,cv.THRESH_TOZERO)

# cv.imshow('thresh',thres)
# cv.imshow('cats',img)

counters,heirachies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank,counters,-1,(255,255,255),1)
cv.imshow('blue_countors',blank)
# print(counters)
print(f'{len(counters)} found')
# cv.imshow('counters',counters)
if cv.waitKey(0)==ord('q'):
    cv.destroyAllWindows()
    

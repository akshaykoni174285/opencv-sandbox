# by akshay with love 
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


pothole = cv.imread('images/pothole_3.png')
# resizing the image 

pothole = cv.resize(pothole,(500,500),interpolation=cv.INTER_LINEAR)
# converting the image in gray
pothole_gray = cv.cvtColor(pothole, cv.COLOR_BGR2GRAY)

cv.imshow('gray',pothole_gray)

blur = cv.blur(pothole_gray,(3,3))
g_blur = cv.GaussianBlur(pothole,(3,3),0)
median = cv.medianBlur(pothole,5)

cv.imshow('blur',g_blur)

kernel = np.ones((3,3),np.uint8)

erosion = cv.erode(median,kernel,iterations = 1)
dilation = cv.dilate(erosion,kernel,iterations = 3)
cv.imshow('dialation',dilation)
closing = cv.morphologyEx(dilation, cv.MORPH_CLOSE, kernel)
edges = cv.Canny(closing,127,360)
cv.imshow('edges',edges)



ret,threshold=cv.threshold(edges.copy(),0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
contours,_=cv.findContours(threshold,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

cv.drawContours(pothole,contours,-1,(0,0,255),2)
cv.imshow("Show",pothole)





if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()

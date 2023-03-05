import cv2 as cv
import sys
import os as os
os.chdir("/home/whoami/Documents/opencv/images")
# converting the bgr to gray
# def cntToGray(frame):
#     return cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

# img = cv.imread('images/blue_cat.jpg')
img = cv.imread("blue_lock.jpg")
img = cv.resize(img, (200,600),interpolation=cv.INTER_LINEAR)
# cv.imshow("color",img)
# img = cntToGray(img)
# cv.imshow("egoist isagi",img)

# how to blur the image
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)
# cv.imshow("orignal",img)

# edge cascading
canny = cv.Canny(blur,125,175)
cv.imshow("edge cascading",canny)

# dilating the image
dialated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilated',dialated)

# you can erode the imge just like dilate




if cv.waitKey(0)==ord('q'):
    cv.destroyAllWindows()

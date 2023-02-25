# import cv2 as cv 
# import matplotlib.pyplot as plt
# import numpy as np
# import sys
# width = 500
# height = 300
# img = cv.imread('images/pothole_3.png')
# img = cv.resize(img, (width, height))
# img_color = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow("rgb",img_color)
# # bluring the image
# blur_img = cv.GaussianBlur(img,[3,3],cv.BORDER_DEFAULT)
# cv.imshow("blur",blur_img)
# cv.imshow("blur",blur_img)
# applying the edge cascading
# canny_img = cv.Canny(blur_img,100,200)
# cv.imshow("blur",blur_img)
# cv.imshow('pothole',img)
# cv.imshow('pothole_outline',canny_img)
# _,th1=cv.threshold(blur_img,100,255,1)

# cv.imshow('thresholding',th1)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


pothole = cv.imread('images/pothole_3.png')
pothole = cv.cvtColor(pothole, cv.COLOR_BGR2RGB)

hsv_pothole = cv.cvtColor(pothole, cv.COLOR_RGB2HSV)

# pothole_blur = cv.GaussianBlur(pothole,[3,3],cv.BORDER_DEFAULT)

grey_dark = (114,17,41)
grey_light = (108,31,66)

mask = cv.inRange(hsv_pothole,grey_light,grey_dark)
result = cv.bitwise_and(pothole,pothole,mask=mask)

# plt.subplot(1,2,1)
# plt.imshow(mask,cmap="gray")
# plt.subplot(1,2,2)
# plt.imshow(result)
# plt.show()
cv.imshow('mask',mask)




if cv.waitKey(0)==ord('q'):
    cv.destroyAllWindows()
    

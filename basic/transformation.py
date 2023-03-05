import cv2 as cv 
import numpy as np 
import os 
os.chdir("/home/whoami/Documents/opencv/images")
img = cv.imread("blue_cat.jpg")
# img = cv.resize(img,(1000,1000),interpolation=cv.INTER_AREA)
# cv.imshow('isag',img)

# translation of image

# def translate(img,x,y):
#     transMat = np.float32([[1,0,x],
#                            [0,1,y]
#                         ]
#                     )
#     dimension = (img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMat,dimension)

# translate = translate(img,-200,-200)
# cv.imshow('isagi',translate)


# rotation 
# def rotate(img,angle,rpoint=None):
#     (height,width) = img.shape[:2]
    
#     if rpoint==None:
#         rpoint = (width//2,height//2)
    
#     rotMat = cv.getRotationMatrix2D(rpoint,angle,1.0)
#     dimensions = (width,height)
#     return cv.warpAffine(img,rotMat,dimensions)

# rotate_img = rotate(img,45)
# cv.imshow('rotate',rotate_img)

if cv.waitKey(0)==ord('q'):
    cv.destroyAllWindows()
    
  
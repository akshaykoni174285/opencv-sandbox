# how to red a image
# import cv2 as cv
# import sys

# img = cv.imread("images/blue_cat.jpg")
# img_resize = cv.resize(img,(255,255))
# cv.imshow('cat',img_resize)
# cv.waitKey(0)
# cv.destroyAllWindows()


# how would you read the videos 

# capture = cv.VideoCapture("videos/sample.mp3")
# while capture.isOpened():
#     isTrue,frame = capture.read()
#     if isTrue==False:
#         print("not able to open the video ")
#     cv.imshow('cartoon',frame)
#     if cv.waitKey(20) == ord('q'):
#         break
    
# capture.release()
# cv.destroyAllWindows()

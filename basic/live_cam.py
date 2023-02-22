import cv2 as cv
import sys


capture = cv.VideoCapture(0)
while capture.isOpened():
    
    ret,frame = capture.read()
    frame = cv.flip(frame,1)
    capture.set(3,400)
    capture.set(3,1000)
    cv.imshow("cam",frame)
    if cv.waitKey(1)==ord('q'):
        break


capture.release()
cv.destroyAllWindows()
import cv2 as cv
import sys

# img = cv.imread('images/blue_cat.jpg')
def rescaleWindow(frame,scale=0.75):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimensions = (height,width)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
# image_resize = rescaleWindow(img)
# cv.imshow('cat',image_resize)
# cv.waitKey(0)
# cv.destroyAllWindows()


# resizing the video window
capture = cv.VideoCapture('videos/sample.mp4')
# now to capture the video from the webcam you will use int 0 and you can also provide a path to the video 
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        print("cant recieve the frame for the video")
    resized_frame = cv.resize(frame,(700,500))
    # gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("frame",frame)
    cv.imshow("resized_frame",resized_frame)
    if cv.waitKey(20) == ord('q'):
    # we are gonna wait 20 seconds or if the letter q is pressed we are gonna close the player
        break

# cv.waitKey(0)
capture.release()
# release the video pointer
cv.destroyAllWindows()
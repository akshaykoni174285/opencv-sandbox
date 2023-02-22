import cv2 as cv 
import sys 

# img = cv.imread('images/blue_lock.jpg')

# if img is None:
#     print("check the file of the image")
# cv.namedWindow("main",cv.WINDOW_NORMAL)
# cv.resizeWindow("resized window",300,700)
# cv.imshow("Display window",img)



#  how to read a videos using opencv 
capture = cv.VideoCapture('videos/sample.mp4')
# now to capture the video from the webcam you will use int 0 and you can also provide a path to the video 
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        print("cant recieve the frame for the video")
    # gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("frame",frame)
    if cv.waitKey(20) == ord('q'):
    # we are gonna wait 20 seconds or if the letter q is pressed we are gonna close the player
        break

# cv.waitKey(0)
capture.release()
# release the video pointer
cv.destroyAllWindows()



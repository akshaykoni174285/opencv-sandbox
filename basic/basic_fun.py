import cv2 as cv
import sys
# converting the bgr to gray
def cntToGray(frame):
    return cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

img = cv.imread('images/blue_cat.jpg')
img = cv.resize(img, (200,600),interpolation=cv.INTER_LINEAR)
# cv.imshow("color",img)
# img = cntToGray(img)
# cv.imshow("egoist isagi",img)

# how to blur the image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)
cv.imshow("orignal",img)

# edge cascading
canny = cv.Canny(blur,125,175)
cv.imshow("edge cascading",canny)


if cv.waitKey(0)==ord('q'):
    cv.destroyAllWindows()

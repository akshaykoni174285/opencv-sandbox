import cv2
import numpy as np

def empty():
   pass


while True:

   img = cv2.imread("images/pothole_3.png")
   imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
   h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
   s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
   s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
   v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
   v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
   lower = np.array([h_min, s_min, v_min])
   upper = np.array([h_max, s_max, v_max])
   mask = cv2.inRange(imgHSV, lower, upper)
   imgResult = cv2.bitwise_and(img, img, mask=mask)


   contours, _ = cv2.findContours(mask, cv2.RETR_TREE, 
   cv2.CHAIN_APPROX_NONE) 

   for contour in contours:
         cv2.drawContours(img, contour, -1, (0, 255, 0), 3)

   cv2.imshow("Original", img)
   cv2.imshow("Result", imgResult)

   if cv2.waitKey(27) & 0xFF == ord('q'):
       print(h_min, h_max, s_min, s_max, v_min, v_max)
       break
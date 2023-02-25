import cv2
import numpy as np

# Load the image
img = cv2.imread('images/potholes_1.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to smooth the image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection to find edges in the image
# edges = cv2.Canny(blurred, 50, 150)

# Apply Hough transform to find circles in the image
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Draw circles on the original image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)

# Display the image with detected circles
cv2.imshow('Pothole Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

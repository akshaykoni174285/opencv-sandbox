from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2 


pothole = cv2.imread('images/pothole_3.png')
pothole = cv2.cvtColor(pothole, cv2.COLOR_BGR2RGB)
plt.imshow(pothole)
plt.show()
r, g, b = cv2.split(pothole)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")
pixel_colors = pothole.reshape((np.shape(pothole)[0]*np.shape(pothole)[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()
axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
hsv_pothole = cv2.cvtColor(pothole,cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv_pothole)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")
axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Hue")
axis.set_ylabel("Saturation")
axis.set_zlabel("Value")
plt.show()
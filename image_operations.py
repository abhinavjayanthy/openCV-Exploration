import numpy as np
import cv2

img = cv2.imread('Phone.JPG', cv2.IMREAD_COLOR)

img[55, 55] == [255, 255, 255]  # changing the color of the image
px = img[55, 55]
print(px)

# ROI is region of image
roi = img[100:150, 100:150]
print(roi)  # The result is a numpy array

# having a white square in the image region
img[100:150, 100:150] = [255, 255, 255]
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

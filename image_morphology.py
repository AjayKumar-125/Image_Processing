
import numpy as np
import cv2





image = cv2.imread('C:Data\\j.png', cv2.IMREAD_GRAYSCALE)

# Define a structuring element
kernel = np.ones((5, 5), np.uint8)

# Perform erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Perform dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Perform opening (erosion followed by dilation)
opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Perform closing (dilation followed by erosion)
closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display results
cv2.imshow('Original', image)
cv2.imshow('Eroded', eroded)
cv2.imshow('Dilated', dilated)
cv2.imshow('Opened', opened)
cv2.imshow('Closed', closed)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# Load two images
img1 = cv2.imread("C:Data\\animal.jpg")
img2 = cv2.imread("C:Data\\bird.png")

# Resize images if necessary
img1 = cv2.resize(img1, (1024, 650))
img2 = cv2.resize(img2, (400, 400))

# Get the shape of img2
r, c, ch = img2.shape
print(r, c, ch)

# Define the region of interest (ROI) in img1
roi = img1[0:r, 0:c]

# Now create a mask of img2 and its inverse mask
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Black-out the area of img2 in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of img2 from img2
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Put img2 in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:r, 0:c] = dst

# Display the result
cv2.imshow("animal", img1)
cv2.imshow("bird", img2)
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

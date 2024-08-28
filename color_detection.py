import cv2
import numpy as np

def nothing(x):
    pass

# Create a window
cv2.namedWindow('Trackbars')

# Create trackbars for color change
cv2.createTrackbar('LH', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('LS', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('LV', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('UH', 'Trackbars', 179, 179, nothing)
cv2.createTrackbar('US', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('UV', 'Trackbars', 255, 255, nothing)

# Load the image
img_path = "C:Data\\balls.jpg"
img = cv2.imread(img_path)
img=cv2.resize(img,(400,400))

while True:
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Get current positions of the trackbars
    lh = cv2.getTrackbarPos('LH', 'Trackbars')
    ls = cv2.getTrackbarPos('LS', 'Trackbars')
    lv = cv2.getTrackbarPos('LV', 'Trackbars')
    uh = cv2.getTrackbarPos('UH', 'Trackbars')
    us = cv2.getTrackbarPos('US', 'Trackbars')
    uv = cv2.getTrackbarPos('UV', 'Trackbars')
    
    # Define the lower and upper HSV range for the color
    lower_blue = np.array([lh, ls, lv])
    upper_blue = np.array([uh, us, uv])
    
    # Create a mask with the specified HSV range
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask=mask)
    
    # Display the result
    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    
    # Break the loop when 'q' is pressed
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()

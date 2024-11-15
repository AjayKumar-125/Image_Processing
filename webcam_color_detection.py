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

# Initialize webcam capture
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam, or change to another index if you have multiple cameras

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Resize frame for display
    frame = cv2.resize(frame, (400, 400))
    
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
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
    
    # Bitwise-AND mask and original frame
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Display the frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', res)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()

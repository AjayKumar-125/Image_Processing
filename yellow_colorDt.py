import cv2
import numpy as np

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
    
    # Define the range of yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # Create a mask with the specified HSV range for yellow
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
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

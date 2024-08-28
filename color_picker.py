import numpy as np
import cv2

# Function to handle trackbar changes (dummy function)
def nothing(x):
    pass

# Create a blank image
image = np.zeros((300, 500, 3), dtype=np.uint8)
cv2.namedWindow('Color Picker')  # Create a named window

# Create trackbars for RGB
cv2.createTrackbar('B', 'Color Picker', 0, 255, nothing)
cv2.createTrackbar('G', 'Color Picker', 0, 255, nothing)
cv2.createTrackbar('R', 'Color Picker', 0, 255, nothing)

# Create a switch (checkbox) for RGB/BGR mode
switch = 'BGR/RGB'
cv2.createTrackbar(switch, 'Color Picker', 0, 1, nothing)

while True:
    # Get current positions of trackbars
    b = cv2.getTrackbarPos('B', 'Color Picker')
    g = cv2.getTrackbarPos('G', 'Color Picker')
    r = cv2.getTrackbarPos('R', 'Color Picker')
    s = cv2.getTrackbarPos(switch, 'Color Picker')

    # Set the color mode based on the switch
    if s == 0:
        color = (b, g, r)  # BGR mode
    else:
        color = (r, g, b)  # RGB mode

    # Fill the image with the selected color
    image[:] = color

    # Display the image
    cv2.imshow('Color Picker', image)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

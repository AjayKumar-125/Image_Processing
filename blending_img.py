import cv2
import numpy as np

def nothing(x):
    pass

# Load the images
image1 = cv2.imread('C:Data\\animal.jpg')
image1=cv2.resize(image1,(400,400))
image2 = cv2.imread('C:Data\\bird.png')
image2=cv2.resize(image2,(400,400))

# Ensure the images are of the same size
if image1.shape != image2.shape:
    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Create a window
cv2.namedWindow('Blended Image')

# Create trackbars for alpha
cv2.createTrackbar('Alpha', 'Blended Image', 0, 100, nothing)

while True:
    # Get the current positions of the trackbars
    alpha = cv2.getTrackbarPos('Alpha', 'Blended Image') / 100

    # Compute beta
    beta = 1.0 - alpha

    # Blend the images
    blended_image = cv2.addWeighted(image1, alpha, image2, beta, 0)

    # Display the blended image
    cv2.imshow('Blended Image', blended_image)

    # Wait for the ESC key to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Destroy all the windows
cv2.destroyAllWindows()

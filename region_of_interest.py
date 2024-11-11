import cv2
img_path="C:Data\\my_image.jpg"
# Load an image
image = cv2.imread(img_path)
image=cv2.resize(image,(800,1080))

# Display the image and allow the user to select the ROI
roi = cv2.selectROI('Select ROI', image, fromCenter=False, showCrosshair=True)

# Crop the selected ROI from the image
x, y, w, h = roi
cropped_image = image[int(y):int(y+h), int(x):int(x+w)]

# Display the cropped ROI
cv2.imshow('Cropped ROI', cropped_image)
cv2.waitKey(0)

# Save the cropped ROI
cv2.imwrite('cropped_image.jpg', cropped_image)

# Clean up and close windows
cv2.destroyAllWindows()

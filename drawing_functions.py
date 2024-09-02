import cv2
import numpy as np
img_path="C:Data\\animal.jpg"
#img=cv2.imread(img_path)
#img=cv2.resize(img,(400,400))

img = np.ones((500, 500, 3), dtype=np.uint8) * 255
# Define the start and end points of the line
start_point = (0, 0)
end_point = (150, 150)

# Define the color (BGR format) and thickness of the line
color = (255, 0, 0)  # Blue color
thickness = 2

# Draw the line on the image
image_with_line = cv2.line(img, start_point, end_point, color, thickness)

# Display the image
cv2.imshow('Image with Line', image_with_line)

# Draw the arrowed line on the image
image_with_arrow = cv2.arrowedLine(img, start_point, end_point, color, thickness)

# Display the image
cv2.imshow('Image with Arrowed Line', image_with_arrow)

# Define the top-left and bottom-right corners of the rectangle
top_left_corner = (50, 50)
bottom_right_corner = (200, 200)

# Define the color (BGR format) and thickness of the rectangle
color = (0, 255, 0)  # Green color
thickness = 2  # Thickness of 2 pixels

# Draw the rectangle on the image
image_with_rectangle = cv2.rectangle(img, top_left_corner, bottom_right_corner, color, thickness)

# Display the image
cv2.imshow('Image with Rectangle', image_with_rectangle)
# Define the center and radius of the circle
center_coordinates = (150, 150)
radius = 50

# Define the color (BGR format) and thickness of the circle
color = (0, 0, 255)  # Green color
thickness = 2  # Thickness of 2 pixels

# Draw the circle on the image
image_with_circle = cv2.circle(img, center_coordinates, radius, color, thickness)

# Display the image
cv2.imshow('Image with Circle', image_with_circle)

# Define the text to be added
text = "Hello, OpenCV!"

# Define the position for the text
position = (50, 50)

# Define the font, scale, color, and thickness of the text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0,0,255)  # Green color
thickness = 2

# Add the text to the image
image_with_text = cv2.putText(img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

# Display the image
cv2.imshow('Image with Text', image_with_text)



# Define the center of the ellipse
center_coordinates = (150, 150)

# Define the axes lengths (major axis and minor axis)
axes_length = (100, 50)

# Define the angle of rotation of the ellipse
angle = 30

# Define the start and end angle of the arc (0 to 360 to draw a full ellipse)
start_angle = 0
end_angle = 360

# Define the color (BGR format) and thickness of the ellipse
color = (0, 255, 0)  # Green color
thickness = 2  # Thickness of 2 pixels

# Draw the ellipse on the image
image_with_ellipse = cv2.ellipse(img, center_coordinates, axes_length, angle, start_angle, end_angle, color, thickness)

# Display the image
cv2.imshow('Image with Ellipse', image_with_ellipse)



cv2.waitKey(0)
cv2.destroyAllWindows()
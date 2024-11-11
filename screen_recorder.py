import cv2
import numpy as np
import pyautogui as p

# Get screen resolution
rs = p.size()

# Prompt user for file name and path
file_name = input("Please enter a filename and path: ")

# Frame rate
fps = 20.0

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(file_name, fourcc, fps, (rs.width, rs.height))

# Create a window for live recording
cv2.namedWindow("Live_Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Recording", (600, 400))

while True:
    # Take a screenshot using pyautogui
    img = p.screenshot()
    
    # Convert the screenshot to a numpy array
    f = np.array(img)
    
    # Convert colors from BGR to RGB
    frame = cv2.cvtColor(f, cv2.COLOR_RGB2BGR)
    
    # Display the recording
    cv2.imshow("Live_Recording", frame)
    
    # Write the frame to the output file
    output.write(frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoWriter and close all windows
output.release()
cv2.destroyAllWindows()

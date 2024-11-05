import cv2

# Initialize the webcam
webcam = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# You can use 'XVID' or 'MJPG' depending on the codec you prefer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = webcam.read()
    if ret:
        # Write the frame to the video file
        out.write(frame)
        
        # Display the frame
        cv2.imshow('frame', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the webcam and file resources
webcam.release()
out.release()
cv2.destroyAllWindows()

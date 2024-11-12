import cv2
import os

# Read video
video_path = os.path.join('.', 'Data', 'video.mp4')
videoCap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not videoCap.isOpened():
    print("Error: Could not open video.")
    exit()

count = 0
frame_interval = 1000  # in milliseconds

while True:
    ret, frame = videoCap.read()
    if not ret:
        break

    # Save frame as image
    frame_path = os.path.join('C:\\Frames', f'imgN{count}.jpg')
    cv2.imwrite(frame_path, frame)

    # Set the position of the next frame to be captured
    videoCap.set(cv2.CAP_PROP_POS_MSEC, (count * frame_interval))

    # Show the frame
    cv2.imshow("Result", frame)

    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
videoCap.release()
cv2.destroyAllWindows()

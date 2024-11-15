import cv2 
import datetime
import os

video_path=os.path.join('.','Data','video.mp4')
videoCap=cv2.VideoCapture(video_path)

# Get video properties
width = int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the text to be added
date_data=str(datetime.datetime.now())
position = (50, 50)  # Bottom-left corner of the text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 255, 0)  # Green color
thickness = 2





    
while True:
    ret,frame=videoCap.read()
    # Add the text to the current frame
    
    cv2.putText(frame, f"Width :{width}  Height : {height}  Date : {date_data}", position, font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.rectangle(frame,(50,50),(200,200),(0,255,0),4)
    cv2.imshow("Result ",frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
videoCap.release()
cv2.destroyAllWindows()    
            

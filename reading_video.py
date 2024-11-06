import cv2
import os
#read video
video_path=os.path.join('.','Data','video.mp4')
video=cv2.VideoCapture(video_path)


while True:
    ret,frame=video.read()
    frame=cv2.resize(frame,(700,450))
    # convert frame color from BGR2GRAY
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame ",gray)
    k=cv2.waitKey(40)
    if k==ord('q'):
        break
       
video.release()
cv2.destroyAllWindows()        


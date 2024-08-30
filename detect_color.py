import cv2
import numpy as np

img_path = "C:Data\\balls.jpg"
img = cv2.imread(img_path)
img=cv2.resize(img,(400,400))

while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define the range for blue color in HSV
    lower_blue = np.array([83, 38, 120])
    upper_blue = np.array([144, 255, 255])
    
    #lower_yellow = np.array([20, 100, 100])
    #upper_yellow = np.array([30, 255, 255])

    # mask that captures all pixels within the blue range
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask=mask)
    
    # Display the images
    cv2.imshow("Image",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result ",res)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()

import cv2
img_path="C:Data\\bird.png"
img=cv2.imread(img_path)
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('original',img)
#cv2.imshow("img_rgb",img_rgb)
#cv2.imshow("img_gray",img_gray)
cv2.imshow("img_hsv",img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
img_path="C:Data\\noisy_img.png"
img=cv2.imread(img_path)
img=cv2.resize(img,(400,400))
cv2.imshow("original_img",img)
size=11
blur_img=cv2.blur(img,(size,size))
GausianBlur_img=cv2.GaussianBlur(img,(size,size),3)
Medianblur_img=cv2.medianBlur(img,(size))
cv2.imshow("blur_img",blur_img)
cv2.imshow("GausianBlur_img",GausianBlur_img)
cv2.imshow("Medianblur_img",Medianblur_img)

cv2.waitKey(0)

cv2.destroyAllWindows()
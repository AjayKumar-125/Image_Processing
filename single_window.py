import cv2
import numpy as np
img_path="C:Data\\noisy_image.png"
img=cv2.imread(img_path)
img=cv2.resize(img,(400,400))

size=17
blur_img=cv2.blur(img,(size,size))
GausianBlur_img=cv2.GaussianBlur(img,(size,size),3)
Medianblur_img=cv2.medianBlur(img,(size))

# Add text to each image
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)

cv2.putText(img, 'Original', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(blur_img, 'Blur', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(GausianBlur_img, 'Gaussian Blur', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(Medianblur_img, 'Median Blur', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)


img1=cv2.hconcat([img,blur_img])
img2=cv2.hconcat([GausianBlur_img,Medianblur_img])
result=cv2.vconcat([img1,img2])
cv2.imshow("origianl image and all blur images in a Single window",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
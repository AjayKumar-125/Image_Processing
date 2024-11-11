import cv2

#read image
img_path="C:Data\dog.jpg"

img=cv2.imread(img_path)
resized_img=cv2.resize(img,(700,480))
print(img.shape)
cv2.imshow("original_img",img)
print(resized_img.shape)
cv2.imshow("resized_img",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
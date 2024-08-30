import cv2
#read 
img_path="C:Data\\bird.jpg"
img=cv2.imread(img_path)

resized_img=cv2.resize(img,(1920,1080))
print(resized_img.shape)

#Crop image using interval

croped_img=resized_img[150:400,700:1160]
cv2.imshow("resized_img",resized_img)
cv2.imshow("croped_img",croped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
#Read
my_img=cv2.imread("C:Data\my_image.jpg",1)
print(my_img)
cv2.imshow("Original",my_img)

#Conversion from Colored Image into GrayScale Image just making second parameter 0
my_img2=cv2.imread("C:Data\my_image.jpg",0)

print(my_img2)
cv2.imshow("Gray Scale Image",my_img2)
k=cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("C:Data\\output.png",my_img2)
else:
    cv2.destroyAllWindows()    


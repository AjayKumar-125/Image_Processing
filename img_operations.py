
import cv2
img_path="C:Data\\bird.png"
img=cv2.imread(img_path)
img=cv2.resize(img,(600,700))
b,g,r=cv2.split(img)
cv2.imshow("original image ",img)

# cv2.imshow("Blue ",b)
# cv2.imshow("Green",g)
# cv2.imshow("Red ",r)

# m1=cv2.merge((b,g,r))
# cv2.imshow("B,G,R :",m1)
# m2=cv2.merge((r,g,b))
# cv2.imshow("R,G,B :",m2)
# m3=cv2.merge((g,r,b))
# cv2.imshow("G,R,B :",m3)

#accessing a pixel value from by its row and column coordinates
px=img[500,530]
print("The pixels of that coordinate ",px)
#now trying to find selected channel value from coordinates
blue=img[500,530,0]
print("the pixel having blue color ",blue)
green=img[500,530,1]
print("the pixel having green color ",green)
red=img[500,530,2]
print("the pixel having red color ",red)

cv2.waitKey(0)
cv2.destroyAllWindows()
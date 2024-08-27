import cv2
import numpy as np

img1=np.zeros((250,500,3),np.uint8)
img1=cv2.rectangle(img1,(150,100),(200,250),(255,255,255),-1)

img_2=np.zeros((250,500,3),np.uint8)
img_2=cv2.rectangle(img_2,(10,10),(170,190),(255,255,255),-1)

bit_and=cv2.bitwise_and(img1,img_2)
bit_or=cv2.bitwise_or(img1,img_2)
bit_not=cv2.bitwise_not(img1)
bit_xor=cv2.bitwise_xor(img1,img_2)
cv2.imshow("img 1",img1)
cv2.imshow("img 2",img_2)
cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_not",bit_not)
cv2.imshow("bit_xor",bit_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()

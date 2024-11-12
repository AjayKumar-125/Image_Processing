import cv2

img_path="C:Data\\animal.jpg"
img=cv2.imread(img_path,0)

img=cv2.resize(img,(520,420))
_,thresh_binary=cv2.threshold(img,80,255,cv2.THRESH_BINARY)
_,thresh_binary_inv=cv2.threshold(img,80,255,cv2.THRESH_BINARY_INV)
_,thresh_2zero=cv2.threshold(img,80,255,cv2.THRESH_TOZERO)
_,thresh_2zero_inv=cv2.threshold(img,80,255,cv2.THRESH_TOZERO_INV)
_,thresh_trunc=cv2.threshold(img,80,255,cv2.THRESH_TRUNC)

cv2.putText(img, 'Original', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(thresh_binary, 'thresh_binary', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(thresh_binary_inv, 'thresh_binary_inv', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(thresh_2zero, 'thresh_2zero', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(thresh_2zero_inv, 'thresh_2zero_inv', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(thresh_trunc, 'thresh_trunc', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
img1=cv2.hconcat([img,thresh_binary,thresh_binary_inv])
img2=cv2.hconcat([thresh_2zero,thresh_2zero_inv,thresh_trunc])
result=cv2.vconcat([img1,img2])
cv2.imshow("All images in single window",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

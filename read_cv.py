import cv2

image1=cv2.imread('dog.png')
type(image1)
cv2.imshow("Image",image1)

cv2.waitKey(0)
cv2.destroyAllWindows()

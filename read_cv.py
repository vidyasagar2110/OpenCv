import cv2

image1=cv2.imread('cat.jpg')
type(image1)
cv2.imshow("Image",image1)

cv2.waitKey(0)
cv2.destroyAllWindows()

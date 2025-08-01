import cv2
import numpy as np

image = cv2.imread("rider.jpg")  #img = cv2.imread('Cat.jpeg', 0) grey scale 
rows, cols = image.shape[:2]
# Shear matrix (x-shear)
shear_matrix = np.float32([[1, 0.5, 0],
                           [0,   1, 0]])

# Apply affine transform
sheared_image = cv2.warpAffine(image, shear_matrix, (int(cols * 1.5), rows))

h_flip = cv2.flip(image, 1) 
v_flip = cv2.flip(image, 0) 
both_flip = cv2.flip(image, -1) 

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.imshow("Sheared (Skewed)", sheared_image)

cv2.waitKey(0)
cv2.imshow("HFlip", h_flip)
cv2.waitKey(0)
cv2.imshow("VFlip", v_flip)
cv2.waitKey(0)
cv2.imshow("HVFlip", both_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()
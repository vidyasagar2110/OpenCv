
import cv2

img = cv2.imread(r"hero.jpg", 0)  # Read image in grayscale

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Thresholded", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
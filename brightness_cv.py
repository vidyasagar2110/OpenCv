
import cv2
import numpy as np

# Read grayscale image
img = cv2.imread("p.png",0)

# Add 20 to each pixel but cap at 255
img1 = np.clip(img + 20, 0, 255).astype(np.uint8)

# Show original and modified images
cv2.imshow("Original", img)
cv2.imshow("Increased Brightness", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
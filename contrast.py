import cv2
import numpy as np

def contrast_stretch(img):
    a, b = 230, 10  # new range
    rmin, rmax = np.min(img), np.max(img)
    stretched = (img - rmin) * ((b - a) / (rmax - rmin)) + a
    return np.uint8(stretched)

img = cv2.imread("rah.jpg", 0)
cv2.imshow("Original", img)
cv2.waitKey(0)
stretched_img = contrast_stretch(img)

cv2.imshow("Contrast Stretched", stretched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
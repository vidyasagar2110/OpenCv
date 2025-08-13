import numpy as np
import cv2
img = cv2.imread('road.jpg', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv2.Canny(img,100,200)
cv2.imshow("Edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
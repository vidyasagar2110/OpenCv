import cv2
import numpy as np

# Read the image
image = cv2.imread('taj.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a Sobel-like kernel (horizontal edge detection)
k = np.array([[-1, 0, 1],
              [-2, 0, 2],
              [-1, 0, 1]])

# Apply the kernel to the grayscale image
output = cv2.filter2D(src=gray, ddepth=-1, kernel=k)

# Show both images
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Edge Detected Output", output)

# Wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

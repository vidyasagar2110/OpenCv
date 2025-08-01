import cv2

img = cv2.imread("heman.jpg")
if img is None:
    print("Error: messi.jpg not found or cannot be opened.")
    exit()

half = cv2.resize(img, (0, 0), fx = 0.4, fy = 0.4)
bigger = cv2.resize(img, (1050, 1610))

print(img.shape)
print(half.shape)
print(bigger.shape)

cv2.imshow("Image1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Image2", half)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Image3", bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()
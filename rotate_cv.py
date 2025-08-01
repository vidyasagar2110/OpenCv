import cv2

img = cv2.imread("bike.png")  #img = cv2.imread('Cat.jpeg', 0) grey scale


# dividing height and width by 2 to get the center of the image
height, width = img.shape[:2]
# get the center coordinates of the image to create the 2D rotation matrix
center = (width / 2, height / 2)

# using cv2.getRotationMatrix2D() to get the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=0.5)

print(rotate_matrix)

# rotate the image using cv2.warpAffine
rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))

cv2.imshow("Image",img)

print("Image Rotation")

cv2.imshow("RImage",rotated_image)
cv2.waitKey(0)
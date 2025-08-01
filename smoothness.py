import cv2
import numpy as np

image=cv2.imread('taj.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

k=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
# k=k/6

output=cv2.filter2D(src=gray,ddepth=-1,kernel=k)


cv2.imshow("Image",gray)
cv2.imshow("Output",output)
cv2.waitKey(0)
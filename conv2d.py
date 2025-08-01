
import cv2
import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.uint8)
b=np.array([[-1,0,1],[-2,0,2],[-1,0,1]],dtype=np.float32)

print(a)
print(b)
b1=cv2.flip(b,-1)
c=cv2.filter2D(src=a,ddepth=cv2.CV_32F,kernel=b1,borderType=cv2.BORDER_CONSTANT)
print(c)
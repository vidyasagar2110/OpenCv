import matplotlib.pyplot as plt
import matplotlib.image as img

image=img.imread('cat.jpg')

plt.imshow(image[:,:,:])
plt.show()
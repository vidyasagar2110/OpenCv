import matplotlib.pyplot as plt
import matplotlib.image as img

image=img.imread('dog.png')

plt.imshow(image[:,:,:])
plt.show()
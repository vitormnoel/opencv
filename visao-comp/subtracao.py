import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("imagens/cebola1.jpg", 0)
img1 = cv.imread("imagens/batata.jpg", 0)

#print(img.shape)
#print(img1.shape)

fig = plt.figure(figsize=(20,5))

ax1 = fig.add_subplot(121)
plt.imshow(img, cmap=plt.cm.gray)

ax2 = fig.add_subplot(122)
plt.imshow(img1, cmap=plt.cm.gray)
plt.show()

#funcao subtract
sub = cv.subtract(img, img1)
fig = plt.figure(figsize=(20,5))
plt.imshow(sub, cmap=plt.cm.gray)
plt.show()
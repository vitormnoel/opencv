import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("imagens/cafe.jpg")

metodo = cv.THRESH_BINARY_INV
ret, imbin = cv.threshold(img, 200, 255, metodo)

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(221)
plt.imshow(img)
plt.title("original")

ax2 = fig.add_subplot(222)
plt.imshow(imbin)
plt.title('binaria')

plt.show()
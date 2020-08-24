import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("imagens/cebola.jpg")
azul, verde, vermelho = cv.split(img)
plt.imshow(img)
plt.show()

fig = plt.figure(figsize=(20,5))

ax1 = fig.add_subplot(131)
ax1.hist(azul.ravel(), 256, [0,256])
plt.title("Azul")

ax2 = fig.add_subplot(132)
ax2.hist(verde.ravel(), 256, [0, 256])
plt.title("Verde")

ax3 = fig.add_subplot(133)
ax3.hist(vermelho.ravel(), 256, [0, 256])
plt.title("Vermelho")

plt.show()
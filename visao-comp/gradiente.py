import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('imagens/moeda.png')
img2 = cv2.imread('imagens/esqueleto.tif')

fig = plt.figure(figsize=(15,15))

ax1 = fig.add_subplot(221)
plt.imshow(img1)
plt.title("Imagem Original")

ax2 = fig.add_subplot(222)
plt.imshow(img2)
plt.title("Imagem Original")

plt.show()

elem_str1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
elem_str2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21,21))

print(elem_str1)
print(elem_str2)

imgProc1 = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, elem_str1)
imgProc2 = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, elem_str2)
imgProc3 = cv2.morphologyEx(img2, cv2.MORPH_BLACKHAT, elem_str2)

fig = plt.figure(figsize=(15,15))

ax1 = fig.add_subplot(131)
plt.imshow(imgProc1)
plt.title("Gradiete Morfologico")

ax2 = fig.add_subplot(132)
plt.imshow(imgProc2)
plt.title("TOPHAT")

ax3 = fig.add_subplot(133)
plt.imshow(imgProc3)
plt.title("BLACKHAT")

plt.show()
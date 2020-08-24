import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('imagens/cebola1.jpg', 0)
img1 = cv.imread('imagens/cebola2.jpg', 0)

soma = cv.add(img, img1) #funcao add
fig = plt.figure(figsize=(10,5))
plt.imshow(soma, cmap=plt.cm.gray)
plt.show()
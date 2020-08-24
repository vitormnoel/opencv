import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

imOriginal = cv.imread("imagens/eu.jpg", 0)

totalLinhas, totalColunas = imOriginal.shape
print(totalLinhas)
print(totalColunas)

mat = cv.getRotationMatrix2D((totalLinhas/2, totalColunas/2), 90, 1)

imR = cv.warpAffine(imOriginal, mat, (totalColunas, totalLinhas))
fig = plt.figure(figsize=(10, 5))
plt.imshow(imR, cmap=plt.cm.gray)
plt.show()
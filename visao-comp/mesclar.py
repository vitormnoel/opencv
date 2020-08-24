import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("imagens/eu.jpg", 0)
img1 = cv.imread("imagens/eu.jpg", 0)

linhas, colunas = img1.shape
matriz = np.float32([(1, 0, 50),[0, 1, 100]])
deslocada = cv.warpAffine(img1, matriz, (linhas, colunas))

mes = cv.addWeighted(img, 0.1, img1, 0.8, 0)

fig = plt.figure(figsize=(20,5))
plt.imshow(mes, cmap=plt.cm.gray)
plt.show()
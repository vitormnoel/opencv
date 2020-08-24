import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("imagens/einstein.jpg", 0)

plt.hist(img.ravel(), 256, [0, 256])
plt.show()
imgE = cv.equalizeHist(img)

#imagem nitida atravez da equalização
fig = plt.figure(figsize=(20,5))
ax1 = fig.add_subplot(121)
plt.imshow(img, cmap=plt.cm.gray)

ax2 = fig.add_subplot(122)
plt.imshow(imgE, cmap=plt.cm.gray)
plt.show()

#histograma equalizado
fig = plt.figure(figsize=(20,5))
ax1 = fig.add_subplot(121)
plt.hist(img.ravel(), 256, [0, 256])

ax2 = fig.add_subplot(122)
plt.hist(imgE.ravel(), 256, [0, 256])
plt.show()

#histograma imagem colorida
img = cv.imread("imagens/pele.jpg")
azul, verde, vermelho = cv.split(img)

##
fig = plt.figure(figsize=(20,5))
x1 = fig.add_subplot(131)
plt.hist(azul.ravel(), 256, [0, 256])

x2 = fig.add_subplot(132)
plt.hist(verde.ravel(), 256, [0, 256])

x3 = fig.add_subplot(133)
plt.hist(vermelho.ravel(), 256, [0, 256])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
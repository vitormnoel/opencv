import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("imagens/predio.jpg")

sobelX = cv.Sobel(img, cv.CV_8U, 0, 1, ksize=7)
sobelY = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=7)

fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(131)
plt.imshow(img)

ax2 = fig.add_subplot(132)
plt.imshow(sobelX)

ax3 = fig.add_subplot(133)
plt.imshow(sobelY)

plt.show()
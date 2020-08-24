import cv2 as cv
from matplotlib import pyplot as plt 

img = cv.imread("imagens/formas.png")

g = cv.GaussianBlur(img, (9,9), 0)

fig = plt.figure(figsize=(20,50))
ax1 = fig.add_subplot(121)
plt.imshow(img)

ax2 = fig.add_subplot(122)
plt.imshow(g)
plt.show()
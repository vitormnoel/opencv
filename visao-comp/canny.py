import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("imagens/predio.jpg")

canny = cv.Canny(img, 75, 50)

fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(121)
plt.imshow(img)

ax2 = fig.add_subplot(122)
plt.imshow(canny, cmap=plt.cm.gray)

plt.show()
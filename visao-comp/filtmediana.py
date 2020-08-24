import cv2 as cv
from matplotlib import pyplot as plt 

img = cv.imread("imagens/einstein.png")

m = cv.medianBlur(img, 5)

fig = plt.figure(figsize=(20,50))

ax1 = fig.add_subplot(121)
plt.imshow(img, cmap=plt.cm.gray)

ax2 = fig.add_subplot(122)
plt.imshow(m, cmap=plt.cm.gray)

plt.show()
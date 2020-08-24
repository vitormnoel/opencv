import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("imagens/predio.jpg")

lap = cv.Laplacian(img, cv.CV_8U)

fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(121)
plt.imshow(img)

ax2 = fig.add_subplot(122)
plt.imshow(lap)

plt.show()
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("imagens/cebola.jpg", 0)
img2 = cv.imread("imagens/pele.jpg", 0)

hist, bins = np.histogram(img.ravel(), 256,[0, 256])
oi = plt.hist(hist.ravel(), 256,[0, 256])
plt.show()

hist2, bins2 = np.histogram(img2.ravel(), 256,[0, 256])
tchau = plt.hist(hist.ravel(), 256,[0, 256])
plt.show()

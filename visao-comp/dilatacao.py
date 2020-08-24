import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 

img = cv.imread("imagens/placa.png")

stru = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7,7))
print(stru)

pro = cv.dilate(img, stru, iterations=2)

fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(211)
plt.imshow(img)

ax2 = fig.add_subplot(212)
plt.imshow(pro)

plt.show()
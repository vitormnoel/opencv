import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("imagens/cafe.jpg", 0)

metodo = cv.THRESH_BINARY_INV + cv.THRESH_OTSU

ret, imgBin = cv.threshold(img, 0, 255, metodo)

print('o melhor limiar é: ', ret)

plt.hist(img.ravel(), 255, (0, 256))
cv.imshow("original", img)
cv.imshow("otsu", imgBin)

cv.waitKey(0)
cv.destroyAllWindows()
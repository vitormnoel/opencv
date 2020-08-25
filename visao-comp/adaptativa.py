import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("imagens/olho.png", 0)

imgGauss = cv.medianBlur(img, 7)

th2 = cv.adaptiveThreshold(imgGauss, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
th3 = cv.adaptiveThreshold(imgGauss, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('original', img)
cv.imshow('media', th2)
cv.imshow('gaussiana', th3)

cv.waitKey(0)
cv.destroyAllWindows()
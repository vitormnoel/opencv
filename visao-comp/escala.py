import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

im = cv.imread("imagens/eu.jpg", 0)

imgM = cv.resize(im, None, fx = 0.5, fy = 0.5, interpolation = cv.INTER_CUBIC)
cv.imshow("imagem original", im)
cv.imshow("im modificada", imgM)
cv.waitKey(0)
cv.destroyAllWindows()
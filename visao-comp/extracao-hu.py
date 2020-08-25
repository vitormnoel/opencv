import cv2 as cv
import numpy as np

img = cv.imread("imagens/circle.jpg", 0)

momentos = cv.moments(img)

momentosHu = cv.HuMoments(momentos)

print(momentosHu.flatten())
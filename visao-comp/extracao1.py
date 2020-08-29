import cv2 as cv
import numpy as np
import imutils
from matplotlib import pyplot as plt 

img = cv.imread("imagens/cebola1.jpg", 1)
img_gray = cv.imread("imagens/cebola1.jpg", 0)

img = imutils.resize(img, width=100)
img_gray = imutils.resize(img_gray, width=100)

cv.imshow("IMG EM RGB", img)
cv.imshow("IMG GRAY", img_gray)

cv.waitKey(0)
cv.destroyAllWindows()

valorM = cv.mean(img)
valorMD = cv.mean(img_gray)

(mean, std) = cv.meanStdDev(img)
(means, sts) = cv.meanStdDev(img_gray)

RGB = np.concatenate([(mean, std)]).flatten()
Gray = np.concatenate([(means, sts)]).flatten()

print("valores da media e desvio padrao RGB")
print(valorM)
print(RGB)

print("valores da media e desvio padrao tons de cinza")
print(valorMD)
print(Gray)
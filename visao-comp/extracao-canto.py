import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("imagens/hospital2.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv.cornerHarris(gray, 2, 3, 0.01)

elemento = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
dst = cv.dilate(dst, elemento)

img[dst > 0.05*dst.max()] = [0, 0, 255]

fig = plt.figure(figsize=(10,8))
plt.imshow(img)
plt.show()
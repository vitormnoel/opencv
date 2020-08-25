import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("imagens/estrada.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 70, 255)

lines = cv.HoughLinesP(edges, 1, np.pi/180, 10, 200)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1,y1), (x2,y2), (0, 0, 255), 3)

cv.imshow('imagem', img)
cv.waitKey(0)
cv.destroyAllWindows()
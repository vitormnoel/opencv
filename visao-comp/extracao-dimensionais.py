import cv2 as cv
import numpy as np

img = cv.imread("imagens/triangle.jpg", 0)

tipo = cv.THRESH_BINARY_INV
_, imgBin = cv.threshold(img, 0, 255, tipo)

modo = cv.RETR_TREE
metodo = cv.CHAIN_APPROX_SIMPLE

contorno, hierarquia = cv.findContours(imgBin, modo, metodo)

if len(contorno)>0:
    obj = contorno[0]
    area = cv.contourArea(obj)
    print("area: ", area)

    perimetro = cv.arcLength(obj, True)
    print("perimentro: ", perimetro)
else:
    print("sem contorno encontrado")



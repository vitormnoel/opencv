import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

full = cv.imread("imagens/ex_template_matching.jpg")
full = cv.cvtColor(full, cv.COLOR_BGR2RGB)

face = cv.imread("imagens/rosto_template.jpg")
face = cv.cvtColor(face, cv.COLOR_BGR2RGB)

sum([1, 2, 3])
mystring = 'sum'
eval(mystring)

myFunc = eval(mystring)

myFunc([1, 2, 3])

height, width, channels = face.shape

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for m in methods:

    #copia da imagem
    full_copy = full.copy()

    #função eval passando as strings
    method = eval(m)

    #aplicaçao TM com os metodos
    res = cv.matchTemplate(full_copy, face, method)

    plt.imshow(res)
    plt.title(m)
    plt.show()

for m in methods:
    #copia da imagem
    full_copy = full.copy()

    #função eval passando as strings
    method = eval(m)

    #aplicaçao TM com os metodos
    res = cv.matchTemplate(full_copy, face, method)

    #pegar os valores max e min, alem dos locais
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    #configurar o retangulo 
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + width, top_left[1] + height)

    cv.rectangle(full_copy, top_left, bottom_right, 255, 10)

    #plotar img
    plt.subplot(121)
    plt.imshow(res)
    plt.title("resultado")

    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title("plt correlacionados")
    plt.suptitle(m)

    plt.show()
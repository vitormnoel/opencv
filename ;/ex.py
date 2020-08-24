import numpy as np 
from matplotlib import pyplot as plt 
import cv2

def showImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def getColor(img, x, y):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def setColor(img, x, y, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)

    return img

def image():
    obj_img = cv2.imread("imagens/eu.jpg")
    altura, largura, canais_de_cor = obj_img.shape
    print("dimensões da img: "+ str(largura) +", "+ str(altura))
    print("Canais de cor: ", canais_de_cor)
    
    for y in range(0, altura):
        for x in range(0, largura):
            #print("["+ str(x) +","+ str(y) +"] = "+ str(obj_img[y][x]))
            #input()

            azul, verde, vermelho = getColor(obj_img, x, y)
            obj_img = setColor(obj_img, x, y, verde, 0, vermelho)

    cabeca = obj_img[50:50 + 65, 100:100 + 59]
    obj_img[161:161 + cabeca.shape[0], 101:101 + cabeca.shape[1]] = cabeca
    #cv2.imwrite("vitor.jpg", obj_img)
    showImage(obj_img)

def showImageGrid(img, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def main():
    img = cv2.imread("imagens/eu.jpg", 0)
    image()
    showImageGrid(img, "foto vitor")
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

main()
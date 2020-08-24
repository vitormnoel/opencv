import cv2 
import numpy as np 
from matplotlib import pyplot as plt

#histograma 
def main():
    img = cv2.imread("imagens/pele.jpg")
    plt.hist(img.ravel(), 256, [0, 256]) #plota um grafico 
    plt.show()

    print(img.shape)
    img.itemset((0, 0, 2), 255)
    img.itemset((0, 0, 1), 0)
    img.itemset((0, 0, 0), 0)
    
    img.itemset((0, 1, 2), 255)
    img.itemset((0, 1, 1), 0)
    img.itemset((0, 1, 0), 0)

    img.itemset((0, 2, 2), 255)
    img.itemset((0, 2, 1), 0)
    img.itemset((0, 2, 0), 0)

    plt.imshow(img)
    plt.show()

main()
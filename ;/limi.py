import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("imagens/pele.jpg", 0)
#limiarização
limiar, imgLimiar= cv.threshold(img, 150, 255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
cv.imshow("limiar", imgLimiar)
print(limiar)

crop = imgLimiar[100:100+90, 128:128+90] #corta parte da imagem
cv.imshow("crop", crop)

plt.hist(imgLimiar.ravel(), 256, [0, 256]) #plota um grafico 
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
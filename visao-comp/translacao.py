import cv2
import numpy as np
from matplotlib import pyplot as plt

original = cv2.imread("imagens/eu.jpg", 0)

linhas, colunas = original.shape
matriz = np.float32([(1, 0, 50),[0, 1, 100]])
deslocada = cv2.warpAffine(original, matriz, (linhas, colunas))

fig = plt.figure(figsize=(10,8))
plt.imshow(deslocada, cmap=plt.cm.gray)
plt.show()
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread("imagens/hospital2.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 10, 0.05, 0.25)

for item in corners:
    x, y = item[0]
    cv.circle(img, (x, y), 4, (0, 0, 255), -1)

fig = plt.figure(figsize=(10,8))
plt.imshow(img)
plt.show()
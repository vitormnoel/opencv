import cv2 as cv

img = cv.imread("imagens/circle.jpg", 0)

momentos = cv.moments(img)

print(len(momentos))
print(momentos)

area = momentos['m00']
print(area)
print("\n")

x = momentos['m10']/area
y = momentos['m01']/area

print("medidas")
print(x)
print(y)

cx = int(momentos['m10']/momentos['m00'])
cy = int(momentos['m01']/momentos['m00'])

print("centro")
print(cx)
print(cy)

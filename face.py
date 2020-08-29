import cv2 as cv

face_cascade = cv.CascadeClassifier('C:\Python38\lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv.imshow('face detectada', img)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()

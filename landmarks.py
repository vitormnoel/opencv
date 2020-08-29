import cv2 as cv
import dlib
from imutils import face_utils

p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        for j in range(1,68):
            cv.putText(frame, str(j), (shape.part(j).x, shape.part(j).y), 
            fontFace = cv.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale = 0.3, color=(0,255,255))
    cv.imshow("frame", frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break 

cv.destroyAllWindows()
cap.release()
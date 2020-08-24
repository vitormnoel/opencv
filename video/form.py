import cv2

cap = cv2.VideoCapture(0)

#Callback retangulo
def draw_rect(event, x, y, flags, params):
    global pt1, pt2, topLeftClicked, bottomRightClicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if topLeftClicked == True and bottomRightClicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeftClicked = False
            bottomRightClicked = False

        if topLeftClicked == False:
            pt1 = (x, y)
            topLeftClicked = True

        elif bottomRightClicked == False:
            pt2 = (x, y)
            bottomRightClicked = True

##variaveis globais
pt1 = (0,0)
pt2 = (0,0)
topLeftClicked = False
bottomRightClicked = False

cv2.namedWindow('Teste')
cv2.setMouseCallback('Teste', draw_rect)

while True:
    ret, frame = cap.read()

    if topLeftClicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255))
    if topLeftClicked and bottomRightClicked:
        cv2.rectangle(frame, pt1, pt2, color=(0, 0, 255), thickness= 1)

    cv2.imshow("Teste", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
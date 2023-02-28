import cv2
import mediapipe as mp
import os

name = "voy"
path = "/home/usuario/PycharmProjects/pythonProject/Photos/training"
directory = path +'/'+name
if not os.path.exists(directory):
    print('directory has been created', directory)
    os.makedirs(directory)

cont = 0

cam = cv2.VideoCapture(0)

class_hands = mp.solutions.hands
hands = class_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.75, min_tracking_confidence=0.5)

drawing = mp.solutions.drawing_utils

while(1):
    ret, frame = cam.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    copy = frame.copy()
    resultado = hands.process(color)
    posiciones = []

    if resultado.multi_hand_landmarks:
        for hand in resultado.multi_hand_landmarks:
            for id, lm in enumerate(hand.landmark):
                height, width, c = frame.shape
                coordx, coordy = int(lm.x*width), int(lm.y*height)
                posiciones.append([id, coordx, coordy])

                drawing.draw_landmarks(frame, hand, class_hands.HAND_CONNECTIONS)
        if len(posiciones) != 0:
            pto_i1 = posiciones[4]
            pto_i2 = posiciones[20]
            pto_i3 = posiciones[12]
            pto_i4 = posiciones[0]
            pto_i5 = posiciones[9]
            x1,y1 = (pto_i5[1]-160),(pto_i5[2]-160)
            ancho, alto = (x1+160),(y1+240)
            x2, y2 = x1+ancho, y1+alto
            dedos_reg = copy[y1:y2, x1:x2]
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0, 3))
            dedos_reg = cv2.resize(dedos_reg, (200,200), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite(directory+"/Mano_{}.jpg".format(cont), dedos_reg)
            cont += 1

    cv2.imshow("Video", frame)
    k = cv2.waitKey(1)
    if k == ord('s') or cont >= 300:
        break
cam.release()
cam.destroyAllWindows()
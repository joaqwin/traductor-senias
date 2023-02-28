import mediapipe as mp
import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh(max_num_faces=1)

mpDibujo = mp.solutions.drawing_utils
confiDibujo = mpDibujo.DrawingSpec(thickness=1, circle_radius=1)

while(1):
    ret, frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = face.process(color)
    posiciones = []

    px = []
    py = []
    lista = []
    r = 5
    t = 3

    if resultado.multi_face_landmarks:
        for rostros in resultado.multi_face_landmarks:
            mpDibujo.draw_landmarks(frame, rostros,mp_face.FACEMESH_CONTOURS, confiDibujo, confiDibujo)

            for id,puntos in enumerate(rostros.landmark):
                height, width, c = frame.shape
                x,y = int(puntos.x*width), int(puntos.y*height)
                px.append(x)
                px.append(y)
                lista.append([id, x, y])
                if len(lista) == 468:
                    #ASOMBRADO
                    x1, y1 = lista[0][1:]
                    x2, y2 = lista[17][1:]
                    cv2.circle(frame, (x1, y1), 3, (0,255,0), 3)
                    cv2.circle(frame, (x2, y2), 3, (255,0,0), 3)
                    dist = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
                    print(dist)
                    if dist > 44:
                        cv2.putText(frame, 'ASOMBRADO' , (x1, y1 - 5), 1, 1.3, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow("Video", frame)
    k = cv2.waitKey(1)
    if k == ord('s'):
        break
cap.release()
cap.destroyAllWindows()
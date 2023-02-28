import multiprocessing
import os
import threading


def playAudio(texto):
    os.system("python3 /home/usuario/PycharmProjects/pythonProject/test.py " + '"' + texto + '"')

hilo = threading.Thread(target=playAudio, args=("audio",))
hilo.start()

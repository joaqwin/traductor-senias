import threading
from tkinter import *
from PIL import Image, ImageTk
import cv2
import imutils
import numpy as np
import os
import multiprocessing
import subprocess

def start():
    pantalla.after(3000, escribirTexto)
    subprocess.Popen(["python3", "/home/usuario/PycharmProjects/pythonProject/prediction.py"])

def escribirTexto():
    try:
        file = open("/home/usuario/PycharmProjects/pythonProject/Traducciones/textoTraduccion/texto.txt", 'r')
        lines = file.readlines()
        nrlines = len(lines)
        print("nobueno")
        if nrlines == 0:
            print("lineas 00000")
            pass
        else:
            print("EsCRIBIENDOO")
            texto2.config(text=lines[nrlines - 1])
            texto2.config(wraplength=500, justify='left')
            texto2.after(3000, escribirTexto)
    except:
        print("hola")



pantalla = Tk()
pantalla.title("Traductor")
pantalla.geometry("1280x720")

imagenFondo = PhotoImage('/home/usuario/PycharmProjects/pythonProject/interfaz/Fondo.png')
background = Label(image = imagenFondo, text = "Fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

texto1 = Label(pantalla, text="VIDEO EN TIEMPO REAL")
texto1.place(x = 550, y = 10)

texto2 = Label(pantalla, text="", font=("Arial", 20))
texto2.place(x = 770, y = 100)
escribirTexto()

imagenBI = PhotoImage(file="/home/usuario/PycharmProjects/pythonProject/interfaz/Inicio.png")
inicio = Button(pantalla, text="Iniciar", image=imagenBI, height="125", width="404", command=start)
inicio.place(x = 100, y = 580)
pantalla.after(3000, escribirTexto)

pantalla.mainloop()



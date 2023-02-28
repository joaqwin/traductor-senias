import speech_recognition as sr
from PIL import Image

# Inicializa el reconocimiento de voz
r = sr.Recognizer()

# Inicia la grabación del micrófono
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Convierte el audio a texto
text = r.recognize_google(audio, language='es-ES')

print("You said: " + text)

if text == "Playa":
    im = Image.open("/home/usuario/PycharmProjects/pythonProject/Photos/training/playa.jpg")
    im.show()
elif text == "Hola":
    im = Image.open("/home/usuario/PycharmProjects/pythonProject/Photos/training/hola.jpg")
    im.show()
elif text == "Voy":
    im = Image.open("ruta/a/tu/voy.jpg")
    im.show()
elif text == "¿Como estás?":
    im = Image.open("/home/usuario/PycharmProjects/pythonProject/Photos/training/¿como estas?.jpg")
    im.show()
elif text == "Caminar":
    im = Image.open("/home/usuario/PycharmProjects/pythonProject/Photos/training/caminar.jpg")
    im.show()



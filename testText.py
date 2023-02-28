import datetime

fecha_actual = datetime.datetime.now().date()
hora_actual = datetime.datetime.now().time()
stringFecha = fecha_actual.strftime("%Y-%m-%d")
stringHora = hora_actual.strftime("%H:%M:%S")

print(stringFecha)

print(hora_actual)

print(stringHora)
duracion = int(input("Ingrese la duración de la llamada en minutos: "))

destino = input("Ingrese el destino de la llamada (Estados Unidos, Canadá, Europa, Resto del mundo):")


if destino == "Estados Unidos":
    print(duracion * 900)
elif destino == "Canadá":
    print(duracion * 800)
elif destino == "Europa":
    print(duracion * 950)
else:
    print(duracion * 1250)


if duracion > 15:
        destino =* 0.80




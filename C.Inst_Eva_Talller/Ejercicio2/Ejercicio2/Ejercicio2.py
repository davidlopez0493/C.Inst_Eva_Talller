duracion = int(input("Ingrese la duración de la llamada en minutos: "))

destino = input("Ingrese el destino de la llamada (Estados Unidos, Canadá, Europa, Resto del mundo):")

if destino == "Estados Unidos" and duracion > 15:
    print((duracion * 900)*0.80)
elif destino == "Estados Unidos":
    print(duracion * 900)

elif destino == "Canadá" and duracion > 15:
    print((duracion * 800)*0.80)
elif destino == "Canadá":
    print(duracion * 800)

elif destino == "Europa" and duracion > 15:
    print((duracion * 950)*0.80)
elif destino == "Europa":
    print(duracion * 950)

elif destino == "Resto del mundo" and duracion > 15:
    print((duracion * 1250)*0.80)
elif destino == "Resto del mundo":
    print(duracion * 1250)
else:
    print("no valido")








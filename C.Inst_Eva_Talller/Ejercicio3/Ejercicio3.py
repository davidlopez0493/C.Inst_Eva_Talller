calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))
calificacion4 = float(input("Ingrese la cuarta calificación: "))

Valor_matricula = float(input("Ingrese el valor de la matricula: "))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4

if 4 <= promedio <= 5:
    print("Excelente su promedio es de:",promedio,"el valor a pagar de su matricula es de:", Valor_matricula * 0.80)
elif 3 <= promedio <= 3.99:
    print("Bien su promedio es de:",promedio,"el valor a pagar de su matricula es de:", Valor_matricula)
elif 0 <= promedio <= 2.99:
    print("Deficiente su promedio es de:",promedio,"el valor a pagar de su matricula es de:", Valor_matricula)
else:
    print("calificacion fuera del rango")



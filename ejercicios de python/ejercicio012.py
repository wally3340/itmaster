"""Escribir un programa en Python que solicite al usuario ingresar dos valores que representen
las medidas en grados de dos ángulos interiores de un triángulo. Luego, calcular y mostrar por
pantalla el valor en grados del ángulo restante.
Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados.
Es decir, la suma de los ángulos internos de un triángulo siempre es igual a 180 grados. Por lo tanto,
para calcular el ángulo restante es necesario restar la suma de los dos ángulos interiores ingresados al valor 180." """

angulo1 = int(input("Escribir el valor del angulo: "))
angulo2 = int(input("Escribir el valor del angulo: "))
valor_angulo_restante = 180 - angulo1 - angulo2

if angulo1 < 0:
    print("El valor ingresado debe ser mayor o igual a 0")
else:
    print(angulo1)

if angulo2 < 0:
    print("El valor ingresado debe ser mayor o igual a 0")
else:
    print(angulo2)
    
if  (valor_angulo_restante + angulo1 + angulo2) > 180 :
    print("La suma de los angulos de un triangulo debe sumar 180°")
else:
    print(f"El valor del angulo restante es {valor_angulo_restante}°")

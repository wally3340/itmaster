"""Escribir un programa que permita ingresar una edad (entre 1 y 120 años),
un género ('F'para mujeres, 'M' para hombres) y un nombre.
En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido),
informar tal situación indicando el nombre de la persona. Si los datos están bien
ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años
o más y los hombres con 65 años o más, si la persona está en edad de jubilarse. """

nombre = input("Nombre: ")
edad = int(input("Edad: "))
genero = input("Genero (F o M): ").upper()

 

if genero != "M" and genero != "F" or edad > 120:
    print("Los datos son erroneos")
elif edad >= 60 and genero == "F":
    print("Se jubila")
elif edad >= 65 and genero == "M":
    print("Se jubila")
else:
    print(f"{nombre}No se jubila")
 












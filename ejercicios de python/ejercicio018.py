"""Escribir un programa que permita al usuario ingresar un número entero y luego muestre un mensaje indicando si el número es par o impar. """

numero = int(input("Ingrese un número: "))
print("El número ingresado es:", numero)
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
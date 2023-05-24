"""Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:
a. Multiplicado por 10. (utilizar el operador *)
b. Dividido por 10. (utilizar el operador /)
c. Elevado al cuadrado. (utilizar el operador **)
Cada resultado debe mostrarse en una línea distinta."""

numero = int(input("Ingrese un número entero: "))
resultado1 = numero * 10
resultado2 = numero / 10
resultado3 = numero ** 2
print(numero,"*","10","=",resultado1)
print(numero,"/","10","=",resultado2)
print(numero,"**",numero,"=",resultado3)
"""Escribir un programa que permita ingresar un número entero n.
Debe mostrar los primeros 10 múltiplos de n."""

numero = int(input("Escribir el numero: "))
print(f"Los primeros 10 multiplos de {numero} son: ")
for i in range (1,11):  
  multiplo = numero * i
  print(multiplo)

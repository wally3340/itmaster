"""Leer números hasta que se ingrese un cero.
Mostrar la suma.

lista1 ==> 1,2,8,5,4,7,7,7,5,6,0
lista2 ==> 2,8,6,4,9,7,3,0
lista3 ==> 0
""" 
# ANTES (PARA TODOS)
sumador = 0
numero = int(input("Numero: "))
while numero != 0:
    # DURANTE (PARA CADA DATO)
    sumador += numero #sumador = numero + sumador
    numero = int(input("Numero: "))
# DESPUES (TOTALES)   
print(f"La suma es:{sumador}")
      
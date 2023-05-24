"""Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor. """

num1 = int(input("Escriba un numero: "))
num2 = int(input("Escriba un numero: "))
num3 = int(input("Escriba un numero: "))

if num1 > num2 and num1 > num3:
    print(f"El numero {num1} es el mayor")
elif num2 > num3:
    print(f"El numero {num2} es el mayor")  
else:
    print(f"El numero {num3} es el mayor")      
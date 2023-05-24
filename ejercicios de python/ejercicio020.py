"""Escribir un programa que permita ingresar dos números
enteros e indicar si el primero es mayor, menor o igual al segundo """

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que {num2}")
elif num1 == num2:
    print("Los numeros son iguales") 
else:
    print(f"El numero {num1} es menor que {num2}" )       
"""Escribir un programa que solicite al usuario ingresar tres notas de un alumno.
El programa debe mostrar por pantalla las notas separadas por comas en un renglón y 
el promedio de las notas en el siguiente renglon."""

nota1 = int(input("Escriba la nota: "))
nota2 = int(input("Escriba la nota: "))
nota3 = int(input("Escriba la nota: "))
promedio = (nota1 + nota2 + nota3)/3
print("Notas:",nota1,",",nota2,",",nota3)
print("Promedio:",promedio)

""" Escribir un programa que permita resolver el siguiente problema:
Tres personas aportan diferente capital a una sociedad y desean saber el valor
total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y su capital aportado,
a partir de esto calcular e informar lo requerido previamente."""

persona1 = input("Ingrese el nombre del socio:  ")
capital1 = float(input("Ingerese el capital aportado: "))
persona2 = input("Ingrese el nombre del socio:  ")
capital2 = float(input("Ingerese el capital aportado: "))
persona3 = input("Ingrese el nombre del socio:  ")
capital3 = float(input("Ingerese el capital aportado: "))

total_aportado = capital1 + capital2 + capital3

porcentaje_inversion_persona1 = round((capital1 / total_aportado) * 100, 2)
porcentaje_inversion_persona2 = round((capital2 / total_aportado) * 100, 2)
porcentaje_inversion_persona3 = round((capital3 / total_aportado) * 100, 2)

print(total_aportado)
print(f"El total aportado por el socio {persona1} fue de {porcentaje_inversion_persona1}")
print(f"El total aportado por el socio {persona1} fue de {porcentaje_inversion_persona2}")
print(f"El total aportado por el socio {persona1} fue de {porcentaje_inversion_persona3}")

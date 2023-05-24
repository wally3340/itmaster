"""Escribir un programa que permita ingresar la cantidad de invitados
a una fiesta y la cantidad de asientos disponibles en el salon. Debes
indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar
cuántos faltan para que todos los invitados puedan sentarse. """

invitados = int(input("Invitados: "))
asientos = int(input("Asientos: "))
dif_asientos = invitados - asientos

if invitados <= asientos:
    print("Los asientos alcanzan para todos")
else:
    invitados != asientos
    print(f"Faltan {dif_asientos} asientos ")
   
    



















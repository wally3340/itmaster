"""Escribir un programa para calcular el importe a cobrar por un vendedor, 
considerando su sueldo fijo de $200000 pesos más el 16% del monto total de ventas realizadas durante un mes.
Pensando los pasos para resolver el problema:
1 Solicitar al usuario que ingrese el monto total de ventas realizadas por el vendedor durante el mes en una variable correspondiente.

2 Calcular el 16% del monto total de ventas realizadas y almacenar el resultado en una variable.

3 Sumar el resultado del cálculo anterior al sueldo fijo del vendedor.

4 Mostrar el importe a cobrar por el vendedor. """

SUELDO_FIJO = 200000
ventas_realizadas = int(input("Ingrese el total de ventas realizadas: "))
ganancia = (ventas_realizadas * 16) / 100

importe_a_cobrar = SUELDO_FIJO + ganancia
print(importe_a_cobrar)
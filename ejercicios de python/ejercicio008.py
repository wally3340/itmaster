"""Escribir un programa que permita ingresar el valor monetario de una hora de trabajo

y la cantidad de horas trabajadas por día, para calcular el salario semanal de un trabajador

que trabaja todos los días hábiles y la mitad de las horas del día hábil los sábados, suponiendo

que todas las horas tienen el mismo valor."""


valor_hora = int(input("Ingrese el valor de la hora: "))

horas_trabajadas_por_dia = int(input("Ingrese las horas trabajadas: "))

dia_habil = horas_trabajadas_por_dia * valor_hora

DIAS_HABILES = 5

semanal = dia_habil * DIAS_HABILES

salario = semanal + (dia_habil / 2)
print(salario)

"""Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por
cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el nombre del vendedor
y el salario que le corresponde en un determinado mes.
Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
¿Sobran datos? ¿Qué datos sobran? """

vendedor = input("Ingrese el nombre del vendedor: ")
SUELDO = int(input("Ingrese el sueldo base: "))
COMISION = int(input("Ingrese la cantidad de ventas realizadas: "))
premio = (COMISION * 5) / 100

salario = SUELDO + COMISION + premio

print(vendedor)
print(salario)

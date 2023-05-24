"""Escribir un programa que permita al usuario ingresar el ancho y largo de un terreno en metros,
junto con el valor del metro cuadrado de tierra. El programa debe calcular y mostrar el valor total del terreno.
Además, debe calcular la cantidad de metros de alambre necesarios para cercar completamente
el terreno a tres alturas distintas. """

largo_del_terreno = int(input("Ingrese el largo del terreno en metros: "))
ancho_del_terreno = int(input("ingrrese el ancho del terreno en metros: "))
VALOR_DEL_METRO_CUADRADO_DE_TIERRA = 50
superficie_del_terreno = largo_del_terreno * ancho_del_terreno
valor_total_terreno = superficie_del_terreno * VALOR_DEL_METRO_CUADRADO_DE_TIERRA
print(valor_total_terreno)

perimetro_del_terreno = (largo_del_terreno * 2) + (ancho_del_terreno *2)

alambre1 = perimetro_del_terreno * 1
alambre2 = perimetro_del_terreno * 2
alambre3 = perimetro_del_terreno * 3
print(f"Se necesitan {alambre1}m de lambre para una altura de 1m")
print(f"Se necesitan {alambre2}m de lambre para una altura de 2m")
print(f"Se necesitan {alambre3}m de lambre para una altura de 3m")

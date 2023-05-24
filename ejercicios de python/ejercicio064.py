"""Un animal en rehabilitación después de una cirugía requiere ser alimentado y monitoreado en un zoológico.
Se alimenta al animal 3 veces al día y se le da de comer hasta que ya no tenga ganas de comer.
Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (número entero)
que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N').
Se desea conocer:
Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento y cuánto fue esa cantidad.
El total en kg de alimento recibido.
Promedio de alimento por tanda. """

CANTIDAD_TANDAS = 3
total = 0

for comida in range(CANTIDAD_TANDAS):
    print(f"comida {comida + 1} de {CANTIDAD_TANDAS}")
    terminar = False
    while not terminar:
        kg = int(input("KG: "))
        total += kg
        terminar = input("Continua [S/N]: ").upper() == "N"
print(f"Total: {total}")
print(f"Comida total: {total/CANTIDAD_TANDAS} ")
























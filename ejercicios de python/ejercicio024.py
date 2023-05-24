"""Para acceder a cierta atracción, es necesario cumplir con dos requisitos:
tener al menos 10 años de edad y medir más de 1,60 metros.
(Ojo, tener en cuenta las palabras: más,al menos y sobre todo la letra y)
Escribir un programa en Python que solicite al usuario su edad y estatura, y
que determine si cumple con los requisitos para subir a la atracción.
Si cumple con ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la pantalla.
Si no cumple con alguno de los requisitos, el programa debe imprimir un mensaje que indique 
el motivo por el cual no puede subir. Por ejemplo, si no cumple con el requisito de la edad,
el programa debe imprimir "Lo siento, eres demasiado joven para acceder."
Si no cumple con el requisito de la estatura,
el programa debe imprimir "Lo siento, eres demasiado bajo para acceder" """

edad = int(input("Escriba la edad: "))
altura = float(input("Escriba la altura: "))

if edad >= 10 and altura > 1.6:
    print("Puede acceder")
elif edad  < 10:
        print("Lo siento, eres demasiado joven para acceder.")
elif altura  <= 1.6:
    print("Lo siento, eres demasiado bajo para acceder")

    
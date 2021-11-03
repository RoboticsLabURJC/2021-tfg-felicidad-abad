## Juego para intentar adivinar una cadena de números,
## se pide al usuario la longitud de la cadena (2-7) y
## a continuación se pide al usuario que lo adivine. Se
## responderá con la cantidad de posiciones que se han
## adivinado.
import random

print("Longitud de la cadena a adivinar: ")
longitud = input()

numero = random.randint(1,9)

## Cuando tenemos la cadena, creamos el número random
longitudAux = 1

while longitudAux < int(longitud):
    numeroAux = random.randint(1,9)
    numero = str(numero) + str(numeroAux)
    longitudAux = longitudAux + 1

print(numero)

## Pedir numero al usuario
print("¿Puedes adivinar el número? Introduce una respuesta: ")
guess = input()

check = 0
while check < int(longitud):
    if numero[check] == guess[check]:
        print("Has acertado una!")
    check = check + 1

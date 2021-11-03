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

def checkAciertos(longitud, guess):
    check = 0
    acertadas = 0

    while check < int(longitud):
        if numero[check] == guess[check]:
            acertadas = acertadas + 1
        check = check + 1
    return acertadas

result = checkAciertos(longitud,guess)
while result != int(longitud):
    print("")
    print("Con la cadena " + str(guess) + " has adivinado " + str(result) + " posiciones")
    print("¿Puedes adivinar el número? Introduce una respuesta: ")
    guess = input()
    result = checkAciertos(longitud,guess)

if result == int(longitud):
    print("")
    print("¡Has acertado todos los números!")

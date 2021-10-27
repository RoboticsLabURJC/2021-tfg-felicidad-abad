## Juego dragones
## Hay que escoger una cueva (R o L) y se echará a suertes si en esa cuevas
## vive un dragón amigable o uno violento. Por cada dragón amigable que
## encuentres, sumas 100 puntos y pasas una ronda más.
## Ejercicio de: https://pythondiario.com/
import random
import time

def introduccion():
    print ("Estamos en una isla de dragones. Delante hay dos cuevas.")
    print ("En una, el dragon es amigable, compartirá su tesoro contigo")
    print ("El otro dragon, atacará en cuanto te vea")
    print ("")

## Escoger una cueva para entrar
def chooseCave():
    cueva = ""
    if (cueva != "R" and cueva != "L"):
        print("¿A qué cueva entramos? ¿Derecha (R) o izquierda (L)")
        cueva = input()
        print("")
    return cueva

## Comprobar si la cueva es buena o mala
puntos = 0
def checkCave(cueva, puntos):
    eleccion = 0
    if cueva.upper() == "R":
        eleccion = 1
    elif cueva.upper() == "L":
        eleccion = 2
    else:
        print("No es una opción válida")

    luck = random.randint(1,2)
    if eleccion == luck:
        print("Enhorabuena! El dragón comparte su tesoro contigo")
        puntos = puntos + 100
        keepPlaying = True
    else:
        print("Game Over")
        keepPlaying = False

    return puntos, keepPlaying

## Continuar a la historia
def story(cueva,puntos):
    print ("Entras en la cueva")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragon salta delante tuyo y...")
    time.sleep(2)
    result = checkCave(cueva,puntos)
    puntos = result[0]
    keepPlaying = result[1]

    return puntos, keepPlaying

def juegoCompleto(puntos,keepPlaying,ronda):
    while keepPlaying == True:
        print("------------------------------------------------")
        print("RONDA " + str(ronda))
        introduccion()
        cueva = chooseCave()
        keepPlaying = story(cueva,puntos)
        puntos = keepPlaying[0]
        keepPlaying = keepPlaying[1]
        ronda = ronda + 1
    else:
        print("Has conseguido un total de: " + str(puntos) + " puntos")
        puntos = 0
        print("Play again? Y/N")
        decision = input()

    return puntos,keepPlaying,decision

ronda = 1
keepPlaying = True
gameState = juegoCompleto(puntos,keepPlaying,ronda)
puntos = gameState[0]
keepPlaying = gameState[1]
decision = gameState[2]

while decision.upper() == "Y":
    print("")
    print("N E W   G A M E")
    ronda = 1
    keepPlaying = True
    gameState = juegoCompleto(puntos,keepPlaying,ronda)
    puntos = gameState[0]
    decision = gameState[2]
    ronda = ronda + 1
else:
    if decision.upper() == "N":
        print("Gracias por jugar!")
        print("Has llegado hasta la ronda " + str(ronda))
        print("")
    else:
        print(decision + " no es una opcion valida")
        print("")

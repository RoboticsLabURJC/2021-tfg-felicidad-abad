print("Prueba1")

## Función para devolver el mayor de dos números
def maximo(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2

print(maximo(1,5))

## Función que compara tres números
def maximoDeTres(n1, n2, n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    else:
        if n2>n3:
            return n2
        else:
            return n3

print(maximoDeTres(1,6,10))

## Función para comprobar si una letra es una vocal o no
def esVocal(a1):
    vocales = ["a","e","i","o","u"]
    toCheck = a1.lower()
    if (toCheck in vocales):
        return True
    else:
        return False

print(esVocal("A"))
print(esVocal("h"))

## Función para contar las vocales en una cadena
def contarVocales(cadena):
    contador = 0
    for char in cadena:
        if esVocal(char):
            contador = contador + 1
    return contador

print(contarVocales("Pablito clavo un clavito"))

## Función para dar la vuelta a una cadena
def invertir(cadena):
    inversion = cadena[::-1]
    return inversion

print(invertir("abcd"))

## Función para reconocer palíndromos
def esPalindromo(cadena):
    if cadena.lower() == invertir(cadena.lower()):
        return True
    else:
        return False

print("¿pepe es palindromo?: " + str(esPalindromo("pepe")))
print("¿Radar es palindromo?: " + str(esPalindromo("Radar")))

## Función que compara dos listas
## Devuelve true si tienen elementos en común, False si no los tienen
def comparar(lista1, lista2):
    contador = 0
    for entrada in lista1:
        if entrada in lista2:
            contador = contador + 1

    if contador > 0:
        return True
    else:
        return False


lista1 = ["manzana","pera","mango"]
lista2 = ["fresa", "mango", "banana"]
print("El resultado de comparar listas es: " + str(comparar(lista1,lista2)))

## Imprimir un caracter tantas veces como se indique
def pintarCaracter(caracter, repeticiones):
    i = 0
    string = ""
    while i < repeticiones:
        string = string + caracter
        i = i + 1

    return string

print(pintarCaracter("*",3))

## Imprimimos una serie
def pintarSerie(caracter, serie):
    salida = ""
    for repeticiones in serie:
        salida = salida + pintarCaracter(caracter, repeticiones)
        salida = salida + "\n"
    return salida

print("La serie queda:")
print(pintarSerie("*",[1,2,3,4]))

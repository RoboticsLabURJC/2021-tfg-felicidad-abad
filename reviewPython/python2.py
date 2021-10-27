## Función para devolver la palabra más larga de un array
def palabraLarga(cadena):
    maxLetras = 0
    word = ""
    for palabra in cadena:
        if len(palabra) > maxLetras:
            maxLetras = len(palabra)
            word = palabra
    return word

cadena = ["pepe", "mamama", "sol"]
print(palabraLarga(cadena))

## Función para devolver palabras con más de x caracteres
def returnPalabra(num, cadena):
    arr = []
    for palabra in cadena:
        if len(palabra) > num:
            arr.append(palabra)
    return arr

print(returnPalabra(3,cadena))

## Función para introducir cadena y contar letras
def contarLetras():
    texto = input("Introduce una palabra: ")
    array = texto.split()
    return palabraLarga(array)

print(contarLetras())

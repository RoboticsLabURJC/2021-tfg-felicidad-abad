import json

## Ingresar año actual
year = input("¿En que año estamos?: ")

## Ingresamos datos de 3 personas (nombre + año nacimiento)
class myPerson(object):

    def __init__(self, name, surname, birthYear):
        self.name = name
        self.surname = surname
        self.birthYear = birthYear

i = 0
personArr = []
for i in range(3):
    name = input("Escribe tu nombre: ")
    surname = input("Escribe tu apellido: ")
    birthYear = input("Escribe tu año de nacimiento: ")

    ## ¿Comprobación de datos?
    new_Person = myPerson(name, surname, birthYear)
    personArr.append(new_Person.__dict__)
    i = i + 1


## Calcular cuantos años cumple en este curso
def calcularEdad(year, birthYear):
    age = int(year) - int(birthYear)
    return age


for person in personArr:
    age = calcularEdad(year,person['birthYear'])
    person['age'] = age
    print("La edad actual de " + person['name'] + " es " + str(person['age']))

# Dentro de Python no es necesario declarar nuestras variables asignandoles una clase.
# Basta con simplemente darle un nombre:

nombre = "Uriel"
edad = 20
promedio = 8.8

print(nombre)
print(edad)
print(promedio)

# Se le asigna la clase dependiendo de que tipo de dato está manejando la variable

# Variable string
print(type(nombre))
# Variable integer
print(type(edad))
# Variable float
print(type(promedio))

# Tipos de datos en Python: 

    # Integer: numeros enteros

    # Float: numeros decimales


# Funciones basicas de Python:


edad_a_cadena = str(edad)   # Convertir a una cadena
print(edad_a_cadena)
print(type(edad_a_cadena))  # Corroboramos la clase de datoss


# Concatenación de variables en un print. Al contrario que en otros lenguajes, Python asigna
# un espacio de linea automaticamente.
print(edad, edad_a_cadena, "hola")

# Los print también pueden recibir parametros
print("Este es mi nombre:", nombre)

# Funciones del sistema
print(len(nombre))   # Imprime el largo de nuestra variable


#¡¡¡¡NO ABUSAR DE ESTA SINTAXIS!!!!

# Variables en una sola linea. Al igual que en otros lenguajes, podemos crear distintas
# variables en una sola linea. Recordando que también no es necesario asignar una clase
# a las variables, nos puede quedar algo así:
name, sourtname, alias, age = "Uriel", "Serano", "Uri", 35
print("Mi nombre es", name, sourtname,"tengo", age, "años y me conocen como", alias)

# Uso de inputs

name = input("Cual es tu nombre?:")
age = input('Cual es tu edad?:')

print("tu nombre es", name, "con", age, "años de edad")

name = 35
age = "Uriel"

print("mi nombre es", name, "con", age, "años")

# Al no definir los tipos de datos, si se le reasigna otro tipo de dato este cambiará.
# Esta puede ser un arma de doble filo puesto que dependiendo de nustras necesidades puede
# causar problemas.

# Una forma de forzar el tipo es la siguiente

address: str = "Mi dirección"
address = 32
print(type(address))
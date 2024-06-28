### Strings ###

# Las strings pueden ser declaradas con comillas simples o dobles
mi_string = 'Mi String'
mi_otra_string = "Mi Otra String"

# Podemos hayar la longitud de nuestra string con la función 'len'
print(len(mi_string))
print(len(mi_otra_string))

# También se pueden concatenar las cadenas
print(mi_string + " " + mi_otra_string)

# Podemos hacer un salto de linea con '\n'
my_new_line_string = "Este es un string con \nFUAAAA SALTO DE LINEA"
print(my_new_line_string)

# Con '\t' se pueden realizar tabulaciones
my_tab_string = '\tME EMPUJAN AAAAAAA'
print(my_tab_string)

# Con ayuda de la doble barra invertida '\\', podemos ignorar los espaciados
my_scape_string = '\\tEste es un string \\nMescapooooo'
print(my_scape_string)


# Formateo

name, secondname, age = 'Uriel', 'Serrano', 20

# En este formateo no es necesario especificar el tipo de variable, puesto que no toma en cuenta el formato
print("Mi nombre es {} {} y tengo {} años".format(name, secondname, age))   # Imprime el objeto sin formatear 
# De esta forma es similar a lenguajes como C, y es importante especificar el tipo de dato
print("Mi nombre es %s %s y tengo %d años" %(name, secondname, age))        # Imprime nuestro valor formateado

# Otra forma de imprimir sin formato es de la siguiente
print(f"Mi nombre es {name} {secondname} y tengo {age} años") 


# Desempaquetado de caracteres
language = 'python'
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

# Toma desde el segundo numero (dirección 1) y no toma en cuenta el ultimo (dirección 3)
language_slice = language[1:3]
print(language_slice)

# Imprime todo desde la dirección 1
language_slice = language[1:]
print(language_slice)

# Cuenta desde el final
language_slice = language[-2]
print(language_slice)

# Cuenta desde el final
language_slice = language[0:6:2]
print(language_slice)

# Revierte nuestra cadena
reversed_language = language[::-1]
print(reversed_language)


# Funciones

print(language.capitalize())        # Imprime la primera en mayuscula
print(language.upper())             # Imprime todas en mayusculas
print(language.count("t"))          # Cuenta los caracteres que tenga la cadena
print(language.isnumeric())         # Corrobora si tiene una cadena numerica
print("1".isnumeric())
print(language.lower())             # Imprime en minusculas
print(language.upper().isupper())   # Convierte en mayusculas y corrobora si está en mayusculas 

### Operadores ###

print("Suma", 3 + 4)    # Suma
print("Resta", 3 - 4)   # Resta
print("Por", 3 * 4)     # Multiplicación
print("Residuo", 4 % 3) # Modulo / Residuo
print("División", 3 / 4)# División
print("Potencia", 3 ** 4)   # Exponencial
print(5 // 4)   # Floor division / Aproxima a un numero entero (NO REDONDEA, SOLO TOMA EL ENTERO)


# Los operadores también sirven para concatenar cadenas
print("Hola" + " python," + " ¿Qué tal?")

# No podemos concatenar un entero, por lo que es necesario convertirlo a cadena
print("Hola" + str(5) + " ¿Qué tal?")

# Si multiplicamos nuestra cadena por un entero, se imprimirá esas veces
print("Hola" * int(2.5 * 2))


### Operadores comparativos ###

print(3 > 4)    # x es mayor que y (falso)
print(3 < 4)    # x es menor que y (verdadero)
print(3 >= 4)   # x es mayor o igual que y (falso)
print(3 <= 4)   # x es menor o igual que y (verdadero)
print(3 == 4)   # x es igual a y (falso)
print(3 != 4)   # x es distinto que y (verdadero)

# También podemos combinar distintos operadores
print(3 > 2 == 2)    # 3 es mayor que 2 que es igual a 2

# Si comparamos cadenas, estas comparan ordenaciones alfabeticas
print('aola' <= 'bola') # aola es menor que bola? Si
print('zola' <= 'bola') # zola es menor que bola? No
print('aaaa' >= 'AAAA') # las ordenaciones también toman en cuenta las mayusculas, tomando en cuenta ASCII
print(len('hola') < len('holaaaa')) # también podemos comparar el largo de caracteres


### Operadores logicos ###

# Estos operadores se rigen bajo la logica booleana.
# En otros lenguajes la sintaxis podría ser conocida como:

# && = and
# || = or

# Casos de uso
print(3 > 4 and 'hola' > 'python') # Dos condicionales falsos
print(3 > 4 or 'hola' > 'python')  # Dos condicionales falsos
print(3 < 4 and 'hola' < 'python') # Dos condicionales verdaderos
print(3 < 4 or 'hola' < 'python')  # Dos condicionales verdaderos
print(3 < 4 and 'hola' > 'python') # Un condicional verdadero y uno falso
print(3 < 4 or 'hola' > 'python')  # Un condicional verdadero y uno falso
print(not(3 > 4))

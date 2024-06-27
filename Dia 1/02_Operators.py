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

print(3 > 4)
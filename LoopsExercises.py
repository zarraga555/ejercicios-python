#EL USO DE RANGE ES DE ESTA FORMA
# range(start , stop, step)
# start : Opcional. Un número entero que especifica en qué posición comenzar. El valor predeterminado es 0
# stop : Necesario. Un número entero que especifica en qué posición detenerse (no incluido).
# step : Opcional. Un número entero que especifica el incremento. El valor predeterminado es 1

#Ejercicio 1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# nombre = input('Introduce tu nombre: ')
# for i in range(10):
#   print(nombre)

#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# edad = int(input('Introduce tu edad: '))
# for i in range(edad):
#   print('Cumpliste ' + str(i + 1) + ' años')

#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese 
# número separados por comas.

# numero = int(input('Ingrese un numero entero: '))
# for i in range(numero):
#   result = i % 2
#   if result != 0:
#     print(i)

#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# number = int(input('Ingrese un numero positivo: '))
# for i in range(number, -1 , -1 ):
#   print(i, end=", ")

#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la 
# inversión cada año que dura la inversión.

# cantidad = float(input('Cantidad que invertira: '))
# interes = float(input('interes anual: '))
# años = int(input('Ingresa la cantidad de años: '))
# for i in range(años):
#   cantidad = cantidad * ( 1 + (interes / 100))
#   print('año ' + str(i+1) + ' ganado ' + str(round(cantidad, 2)))

#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# cantidad = int(input('Ingrese un numero enteero: '))
# for i in range(cantidad):
#   for j in range(i + 1):
#     print('*', end="")
#   print("")

#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# numero = int(input('Ingrese un numero entero a multiplicar: '))

# for i in range(11):
#   print(str(i) + ' x ' + str(numero) + ' = ' + str(i*numero))

#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

# n = int(input('Ingrese la altura del triangulo: '))
# for i in range(1, n + 1, 2):
#   for j in range(i, 0, -2):
#     print(j, end=" ")
#   print("")

#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# key = 'pass'
# contraseña = ''

# while contraseña != key:
#   contraseña = input('introduce tu contraseña: ')
# print('contraseña correcta')

#Ejercicio 10
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

# primo = int(input('Ingrese un numero entero: '))
# i = 2

# while primo % i != 0:
#   i += 1
# if i == primo:
#   print(str(primo) + ' es primo')
# else:
#   print(str(primo) + ' no es primo')

#Ejercicio 11
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

# palabra = input('Introduzca una palabra: ')
# for i in range(len(palabra)-1, -1, -1):
#   print(palabra[i])

#Ejercicio 12
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

# frase = input('Ingrese una frase: ')
# letra = input('Ingrese una letra: ')
# contador = 0
# for i in frase:
#   if i == letra:
#     contador += 1
# print('La letra ' + letra + ' aparece ' + str(contador) + ' veces en la frase: ' + frase)

#Ejercicio 13
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
  frase = input('Ingresa algo: ')
  if frase == 'salir':
    break
  print(frase)
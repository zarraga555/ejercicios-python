#Ejecicio 1
#Escribir un programa que muetre por pantalla
#la cadena Hola Mundo

# print('Hola Mundo!')

#Ejercicio 2
#Escribir un programa que almacene la cadena
# Hola mundo en una varibale y luego muestree por pantalla

# message = 'Hola Mundo'
# print(message)

#Ejercicio 3 
#Escribir un progrmama que pregunte el nombre del usuario
#en la consola y despues de que el usuario ño instroduxa por la pantalla la cadena
# Hola <variable>, donde <name> es el nombre que el usuario haya introducido

# name = input('Introduce tu nombre: ')
# print('Hola ' + name)

#Ejercicio 4
#Escribir un programa que pregnte el nombre del usuario en la consola y un numero entero
#e imprima por pantalla en lineas distintas el nombre del usuario tantas veces como el
#numero introducido

# names = input('Introduce tu nombre: ')
# a = input('Introduce un numero cualquiera: ')
# print((names + "\n") * int(a))

#Ejercicio 5
#Escribir un programa que pregunte el nombre del usuario en la consola y despues de que el 
#usuario lo introduzca muestre por pantalla <name> tiene <n> letras, donde <name> es el nombre
#de usurio en mayusculas y <n> es el numero de letras que tiene el nombre.

# name = input('Introduzca un nombre: ')
# print('El nombre: ' + name.upper() + ' tiene: '+ str(len(name)) + ' letras')

#Ejercicio 6
#Escribir un programa que realice la siguiente operación aritmética (3+2/2⋅5)2

# print(((3 + 2) / (2 * 5))**2)

#Ejercicio 7
#Escribir un programa que lea un entero positivo, , introducido por el usuario y 
#después muestre en pantalla la suma de todos los enteros desde 1 hasta . 
# La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = n(n + 1) / 2

# n = int(input('Ingresa un numero: '))
# result = (n * (n + 1) / 2)
# print(result)

#Ejecicio 9
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
# pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice 
# de masa corporal calculado redondeado con dos decimales.

# weight = float(input('Cual es tu peso en Kg?: '))
# height = float(input('Cual es tu estatura en metros?: '))
# imc = round(weight/(height)**2,2)
# print('Tu indice de masa corporal es de: ' + str(imc))

#Ejercicio 10
#Escribir un programa que pida al usuario dos números enteros y muestre por 
# pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> 
# son los números introducidos por el usuario, y <c> y <r> son el cociente 
# y el resto de la división entera respectivamente.

# a = input('Ingrese un numero para a: ')
# b = input('Ingrese un numero para b: ')

# print(a + ' entre ' + b + ' da un cociente ' + str(int(a) // int(b)) + ' y un resto ' + str(int(a) % int(b))) 

#Ejercicio 11
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión.
# cantidad = float(input('Cantidad a invertir?: '))
# interes = float(input('Interes porcentual anual?: '))
# years = int(input('Años?: '))

# capital = round((cantidad * (interes / 100 + 1)** years),2)
# print('capital final: ' + str(capital))

#Ejercicio 12
#Una juguetería tiene mucho éxito en dos de sus productos: 
# payasos y muñecas. Suele hacer venta por correo y la empresa 
# de logística les cobra por peso de cada paquete así que deben 
# calcular el peso de los payasos y muñecas que saldrán en cada 
# paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas 
# vendidos en el último pedido y calcule el peso total del 
# paquete que será enviado.

# peso_payaso = 112
# peso_muñeca = 75
# payasos = int(input('Introduce el numero de payasos a enviar: '))
# muñecas = int(input('Introduce el numero de muñecas a enviar: '))
# peso_total = peso_payaso * payasos + peso_muñeca * muñecas
# print('El peso total del paquete es : ' + str(peso_total))

#Practica 13
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece 
# el 4% de interés al año. Estos ahorros debido a intereses, que no se 
# cobran hasta finales de año, se te añaden al balance final de tu cuenta 
# de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
# depositada en la cuenta de ahorros, introducida por el usuario. Después el 
# programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el 
# primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

# inversion = float(input('Introduce la inversion inicial: '))
# intereses = 0.04
# balance1 = inversion * (1 + intereses)
# print('Balance tras el primer año: ' + str(round(balance1, 2)))
# balance2 = balance1 * (1 + intereses)
# print('Balance tras el segundo año: ' + str(round(balance2, 2)))
# balance3 = balance2 * (1 + intereses)
# print('Balance tras el tercer año: ' + str(round(balance3, 2)))

#Practica 14
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día 
# tiene un descuento del 60%. Escribir un programa que comience leyendo el 
# número de barras vendidas que no son del día. Después el programa debe mostrar 
# el precio habitual de una barra de pan, el descuento que se le hace por no ser 
# fresca y el coste final total.

barras = int(input('Introduce el numero de barras vendidas que no son frescas: '))
precio = 3.49
descuento = 0.6
coste = barras * precio * (1 - descuento)
print('El coste de una barra fres es ' + str(precio) + '$')
print('El descuneto sobre una barra no fresca es ' + str(descuento * 100) + '%')
print('El coste final a pagar es ' + str(round(coste, 2)) + '$')

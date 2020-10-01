#Ejercicio 1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
# edad = int(input('Inserta tu edad: '))

# if edad > 18:
#   print('Eres mayor de edad')
# else:
#   print('Eres menor de edad')

#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario 
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en 
# la variable sin tener en cuenta mayúsculas y minúsculas.

# contraseña = input('digita tu contraseña: ')
# password = 'hola'

# if contraseña == password:
#   print('Las contraseñas coiciden')
# else:
#   print('Las contraseñas son incorrectas')

#Ejercicio 3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

# numero = int(input('Ingrese un numero: '))
# divisor = int(input('ingrese un numero para el divisor: '))
# if divisor > 0:
#   result = numero / divisor
# else:
#   print('El divisor no puede ser 0')

#Ejercicio 4
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

# numero = int(input('Ingrse un numero entero: '))
# result = numero % 2
# if(result == 0):
#   print('El numero ' + str(numero) + ' es par')
# else:
#   print('El numero ' + str(numero) + ' es impar')

#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o 
# superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y 
# muestre por pantalla si el usuario tiene que tributar o no.

# edad = int(input('Ingrese su edad: '))
# ingresos = int(input('Ingrese sus ingresos: '))

# if edad > 16 and ingresos >= 1000:
#   print('Usted tiene que tributar')
# else:
#   print('Usted no debe tributar')

#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta 
# formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el 
# grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla 
# el grupo que le corresponde.

# name = input('Ingresa tu nombre: ')
# sexo = input ('Ingresa tu sexo (M o F): ')
# if sexo == 'F':
#   if name.lower() < 'm':
#     group = 'A'
#   else:
#     group = 'B'
# else:
#   if name.lower() > 'n':
#     group = 'A'
#   else:
#     group = 'B'

# print('Tu grupo es ' + group)

#Ejercicio 7
#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 200000€ y 35000€	20%
#Entre 350000€ y 60000€	30%
#Más de 60000€	45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

# renta = int(input('Ingresa su renta anual: '))
# if renta < 10000:
#   print('Su impositivo es de 5%')
# else:
#   if renta > 10000 and renta < 20000:
#     print('Su impositivo es de 15%')
#   else:
#     if renta > 20000 and renta < 35000:
#       print('Su impositivo es de 20%')
#     else:
#       if renta > 35000 and renta < 60000:
#         print('Su impositivos es de 30%')
#       else:
#         print('Su impositivo es de 45%')

#Ejercicio 8
#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación 
# comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados 
# pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla 
# con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada 
# por la puntuación del nivel.

#Nivel	Puntuación
#Inaceptable	0.0
#Aceptable	0.4
#Meritorio	0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

# bonificacion = 2400
# puntuación = float(input('Ingrrese la puntacion obtenida: '))
# if puntuación  == 0.0:
#   nivel = 'Inaceptable'
# else:
#   if puntuación >= 0.4 and puntuación < 0.6:
#     nivel = 'Aceptable'
#   else:
#     if puntuación >= 0.6:
#       nivel = 'Meritorio'

# print('Tu nivel de rendimiento es: ' + nivel)
# print('Te corresponde cobrar: ' + str(puntuación * bonificacion) + '$')

#Ejercicio 9
#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que 
# debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el 
# cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

# edad = int(input('Ingrese la edad: '))
# if edad <= 4:
#   print('El ingreso es gratis')
# elif edad > 4 and edad < 18:
#   print('El ingreso es de: 5$')
# else:
#   print('El ingreso es de : 10$')

#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes 
# disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar 
# por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

pizza = input('Que tipo de pizza quiere (V o N): ')
if pizza == 'V':
  print('La pizza vegetariana tiene estos ingredientes: Pimiento y Tofu')
else:
  print('La pizza normal tiene estos ingredientes: Peperoni, Jamon y Salmon')
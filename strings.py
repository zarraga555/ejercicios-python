myStr = "Hello World"

print(dir(myStr))

#concatenar
print('My name is '+myStr)
print(f'My name is {myStr}')
print('My name is {0}'.format(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("Hello", 'perro'))
print(myStr.count('l'))

print(myStr.startswith('hola'))
print(myStr.endswith('World'))

print(myStr.split('o'))
print(myStr.find('o'))

print(len(myStr))
print(myStr.index('e'))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])
print(myStr[3])
print(myStr[4])
print(myStr[-1])
print(myStr[-5])
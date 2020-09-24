demo_list = [1, 'hello', 1.34, True, [1,2,3]]
colors = ['red', 'green', 'blue']

numbers_list = list((1,2,3,4))
print(numbers_list)

r = list(range(1, 10))
print(r)
print(type(colors))
print(dir(colors))

print(len(demo_list))

print(colors[1])
print(colors[-1])

print('green' in colors)

print(colors)
colors[1] = 'Yellow'
print(colors)

colors.append('violet')
colors.extend(('violet', 'green'))

colors.insert(1, 'violet')
colors.insert(-1, 'blue')
colors.insert(len(colors), 'violet')

#Elimina un artibuto con ese nonbre
colors.remove('green')

print(colors)
#Elimina el ultimp de la lista o asignado la posicion
colors.pop()
#Limpia la lista
# colors.clear()

#Ordena la lista z-a
colors.sort(reverse=True)

#cuenta la cantidad del valor asignado existe
print(colors.count('red'))
print(colors)
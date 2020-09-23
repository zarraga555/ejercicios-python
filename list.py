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
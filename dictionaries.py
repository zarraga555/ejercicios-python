product = {
    'name':'book',
    'quantity': 3,
    'price': 4.99
}

person = {
    'first_name': 'Alberto',
    'lost_name': 'Zarraga'
}
print(dir(product))
print(type(product))

print(person.keys())
print(person.items())

print(person.clear())
print(person)

products = [
    {'name': 'book', 'price': 10.99},
    {'name': 'laptop', 'price': 1000}
]
print(products)
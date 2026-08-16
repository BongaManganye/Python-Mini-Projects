# Map fetch value from dict

people = [
    {
        'name': 'Foo',
        'phone': '123',
    },
    {
        'name': 'Bar',
        'phone': '456',
    },
    {
        'name': 'SnowWhite',
        'phone': '7-dwarfs',
    }
]

phones = map(lambda d: d['phone'], people)

print(phones)
print(list(phones))

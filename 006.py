#Write a generator capable of generating a sequence with the factorial from 1 to n,
#where n is passed as a parameter to the generator.

def factorial_generator(n):
    value = 1
    for element in range(1, n + 1):
        value *= element
        yield value

for n, factorial in enumerate(factorial_generator(5), 1):
    print(f"{n}! = {factorial}")

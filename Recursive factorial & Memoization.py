#Recursive factorial & Memoization
# Write a recursive function to compute the factorial of a number. Add a custom 
# decorator or dictionary cache to memoize previous results

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def factorial(n):
    if n <= 1 : return 1 
    return n *factorial(n - 1)

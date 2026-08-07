#Fibonacci Sequence Generator
#Generate and print a list containg the first n Fibonacci numbers, where n is provided by the user

def fib(n):
    if n <= 0: return[]
    if n == 1: return[0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

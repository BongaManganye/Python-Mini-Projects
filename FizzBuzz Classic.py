#FizzBuzz Classic
# Iterate numbers from 1 to 50. For multiples of, print "Fizz"; for multiples of 5,
# print "Buzz"; for multiples of both, print "FizzBuzz"; otherwise print the number

for i in range(1, 51):
    if i % 15 == 0: print("FizzBuzz")
    elif i % 3 == 0: print("fizz")
    elif i % 5 == 0: print("Buzz")
    else: print(i)

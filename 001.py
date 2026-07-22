#Write a function that takes a string and a list. The function must 
# compare the string passed with the elements of the list, which is
#  also passed as a parameter. Return True if the string is found 
# within the list; otherwise, return False

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(f"GCD of 10 and 5 --> {gcd(10,5)}")
print(f"GCD of 32 and 24 --> {gcd(32,24)}")
print(f"GCD of 5 and 3 --> {gcd(5,3)}")

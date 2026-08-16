# Two -Factor Authentication (2FA) Generator

import random

def generate_2fa_code():
    return random.randint(100000, 999999)

code = generate_2fa_code()
print(f"Your 2FA Code: {code}")

user_input = int(input("Enter the code: "))
if user_input == code:
    print("Access granted.")
else:
    print("Invalid code.")

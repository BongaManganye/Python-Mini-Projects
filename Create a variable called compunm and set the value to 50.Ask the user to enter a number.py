# Create a variable called compunm and set the value to 50.Ask the user to enter a number. 
# While their guess is not the same as the compnum value, tell them if their guess is too low or too high and ask 
# them to have another guess. If they enter the same value as compnum, display the message "Well done, you took [count] attempts"

compnum = 50
count = 0
num = int(input("Enter a number: "))

while compnum != num:
    print("Guess is too low  or low") 
    num = int(input("Enter another number: "))
    count = count + 1
    if compnum == 50:
        print(f"Well done, you took {count} attempts")

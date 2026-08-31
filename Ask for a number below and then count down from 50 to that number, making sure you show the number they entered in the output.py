# Ask for a number below and then count down from 50 to that number, making sure you show the number they entered in the output

num1 = int(input("Enter number below 50 "))

for i in range(10, num1-1, -1):
    print(i)

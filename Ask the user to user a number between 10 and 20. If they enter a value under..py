#Ask the user to user a number between 10 and 20. If they enter a value under 
#Display the message "Too low" and ask them to try again. If they enter a a value above 20,
#Display  the message "Too high" and ask them to try again. Keep repeating this until they 
#Enter a value that is between 10 and 20 and then display the message "Thank you".

num = int(input("Enter number between 10 and 20: "))
while num < 10 or num > 20:
    if num < 10:
        print("Too low")
    else:
        print("Too high")
        num = int(input("Try again"))
print("Thank you!")

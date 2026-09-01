# Ask the user to enter a number between 10 and 20. If they enter a value under 10,
# dsiplay the message "Too low " and ask them to try again. If they enter a value above 20, display the message "Too high"
# and ask them to try again. Keep repeating this until they enter a value that is between 10 and 20 and then display the message "Thank you".

num = input("Enter a number between 10 and 20.")

if num < 10:
    print("Too low")
    again = input("Enter a number again")
    if num > 20:
        print("Too high")
        again = input("Enter a number again")
        

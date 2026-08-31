# Ask how many people the user wants to to invite to a party. If they enter a number below
# 10, ask for the names and after each name display "[name] has been invited". If they 
# enter a number which is 10 or higher, display the message "Too many people".

user = int(input("Enter the number of users: "))

if user < 10:
    name = input("Enter name")
    print(f"{name} has been invited:  ")
elif user > 10:
    print("Too many people")   

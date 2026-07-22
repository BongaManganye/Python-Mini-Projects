#Write a function that receives a string with the valid options to accept (each option is
#a letter). Convert valid options to lowercase letters. Use input to read an option,
#convert the value to lowercase letters, and verify that the option is valid. In the case of
# an invalid option, the function must ask the user to re-enter another option

def validate_input(message, valid_options):
    options = valid_options.lower()
    while True:
        choice = input(message)
        if choice.lower() in options:
            break
        print("Error: invalid option. Please try again.\n")
    return choice

print(validate_input("Choose an option:", "abcde"))

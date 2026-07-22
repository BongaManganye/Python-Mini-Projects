#Write a function that receives a string with the valid options to accept (each option is
#a letter). Convert valid options to lowercase letters. Use input to read an option,
#convert the value to lowercase letters, and verify that the option is valid. In the case of
#an invalid option, the function must ask the user to re-enter another option.

def validate_options(valid_options):
    valid_options = valid_options.lower()
    while True:
        option = input("Enter an option:").lower()
        while True:
            option = input("Enter an option:").lower()
            if option in valid_options:
                return option
            print("Invalid option, please choose again.")

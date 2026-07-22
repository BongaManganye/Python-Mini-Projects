#Modify Program 8.26 to receive two optional parameters. One is to indicate the
#character to print before the number, with white space being the default value. The
#second optional parameter is how many characters to add per level, with 2 as the
#default value

def print_lists(values, level=0, character=" ", increment=2):
    for x in values:
        if isinstance(x,int):
            print(f"{character * (level * increment)}{x}")
        else:
            print_lists(x, level + 1, character, increment)

print_lists([1, 2, 3, [4, 5, 6, [7, 8, 9]], 10], character="*",increment=2)

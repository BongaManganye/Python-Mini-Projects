#Write a function that takes a string and a list. The function must compare the string
#passed with the elements of the list, which is also passed as a parameter. Return True
#if the string is found within the list; otherwise, return False

def search_string(s, list_to_search):
    return s in list_to_search

L = ["AB", "CD", "EF", "FG"]

print(search_string("AB", L))
print(search_string("CD", L))
print(search_string("EF", L))
print(search_string("FG", L))
print(search_string("XYZ", L))

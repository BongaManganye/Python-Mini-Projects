# Second Largest Element
# Given a list of numbers, find the second largest unique number without sorting the entire list using built-in
# sort methods (or handle it efficiently)

def second_largest(lst):
    unique = set(lst)
    if len(unique) < 2: return None
    unique.remove(max(unique))
    return max(unique)

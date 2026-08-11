# Invert a Dictionary
# Write a function that takes a dictionary and returns a new dictionary where keys become values and values
# become keys. Handle potential duplicates values by grouping them into lists

def invert_dict(d):
    inverted = {}
    for k,v in d.items():
        inverted.setdefault(v, [].append(k))
    return inverted

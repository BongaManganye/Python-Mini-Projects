#Flatten Nested List
# Write a recursive function that takes a deeply nested list containing integers and lists, and flattens it into a single 1D list

def flatten(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

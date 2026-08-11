#Common Elements in Three Lists
# Given three lists of integers, find all elements that appear in all three using set intersection

def common_elements(l1, l2, l3):
    return list(set(l1) & set(l2) & set(l3))

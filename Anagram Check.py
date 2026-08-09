#Anagram Check
#Write a function that checks if two strings are anagrams of each other(contain exact same characters with same frequencies)

from collections import Counter

def is_anagram(s1, s2):
    clean1 = s1.replace(" ","").lower()
    clean2 = s2.replace(" ","").lower()
    return Counter(clean1) == Counter(clean2)

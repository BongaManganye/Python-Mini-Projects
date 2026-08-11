# Unique Vowel Finder
# Given a text string, use set operations to identify which vowels(a, e, i, o, u) are present in the text and which
# are missing

def check_vowels(text):
    vowels = set("aeiou")
    text_vowels = set(text.lower()) & vowels
    missing = vowels - text_vowels
    return text_vowels, missing

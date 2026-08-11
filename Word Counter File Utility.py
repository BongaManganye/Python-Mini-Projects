# Word Counter File Utility
# Write a function that reads a text file, count the total number of lines, words and characters, and handles
# FileNotFoundError safely

def analyze_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()
            words = content.split()
            chars = len(content)
            return len(lines), len(words), chars
    except FileNotFoundError:
        return "File not Found"

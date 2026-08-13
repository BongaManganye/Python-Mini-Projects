# Count Characters

text = """My name is Bonga and I am a University student, now I am coding"""

#print(text)
count = {}

for char in text:
    if char == '\n':
        continue
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1

for key in sorted(count.keys()):
    print("'{}' {}".format(key, count[key]))

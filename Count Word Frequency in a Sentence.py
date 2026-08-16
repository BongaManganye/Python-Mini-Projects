#Count Word Frequency in a Sentence

sentence = "Python is great and Python is fun"
words = sentence.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1
 
print(word_count)

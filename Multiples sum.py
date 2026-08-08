#Multiples sum
#Find the sum of all integers between 1 and 1000 (inclusive) that are multiples of 3 or 5

total = sum(i for i in range(1, 1001) if i % 3 == 0 or i % 5 == 0)
print(total)

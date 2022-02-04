# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

s = 'azcbobobegghakl'
total = 0

for letter in range(0, len(s)):
    if (s[letter:letter+3] == 'bob'):
        total += 1
        
print('Number of times bob occurs is: ' + str(total))
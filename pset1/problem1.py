# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

s = 'azcbobobegghakl'
vowels = 0

for letter in range(0, len(s)):
    if (s[letter] == 'a' or s[letter] == 'e' or s[letter] == 'i' or s[letter] == 'o' or s[letter] == 'u'):
        vowels += 1
        
print('Number of vowels: ' + str(vowels))
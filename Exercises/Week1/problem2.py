total = 0

for letter in range(0, len(s)):
    if (s[letter:letter+3] == 'bob'):
        total += 1
        
print('Number of times bob occurs is: ' + str(total))
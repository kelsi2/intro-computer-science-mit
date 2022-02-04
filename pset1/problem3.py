# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

s = 'abcbcd'
# Create empty string to hold alphabetical substring
alphaString = ''
# Track temporary string
tempAlphaString = ''

# Iterate over s
for letter in range(len(s) - 1):
    # Compare neighbours
    # if neighbour1 <= neighbour2
    if s[letter] <= s[letter + 1]:
        # Substring is in alphabetical order
        # Store that value
        if tempAlphaString == '':
            tempAlphaString = s[letter] + s[letter + 1]
        else:
            tempAlphaString += s[letter + 1]
        # Is current substring longer than previous one
        if len(tempAlphaString) > len(alphaString):
            # Remember that
            alphaString = tempAlphaString
    # Else you don't have an alphabetical substring so get rid of your current alphabetical substring
    else:
        tempAlphaString = ''
    if alphaString == '':
        alphaString = s[0]
# Print the result
print('Longest substring in alphabetical order is: ' + alphaString)
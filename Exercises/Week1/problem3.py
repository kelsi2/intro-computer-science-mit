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
# In this problem, you'll create a program that guesses a secret number!

# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

print('Please think of a number between 0 and 100!')

high = 100
low = 0

while True:
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + '?')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ans == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
    elif ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess
    else:
        print('Sorry, I did not understand your input.')
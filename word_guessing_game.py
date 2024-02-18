import random

# list of words
words = ['python', 'programming','computer','science','machine','learning','mathematics','physics','random']

# randomly choose a word
secret_word = random.choice(words)

# initialize variables
guesses = ''
wrong_guesses = 0
max_guesses = len(secret_word)

# display welcome message
print('Welcome to the word guessing game!')
print(f'Your word is of {len(secret_word)} letters')

# game loop
while wrong_guesses <= max_guesses:
    
    # diplay current progress
    display_word = ''
    for c in secret_word:
        if char in guesses:
            display_word = display_word + char
        else:
            display_word = display_word + '_'
    print(f"Guess the word: {display_word}")
    
    # get the user guess
    guess = input('Enter your guess (single letter): ').lower()
    
    # check if guess is correct
    if guess in secret_word:
        guesses += guess
        print('Correct!')
    else:
        wrong_guesses += 1
        print(f'You have {max_guesses-wrong_guesses} guesses left')
    
    # check if word is guessed or not
    
    if display_word == secret_word:
        print(f'Congratulations! You have guesses the word: {secret_word}')
        break
    
# End of game message
if wrong_guesses == max_guesses:
    print(f'Sorry, you ran out of guesses. The word was: {secret_word}')

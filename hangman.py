import random
words = ['cat', 'dog', 'elephant', 'tiger', 'wolf', 'lion','giraffe', 'zebra']
guess_limit = 5
random_word = random.choice(words)
hidden_word = ['_'] * len(random_word)
print('The word you need to guess has ' + str(len(random_word)) +' letters')

while guess_limit > 0:
    print(hidden_word)
    print('You have ' + str(guess_limit) + ' guesses left')
    question = input('Do you want to guess the word? (type y for yes)')
    if question.lower() == 'y':
        final = input('Your final answer: ')
        if final.lower() == random_word:
            print('Congratulations! You won!')
            break
    else:
        letter_guess = input('Enter a letter: ')
        if len(letter_guess) == 1:
            n = len(random_word) - 1
            while n >= 0:
                if letter_guess.lower() == random_word[n]:
                    print('Nice job! This letter is in the word')
                    hidden_word[n] = letter_guess.lower()
                n -= 1
                
            if letter_guess not in random_word:
                print('Sorry that letter is not in the word')
        else:
            print('You wrote more than 1 letter')
    
    guess_limit -= 1

if guess_limit == 0:
    print('You don\'t have any more guesses left')
    final1 = input('Your final guess is: ')
    if final1.lower() == random_word:
        print('Congratulations! You won!')
    else:
        print('Sorry, you just hanged the hangman. You lost! The word was ' + random_word)
    
                  
            
#Task 3
# Question 1:Guess the number
import random
computer_guess = random.randint(1,5)
#print('Computer guess is',computer_guess)
while True:
    user_guess = int(input('Enter user guess:' ))
    if user_guess > computer_guess:
        print('Guess is too high')
    elif user_guess < computer_guess:
        print('Guess is too low')
    else:
        print('Guess is right')
        break   

#Question 2:word scramble
#import random
words = ['python','javascript','java','automation','pytest','guvi','selenium']
chosen_word = random.choice(words)
#print('Chosen word is:',chosen_word)
word_list=list(chosen_word)
random.shuffle(word_list)
scrambled_word=''.join(word_list)
print('unscramble word',scrambled_word)
while True:
    guessed_word=input('Guess the word', )
    if guessed_word != chosen_word:
        print('Try again')
    else:
        print('Your guess is right')
        break

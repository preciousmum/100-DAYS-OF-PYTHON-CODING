'''Psueocode'''
 
#Step 1

word_list = ["ardvark", "baboon", "camel"]

'''todo-1 Randomly choose  word from the word_list and
assign it to a variable called chosen_word.'''
import random
chosen_word = random.choice(word_list)
#print(chosen_word)

'''todo-2 Ask the user to guess a letter and assign their answer to a variable
called guess. Make guess lowercase'''

guess = input("Guess a random letter: ").lower()
#print(guess)

'''todo-3 Check if the letter the user guessed(guess) is on of the letters in the chosen_word'''
'''
MY CODE
if guess in chosen_word:
    print ("true")
else:
    print("fasle")'''

# ANGELA'S CODE
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")
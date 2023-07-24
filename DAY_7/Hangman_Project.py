'''Psueocode'''
 
#Step 1

word_list = ["ardvark", "baboon", "camel"]

'''todo-1 Randomly choose  word from the word_list and
assign it to a variable called chosen_word.'''
import random
chosen_word = random.choice(word_list)

# code check
# print(chosen_word)
# Challenge 2 todo -01 create an empty list called display


display = []

# for each letter in chosen word, add a "_ " to "display"
# My codel
for i in chosen_word:
    display.append("_")
print(display)

# # # ANGELA'S CODE
# for letter in chosen_word:
#     display += "_"
# print(display)

# # #ANGELA'S CODE 2
# # instead of letter she used an underscore, but it doesn't really matter
# for letter in range(len(chosen_word)):
#     display += "_"
# print(display)


'''todo-2 Ask the user to guess a letter and assign their answer to a variable
called guess. Make guess lowercase'''

guess = input("Guess a random letter: ").lower()
#print(guess)

''' todo -2.1 Loop through each position in the chosen_word if the letter at thata
position matches 'guess' then reveal hat letter in the display at that position'''

# My code
# Review List and manipulating list
# In other to do this, you need to learn how to replace item in a list
''' The for loop must used the range function so you can get the position of the letter in the list 
because you can't slice string in list it must have an integer index '''

for position in range(len(chosen_word)):
    # Getting hold of the letter in the chosen word
    letter = chosen_word[position]
    if letter == guess:
        # getting hold of the display
        display[position] = letter
print(display)





'''todo-3 Check if the letter the user guessed(guess) is on of the letters in the chosen_word'''
'''
MY CODE
if guess in chosen_word:
    print ("true")
else:
    print("fasle")'''

# ANGELA'S CODE
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("wrong")
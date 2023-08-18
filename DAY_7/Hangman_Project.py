'''Psueocode'''
 
#Step 1

from hangman_word import word_list
from hangman_art import stages,logo


'''todo-1 Randomly choose  word from the word_list and
assign it to a variable called chosen_word.'''
import random

print(logo)
chosen_word = random.choice(word_list)

# Todo Create a variable called lives to keep track of the number of lives
lives = 6

# code check
# print(chosen_word)
# Challenge 2 todo -01 create an empty list called display


display = []

# for each letter in chosen word, add a "_ " to "display"
# My code
for i in chosen_word:
    display.append("_")
print(display)

# # # ANGELA'S CODE
# for letter in chosen_word:
#     display += "_"
# print(display)

# # #ANGELA'S CODE 2
# # instead of letter she used an underscore, but it doesn't really matter
# for _ in range(len(chosen_word)):
#     display += "_"
# print(display)


end_of_game = False
while not end_of_game:

    guess = input("Guess a random letter: ").lower()
    #print(guess)

    ''' todo -2.1 Loop through each position in the chosen_word if the letter at thata
    position matches 'guess' then reveal hat letter in the display at that position'''

    # My code
    # Review List and manipulating list
    # In other to do this, you need to learn how to replace item in a list
    ''' The for loop must used the range function so you can get the position of the letter in the list 
    because you can't slice string in list it must have an integer index '''

    if guess in display:
        print(f"You have already guess {guess}")

    for position in range(len(chosen_word)):
        # Getting hold of the letter in theE chosen word
        letter = chosen_word[position]
        if letter == guess:
            # getting hold of the display
            display[position] = letter
    # print(display)

    if guess not in chosen_word:
      print(f"{guess} is not in chosen word, You loose a life")
      lives -= 1
      print(f"You have {lives} left")
      if lives == 0:
          end_of_game = True
          print("Hahaha You loose")
          print(f"The word is {chosen_word}")
      
    # Joining all elements of the list and turning it into a display to print out the filled in blanks
    print(f"{' '.join(display)}")





    # checking for blanks in display to stop the code
    if "_" not in display:
        end_of_game = True
        print("You win ")
    
    print(stages[lives])




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
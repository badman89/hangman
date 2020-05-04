# /bin/python3
import random
import time
import re
import os
import sys
import subprocess as sp

#backing music using try as its an external module
try:
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    from pygame import mixer

    mixer.init()
    mixer.music.load("tune.mp3")
    mixer.music.play()
except:
    pass

#clear the terminal\

sp.call('clear', shell=True)


#define all functions
# function to randomly select a word from the list, convert it into a list of characters

def selectWord():
    wordsfile = open("words.txt", "r")
    lines = wordsfile.read().splitlines()
    word = list(random.choice(lines))

    return word

# user input sanitation

def inputcheck(guess, array, wrong):

    if len(guess) != 1:

        print("\njust 1 letter at a time please!\n")

        return False

    if not guess.isalpha():

        print("\nletters only please!\n")
        return False

    if not guess.islower():

        print("\nlowercase only please!\n")
        return False

    if guess in array:

        print("\nletter already guessed, choose another...\n")
        return False

    if guess in wrong:

        print("\nletter already guessed, choose another...\n")
        return False
    else:

        return True


# function to check if the chosen letter is in the word and return true/false and index of letter in the list

def checkchar(char, word):
    if char in word:

        result = "yes"
        #list comprehension for regexing the position of the letter in the word
        position = [i for i, item in enumerate(word) if re.search(char, item)]

    else:

        position = [i for i, item in enumerate(word) if re.search(char, item)]
        result = 'no'

    return result, position

# function to update positional letter array

def updatearray(array, position, guess):

    #debug : print(array,position,guess)
    position = position[0]

    array[position] = guess
    return array

#function for storing the hangman graphics

def hanged(lives):

    if (lives == 8):
        print("_________")
        print("|	 ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    if (lives == 7):
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    if (lives == 6):
        print("_________")
        print("|	 |")
        print("|        O")
        print("|")
        print("|")
        print("|")
        print("|________")
    if (lives == 5):
        print("_________")
        print("|	 |")
        print("|        0")
        print("|        |")
        print("|")
        print("|")
        print("|________")
    if (lives == 4):
        print("_________")
        print("|	 |")
        print("|        0")
        print("|        |/")
        print("|")
        print("|")
        print("|________")
    if (lives == 3):
        print("_________")
        print("|	 |")
        print("|        0")
        print("|       \|/")
        print("|      ")
        print("|")
        print("|________")
    if (lives == 2):
        print("_________")
        print("|	 |")
        print("|        0")
        print("|       \|/")
        print("|        |")
        print("|")
        print("|________")
    if (lives == 1):
        print("_________")
        print("|	 |")
        print("|        0")
        print("|       \|/")
        print("|        |")
        print("|       /")
        print("|________")
        print("\nLast Chance !!!!")
#function for the end of the game giving a choice to restart

def endgame(word, death):
    try:
        from pygame import mixer

        mixer.init()
        mixer.music.load("hadouken.mp3")
        mixer.music.play()
    except:
        pass
    sp.call('clear', shell=True)
    print(death)
    time.sleep(2)
    sp.call('clear', shell=True)
    print("The answer was", end="")
    print(word)
    print("\n YOU LOST TRY AGIAN?...")
    choice = input("Y/N :")
    if choice == "y":
        os.execl(sys.executable, sys.executable, *sys.argv)
    if choice == "n":
        exit()
    else:
        endgame(word, death)

def win(word):
    try:
        from pygame import mixer

        mixer.init()
        mixer.music.load("ff.mp3")
        mixer.music.play()
    except:
        pass
    print("\n CONGRATULATIONS YOU WON TRY AGIAN?...")
    choice = input("Y/N :")
    if choice == "y":
        os.execl(sys.executable, sys.executable, *sys.argv)
    if choice == "n":
        exit()
    else:
        win(word)
# define global vars
# run word selection function returning a random selection word 5 chars and above
word = selectWord()
# define lives counter
lives = 8
#define score to enable winning
score = 0
#define list of wrongly chosen characters
wrong = [""]
#initialize correctly chosen letter array
array = []
# death
death = ("""
                                           .----.._
                                           []      `'--.._
                                           ||__           `'-,
                                         `)||_ ```'--..       \
                     _                    /|//}        ``--._  |
                  .'` `'.                /////}              `\/
                 /  .'''.\              //{///    
                /  /_  _`\\            // `||
                | |(_)(_)||          _//   ||
                | |  /\  )|        _///\   ||
                | |L====J |       / |/ |   ||
               /  /'-..-' /    .'`  \  |   ||
              /   |  :: | |_.-`      |  \  ||
             /|   `\-::.| |          \   | ||
           /` `|   /    | |          |   / ||
         |`    \   |    / /          \  |  ||
        |       `\_|    |/      ,.__. \ |  ||
        /                     /`    `\ ||  ||
       |           .         /        \||  ||
       |                     |         |/  ||
       /         /           |         (   ||
      /          .           /          )  ||
     |            \          |             ||
    /             |          /             ||
   |\            /          |              ||
   \ `-._       |           /              ||
    \ ,//`\    /`           |              ||
     ///\  \  |             \              ||
    |||| ) |__/             |              ||
    |||| `.(                |              ||
    `\\` /`                 /              ||
       /`                   /              ||
 jgs  /                     |              ||
     |                      \              ||
    /                        |             ||
  /`                          \            ||
/`                            |            ||
`-.___,-.      .-.        ___,'            ||
         `---'`   `'----'`' \
                        """)

# begin the game

print("WELCOME TO HANGMAN GAME!")

#initialise the _ array for the letters
for i in word:

    array.append("_")
#start the game loop

while lives > -1:
    #check lives counter for losing the game
    if lives == 0:
        endgame(word,death)
    #check the score for winning
    if score == len(word):
        win(word)
    #print the hangman graphic
    hanged(lives)
    #print how many lives left
    print("\nyou have " + str(lives) + " lives remaining")
    # print array of characters guessed correctly
    print("\nletters already chosen:   ", end="")
    print(array)
    #print list of wrongly guessed letters
    print("\nwrong guesses:  ", end="")
    print(wrong)
    # get guess
    guess = input("\nchoose a letter: >")
    #clear screen
    sp.call('clear', shell=True)

    #send guess to the input check function

    inputstatus = inputcheck(guess,array,wrong)

    # if pass sanitization send guess to check character function
    if inputstatus is True:

        result = checkchar(guess, word)[0]
        position = checkchar(guess, word)[1]
        if result == "yes":

            print("\nyes that letter is in the word\n")
            array = updatearray(array, position, guess)
            score = score + 1

        else:

            print("\nno that letter is not in the word\n")
            lives = lives - 1
            wrong.append(guess)
            # letterArray()

    else:

        continue

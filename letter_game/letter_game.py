
import os
import random
import sys

word_list=[]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add_word():
    while True:     
        word = str(input("Add word to game(q to stop) >>> "))
        if not word.lower() == "q":
            word_list.append(word)
        else:
            break
        
def draw(misses, hits, secret_word):
    clear()

    print("Misses: {}/7".format(len(misses)))
    print('')

    for letter in misses:
        print(letter, end=' ')
    print('\n\n')
        
    for letter in secret_word:
                if letter in hits:
                    print(letter, end = ' ')
                else:
                    print("_", end = ' ')
    print('')
        
def get_guess(misses, hits):
        while True:
            guess = input("Guess a letter >>> ").lower()
        
            if len(guess) != 1:
                print("Only one letter allowed. Try again")               
            elif guess in misses or guess in hits:
                print("You already guessed this letter. Try again")            
            elif not guess.isalpha():
                print("Only letters allowed")                
            else:
                return guess

def play(done):
    clear()
    secret_word = random.choice(word_list)
    misses = []
    hits = []

    while True:
        draw(misses, hits, secret_word)
        guess = get_guess(misses, hits)

        if guess in secret_word:
            hits.append(guess)
            found = True
            for letter in secret_word:
                if letter not in hits:
                    found = False           
            if found:
                print("You win!")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            misses.append(guess)
            if len(misses) == 7:
                draw(misses, hits, secret_word)
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True
        if done:
            play_again = input("Play again(Y/n) >>> ").lower()
            if play_again != 'n':
                return play(done = False)
            else:
                sys.exit()
                
def welcome():
    start = input("Press enter to start or Q to quit ").lower()
    if start == 'q':
        print("bye!")
        sys.exit()
    else:
        return True
        
print('Welcome to Letter Guess!')

done = False

while True:
    clear()
    add_word()
    welcome()
    play(done)
    
    

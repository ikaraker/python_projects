import random

play_again = True
LOWER = 1
UPPER = 20
MAX_TRIES = 5

def display_init(lower_bound, upper_bound, tries):
    print("-" * 30)
    print("Welcome to this exciting mini game")
    print("Guess the lucky number")
    print("Pick from {} to {}".format(lower_bound, upper_bound))
    print("You have {} shots".format(tries))
    print("-" * 30)

def get_player_input():
    print("Choice #{}".format(MAX_TRIES+1-tries))
    try:
        user_guess=int(input("Enter number > "))
    except ValueError:
        print("This is not a legal value, try again please.")
        return False
    else:
        return user_guess


def check_bounds(user_input):
    if user_input > UPPER:
       print("Oooops, number is out of bounds, choose another...")
       return 0
    elif user_input < LOWER:
        print("Oooops, number is out of bounds, choose another...")
        return 0
    else:
        return 1

def check_guess(validated_user_input, limit):
        if validated_user_input != num_to_guess and limit == 0:
            print("Sorry, you lost... number to guess was {}, better luck next time".format(num_to_guess))
            return False
        elif validated_user_input > num_to_guess and limit != 0:
            print("Try a smaller number")
            return False
        elif validated_user_input < num_to_guess and limit != 0:
            print("Try a larger number")
            return False
        else:
            print("Well done!!! You guessed the secret number {} in {} tries!".format(num_to_guess,len(guess_list)))
            return True
            

def prompt_to_play():
        play = ""
        while play != "yes" and play != "no":
            play = input("Play again (yes/no) > ")
            if play == "yes":
                return True
            if play == "no":
                return False
        


while play_again == True:
    num_to_guess = random.randint(LOWER, UPPER)
    guess_list = []
    display_init(LOWER,UPPER,MAX_TRIES)
    tries = MAX_TRIES
    while tries != 0:
        print("-" * 30)
        print("Guess List > {}".format(guess_list))
        choice=get_player_input()
        if choice == False:
            continue
        check = check_bounds(choice)
        if check == 1:
            if not choice in guess_list:
                tries-=1
                guess_list.append(choice)
                guess = check_guess(choice, tries)
                if guess == True:
                    break    
            else:
                print("Number already chosen before...try another")
                continue
            
        
    play_again = prompt_to_play()


import random, sys
CREATOR = 'David Garcia'


def start_game_normal():
    
    the_solution = random.randint(1, 100)
    attempts = 1

    while True:
        try:
            user_number = int(input("Please give me a number between 1 and 100: \n"))
        except ValueError:
            print("You must enter a number please.\n")
            continue
            
        if user_number > the_solution:
            print("The number your looking for is lower!\n")
            attempts += 1
        elif user_number < the_solution:
            print("The number your looking for is higher!\n")
            attempts += 1
        elif user_number == the_solution:
            print("It looks like you got the right number!")
            print("Your attemps: ({})".format(attempts))
            break  

            
            
            
            
def start_game_hard():
    
    the_solution = random.randint(1, 100)
    attempts = 1
    print("Remember you only get 10 TRIES!!!\n")
    while True:
        try:
            user_number = int(input("Please Give me a number between 1 and 100: \n"))
        except ValueError:
            print("You must enter a number please\n")
            continue
        if attempts >= 10:
            print("Your attempts: {} \n".format(attempts))
            sys.exit("You Lose! (Game Over)\n")
        elif user_number > the_solution:
            print("The number your looking for is lower!\n")
            print("Your attempts: ({})".format(attempts))
            attempts += 1
        elif user_number < the_solution:
            print("The number your looking for is higher!\n")
            print("Your attempts: ({})".format(attempts))
            attempts += 1
        elif user_number == the_solution:
            print("You Win! You got the right number!")
            print("Your attempts: ({})".format(attempts))
            break
            
            
            
def asked_name():
    while True:
        user_name = input("Please enter your name to start: \n")
        if user_name.isalpha():
            print("Hello and welcome, {}!".format(user_name))
            return user_name
        else:
            print("Please type in your name only!\n") 
            
            
            
            
                        
            
#******(program begins here)******            
            
print("Hello and welcome, you will be playing a gussing number game!\n")            
asked_name()

print("Would you like to play on Normal or Hard mode?\n")

while True:
    difficulty = input("Please select Game mode: Normal/Hard: \n")
    if difficulty.lower() == "normal":
        start_game_normal()
        break
    elif difficulty.lower() == "hard":
        start_game_hard()
        break
        
        
print("-"*20)
print("Thank you for playing!\n")
print("This program was made by: {}\n".format(CREATOR))


while True:
    replay = input("Would you like to play again?: Yes/No: \n")
    if replay.lower() == "yes":
        mode = input("Choose your mode: Normal/Hard: \n")
        if mode.lower() == "normal":
            start_game_normal()
        elif mode.lower() == "hard":
            start_game_hard()
    elif replay.lower() == "no":
        sys.exit("Thank you for playing and have a nice day!\n")
    

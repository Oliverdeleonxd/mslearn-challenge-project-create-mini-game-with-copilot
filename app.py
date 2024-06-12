
import random

options = ["rock", "paper", "scissors"]

player_wins = 0
computer_wins = 0

def play_game():
    while player_wins < 3 and computer_wins < 3:    
        print("options:  1 = rock , 2 = paper , 3 = scissors")
        choose = input("Enter an option: ")
        option = int(choose)
        computer_option = get_computer_option()
        
        if  option > 0 and option < 4:
            options[option-1]
            get_round_winner(options[option-1], computer_option)
            print("chosed: " + options[option-1] + " vs " + computer_option)
            print("player wins: " + str(player_wins) + " computer wins: " + str(computer_wins))
            
        else:
            print("Invalid option")
            return play_game()
    else: 
        resert_game()

    
def get_computer_option():
    number = random.randint(1, 3)-1
    return options[number]
    
def get_round_winner(player_option, computer_option):
    global player_wins
    global computer_wins
    if player_option == computer_option:
        print("Tie")
    elif player_option == "rock" and computer_option == "scissors":
        print("Player wins")
        player_wins+=1
    elif player_option == "scissors" and computer_option == "paper":
        print("Player wins")
        player_wins+=1
    elif player_option == "paper" and computer_option == "rock":
        print("Player wins")
        player_wins+=1
    else:
        print("Computer wins")
        computer_wins+=1

    
def resert_game():
    choose = input("Do you want to play again? y/n: ")
    if choose == "y":
        global player_wins
        global computer_wins
        player_wins = 0
        computer_wins = 0
        play_game()
    elif choose == "n":
        exit()
    else:
        print("Invalid option")
        resert_game()


play_game()


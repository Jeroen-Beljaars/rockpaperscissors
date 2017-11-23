#Rock Paper Scissors
import random

def game():
    print("This is a rock paper scissors game!")

    #ask user to choose rock paper or scissors
    user_pick = input("Please choose Rock, paper or scissors!\n" +
                      "> ").lower()

    #the bot wil choose rock paper or scissors                
    bot_pick = random.randint(1,3)
    if bot_pick == 1:
        bot_pick = "rock"
    elif bot_pick == 2:
        bot_pick = "paper"
    else:
         bot_pick = "scissors"

    #check the outcome
    if user_pick == bot_pick:
        print("It's a tie!")
    elif user_pick == "rock":
        if bot_pick == "paper":
            print("Bot chose paper you lose")
        else:
            print("Bot chose {} you win!".format(bot_pick))
    elif user_pick == "paper":
        if bot_pick == "scissors":
            print("You chose scissors, you lose")
        else:
            print("Bot chose {}, you win!".format(bot_pick))
    elif user_pick == "scissors":
        if bot_pick == "paper":
            print("Bot chose paper you win!")
        else:
            print("Bot chose {}, you lose!".format(bot_pick))

    #if completed ask the player if he/she want's to play agian        
    play_again()

def play_again():
    #play again y/n
    play_again = input("\nDo you want to play again? (Y/n) ")
    if(play_again == "y" or
       play_again == "yes"):
       print()
       game()
    else:
        print("Good bye!")

game()
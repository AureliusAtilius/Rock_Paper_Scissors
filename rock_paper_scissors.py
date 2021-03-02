#!/usr/bin/env python3

import random

hands= ["rock","paper","scissors"]
game= True
wins= 0
losses=0
#start game
while game == True:
    #player chooses rock, paper, or scissors
    hand = input("Rock, Paper, Scissors, Shoot!\n")
    #ask again if choice is invalid
    if hand.lower() not in hands:
        continue

    #computer gets a random choice
    computer_hand = hands[random.randint(0,2)]

    #compare player vs computer hand

    if hand.lower() == "rock" and computer_hand == "rock":
        print("Draw")
        pass
    elif hand.lower() == "rock" and computer_hand == "paper":
       print("Paper beats Rock!")
       losses+=1
    elif hand.lower() == "rock" and computer_hand == "scissors":
        print("Rock beats Scissors")
        wins +=1
    elif hand.lower() == "paper" and computer_hand == "rock":
        print("Paper beats Rock!")
        wins +=1
    elif hand.lower() == "paper" and computer_hand == "paper":
        print("Draw")
        pass
    elif hand.lower() == "paper" and computer_hand == "scissors":
        print("Scissors beats Paper!")
        losses+=1
    elif hand.lower() == "scissors" and computer_hand == "rock":
        print("Rock beats Scissors!")
        losses +=1
    elif hand.lower() == "scissors" and computer_hand == "paper":
        print("Scissors beats Paper!")
        wins+=1
    elif hand.lower() == "scissors" and computer_hand == "scissors":
        print("Draw")
        pass

    #after comparison print score
    print("Player: {}, Computer: {}".format(wins,losses))


    #ask if you want to play again
    play_again=True
    responses=["Yes","yes","y","Y","No","no","n","N"]
    answer= " "

    #ask again if answer is invalid
    while answer not in responses:
        answer= input("Would you like to play again?")

    if answer in responses[4:7]:
        print("Player: {}, Computer: {}".format(wins,losses))
        if wins>losses:
                print("Player Wins!")
        elif wins == losses:
                print("Its a tie!")
        elif wins < losses:
            print("Computer Wins!")
        game = False
    continue




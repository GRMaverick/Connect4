#!/usr/bin/python
import os
from Board import Board

#GLOBALS
PLAYER_TURN=0
PLAYER_INPUT=0
GAME_BOARD=Board()
WINNER=-1

def Initialise():  
    global WINNER
    global PLAYER_TURN
    global PLAYER_INPUT
    WINNER = -1
    PLAYER_TURN = 0
    PLAYER_INPUT = 0
    GAME_BOARD.Initialise()
    Run()

def Run():
    global WINNER
    while(WINNER == -1):
        CheckUserInput()
        WINNER = GAME_BOARD.CheckWinner()
        Draw()

    GameOver()

def CheckUserInput():
    try:
        PLAYER_INPUT = int(input("Enter a column number: "))
    except ValueError:
        print("Not a valid number")
        CheckUserInput()
    else:
        os.system('cls')
        print("Player:", PLAYER_TURN+1, "has entered:", PLAYER_INPUT)
        GAME_BOARD.PlaceToken(PLAYER_INPUT, PLAYER_TURN)

def Draw():
    global PLAYER_TURN
    PLAYER_TURN = (PLAYER_TURN + 1) % 2
    GAME_BOARD.Draw()
    print("Player: ", PLAYER_TURN+1)

def GameOver():
    print("The winner is:", WINNER)
    try:
        PLAYER_INPUT = input("Play again? ( Yes | No )")
    except ValueError:
        print("Input not valid")
        GameOver()
    else:
        if(PLAYER_INPUT == "y"):
            Initialise()
        elif(PLAYER_INPUT == "n"):
            os.close(0)
        else:
            print("Input not valid")
            GameOver()

Initialise()
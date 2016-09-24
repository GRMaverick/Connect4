#!/usr/bin/python
import os
from Board import Board

#GLOBALS
GAME_LOOP=True
PLAYER_TURN=0
PLAYER_INPUT=0
GAME_BOARD=Board()

def Initialise():  
    GAME_LOOP = True
    PLAYER_INPUT = 0
    Run()

def Run():
    while(GAME_LOOP):
        CheckUserInput()
        Draw()

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

Initialise()
#!/usr/bin/python
import os
from Board import Board

#GLOBALS
GAME_LOOP_NOT_PAUSED=True
PLAYER_TURN=0
PLAYER_INPUT=0
GAME_BOARD=Board

def Initialise():  
    GAME_LOOP_NOT_PAUSED = True
    PLAYER_INPUT = 0
    Run()

def Run():
    while(GAME_LOOP_NOT_PAUSED):
        Update()
        Draw()

def CheckUserInput():
    PLAYER_INPUT = input("Enter a column number")
    os.system('cls')
    print("Player:", PLAYER_TURN+1, "has entered:", PLAYER_INPUT)

def Update():
    CheckUserInput()

def Draw():
    global PLAYER_TURN
    PLAYER_TURN = (PLAYER_TURN + 1) % 2
    GAME_BOARD.Draw()
    print("Player: ", PLAYER_TURN+1)   


Initialise()
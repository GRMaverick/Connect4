class Board(object):
    __pBoard = 0
    __pLastPlayer = 0

    def __init__(self):
        __pBoard = [0, 0, 0, 0, 0, 0 ,0, 0]

    def PlaceToken(position, player):
        __pLastPlayer = player
        # BASE-2 Calculation x**0
        __pBoard[position] += __pBoard[position] * __pBoard[position] 
        

    def Draw():
        print("Board Draw")
        
                



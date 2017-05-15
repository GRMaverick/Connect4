from Colours import Colours

class Board(object):
    __pHeight = 6
    __pWidth = 7
    __pBoard = [0, 0, 0, 0, 0, 0 ,0]
    __pBoardGraphic = [0, 0, 0, 0, 0, 0, 0]
    __pLastPlayer = 0

    def CheckHorizontal(self):
        for i in range(0, 4):
            for x in reversed(range(0,self.__pHeight)):
                check1 = ((self.__pBoard[i] & 2**x) and (self.__pBoard[i+1] & 2**x) and (self.__pBoard[i+2] & 2**x) and (self.__pBoard[i+3] & 2**x))    
                check2 = ((self.__pBoardGraphic[i] & 2**x == 0) and (self.__pBoardGraphic[i+1] & 2**x == 0) and (self.__pBoardGraphic[i+2] & 2**x == 0) and (self.__pBoardGraphic[i+3] & 2**x == 0))
                check3 = ((self.__pBoardGraphic[i] & 2**x) and (self.__pBoardGraphic[i+1] & 2**x) and (self.__pBoardGraphic[i+2] & 2**x) and (self.__pBoardGraphic[i+3] & 2**x))
                if(check1 and (check2 or check3)):
                    return self.__pLastPlayer
        return -1

    def CheckVertical(self):
            for x in range(0, self.__pWidth):
                for i in range(0,3):
                    check1 = (self.__pBoard[x] & 2**i) and (self.__pBoard[x] & 2**(i+1)) and (self.__pBoard[x] & 2**(i+2)) and (self.__pBoard[x] & 2**(i+3))
                    check2 = (self.__pBoardGraphic[x] & 2**i == 0) and (self.__pBoardGraphic[x] & 2**(i+1) == 0) and (self.__pBoardGraphic[x] & 2**(i+2) == 0) and (self.__pBoardGraphic[x] & 2**(i+3) == 0)
                    check3 = (self.__pBoardGraphic[x] & 2**i) and (self.__pBoardGraphic[x] & 2**(i+1)) and (self.__pBoardGraphic[x] & 2**(i+2)) and (self.__pBoardGraphic[x] & 2**(i+3))
                    if(check1 and (check2 or check3)):
                        return self.__pLastPlayer
            return -1

    def CheckDiagonal(self):
        for n in reversed(range(3,6)):
            for i in range(0, 4):
                check1 = (self.__pBoard[i] & 2**n) and (self.__pBoard[i+1] & 2**(n-1)) and (self.__pBoard[i+2] & 2**(n-2)) and (self.__pBoard[i+3] & 2**(n-3))
                check2 = (self.__pBoardGraphic[i] & 2**n == 0) and (self.__pBoardGraphic[i+1] & 2**(n-1) == 0) and (self.__pBoardGraphic[i+2] & 2**(n-2) == 0) and (self.__pBoardGraphic[i+3] & 2**(n-3) == 0)
                check3 = (self.__pBoardGraphic[i] & 2**n) and (self.__pBoardGraphic[i+1] & 2**(n-1)) and (self.__pBoardGraphic[i+2] & 2**(n-2)) and (self.__pBoardGraphic[i+3] & 2**(n-3))
                if(check1 and (check2 or check3)):
                    return self.__pLastPlayer
        for n in reversed(range(3, 6)):
            for i in reversed(range(3, 7)):
                check1 = (self.__pBoard[i] & 2**n) and (self.__pBoard[i-1] & 2**(n-1)) and (self.__pBoard[i-2] & 2**(n-2)) and (self.__pBoard[i-3] & 2**(n-3))
                check2 = (self.__pBoardGraphic[i] & 2**n == 0) and (self.__pBoardGraphic[i-1] & 2**(n-1) == 0) and (self.__pBoardGraphic[i-2] & 2**(n-2) == 0) and (self.__pBoardGraphic[i-3] & 2**(n-3) == 0)
                check3 = (self.__pBoardGraphic[i] & 2**n) and (self.__pBoardGraphic[i-1] & 2**(n-1)) and (self.__pBoardGraphic[i-2] & 2**(n-2)) and (self.__pBoardGraphic[i-3] & 2**(n-3))
                if(check1 and (check2 or check3)):
                    return self.__pLastPlayer
        return -1

    def __init__(self):
        self.__pBoard = [0, 0, 0, 0, 0, 0 ,0]
        self.__pBoardGraphic = [0, 0, 0, 0, 0, 0 ,0]
        self.__pLastPlayer = 0 

    def Initialise(self):
        self.__pBoard = [0, 0, 0, 0, 0, 0 ,0]
        self.__pBoardGraphic = [0, 0, 0, 0, 0, 0 ,0]
        self.__pLastPlayer = 0 

    def CheckWinner(self):
        if(self.CheckHorizontal() != -1):
            return self.__pLastPlayer
        if(self.CheckVertical() != -1):
            return self.__pLastPlayer
        if(self.CheckDiagonal() != -1):
            return self.__pLastPlayer
        return -1

    def Draw(self):
        print()
        for index in reversed(range(0, self.__pHeight)):
            print(
                "[        ]" if self.__pBoard[0] & 2**index == 0 else "[" + Colours.RED + "  RED   " + Colours.NORMAL + "]" if self.__pBoardGraphic[0] & 2**index else "[" + Colours.YELLOW + " YELLOW " + Colours.NORMAL + "]" if self.__pBoardGraphic[0] & 2**index == 0 else print("X"),
                "[        ]" if self.__pBoard[1] & 2**index == 0 else "[" + Colours.RED + "  RED   " + Colours.NORMAL + "]" if self.__pBoardGraphic[1] & 2**index else "[" + Colours.YELLOW + " YELLOW " + Colours.NORMAL + "]" if self.__pBoardGraphic[1] & 2**index == 0 else print("X"),
                "[        ]" if self.__pBoard[2] & 2**index == 0 else "[" + Colours.RED + "  RED   " + Colours.NORMAL + "]" if self.__pBoardGraphic[2] & 2**index else "[" + Colours.YELLOW + " YELLOW " + Colours.NORMAL + "]" if self.__pBoardGraphic[2] & 2**index == 0 else print("X"),
                "[        ]" if self.__pBoard[3] & 2**index == 0 else "[" + Colours.RED + "  RED   " + Colours.NORMAL + "]" if self.__pBoardGraphic[3] & 2**index else "[" + Colours.YELLOW + " YELLOW " + Colours.NORMAL + "]" if self.__pBoardGraphic[3] & 2**index == 0  else print("X"),
                "[        ]" if self.__pBoard[4] & 2**index == 0 else "[" + Colours.RED + "  RED   " + Colours.NORMAL + "]" if self.__pBoardGraphic[4] & 2**index else "[" + Colours.YELLOW + " YELLOW " + Colours.NORMAL + "]" if self.__pBoardGraphic[4] & 2**index == 0  else print("X"),
                "[        ]" if self.__pBoard[5] & 2**index == 0 else "[" + Colours.RED + "  RED   " + Colours.NORMAL + "]" if self.__pBoardGraphic[5] & 2**index else "[" + Colours.YELLOW + " YELLOW " + Colours.NORMAL + "]" if self.__pBoardGraphic[5] & 2**index == 0  else print("X"),
                "[        ]" if self.__pBoard[6] & 2**index == 0 else "[" + Colours.RED + "  RED   " + Colours.NORMAL + "]" if self.__pBoardGraphic[6] & 2**index else "[" + Colours.YELLOW + " YELLOW " + Colours.NORMAL + "]" if self.__pBoardGraphic[6] & 2**index == 0  else print("X"))
        print()
        
    def GetNextAvailable(self, board, column):
        BIT_POSITION = 0
        BIT_SWITCH = 2 ** BIT_POSITION
        while(board[column] & BIT_SWITCH):
            BIT_POSITION += 1
            BIT_SWITCH = 2 ** BIT_POSITION
        return BIT_POSITION

    def CheckColumnFull(self, column):
        return (self.__pBoard[column-1] == 2 ** self.__pHeight-1)

    def PlaceToken(self, column, player):
        if(column not in range(1, self.__pWidth + 1)):
            try: 
                self.PlaceToken(int(input("Please enter a column between 1 and 8: ")), player) 
            except ValueError:
                print("Not a valid number")
                self.PlaceToken(int(input("Please enter a column between 1 and 8: ")), player)
        elif(self.CheckColumnFull(column) == True):
            try:
                self.PlaceToken(int(input("Column is full, please select another column: ")), player)
            except ValueError:
                print("Not a valid number")
                self.PlaceToken(int(input("Please enter a column between 1 and 8: ")), player)
        else:
            self.__pLastPlayer = player
            value = (2 ** self.GetNextAvailable(self.__pBoard, column-1))
            self.__pBoard[column-1] = self.__pBoard[column-1] + value
            if(player == 0):
                self.__pBoardGraphic[column-1] = self.__pBoardGraphic[column-1] + value
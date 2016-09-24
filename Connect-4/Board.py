class Board(object):
    __pBoard = [0, 0, 0, 0, 0, 0 ,0, 0]
    __pBoardGraphic = [0, 0, 0, 0, 0, 0, 0, 0]
    __pLastPlayer = 0

    def __init__(self):
        self.__pBoard = [0, 0, 0, 0, 0, 0 ,0, 0]
        self.__pBoardGraphic = [0, 0, 0, 0, 0, 0, 0, 0]
        self.__pLastPlayer = 0 
    def Draw(self):
        print()
        for index in reversed(range(0, 8)):
            print(self.__pBoard[0] & 2**index, " ", self.__pBoard[1] & 2**index, " ", self.__pBoard[2] & 2**index, " ", self.__pBoard[3] & 2**index, " ", self.__pBoard[4] &2**index, " ", self.__pBoard[5] & 2**index , " ", self.__pBoard[6] & 2**index, " ", self.__pBoard[7] & 2**index)
        print()
        
    def GetNextAvailable(self, column):
        BIT_POSITION = 0
        BIT_SWITCH = 2 ** BIT_POSITION
        while(self.__pBoard[column] & BIT_SWITCH):
            BIT_POSITION += 1
            BIT_SWITCH = 2 ** BIT_POSITION
        return BIT_POSITION
    def CheckColumnFull(self, column):
        if(self.__pBoard[column-1] == 255):
            return True
        return False       
    def PlaceToken(self, column, player):
        if(column not in range(1,8)):
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
            self.__pBoard[column-1] = self.__pBoard[column-1] + (2 ** self.GetNextAvailable(column-1))
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.simpleImage import SimpleImage
from Objects.piece import Piece

class Queen(Piece) :
    def __init__(self, isWhite) :
        if isWhite :
            super().__init__("Resources/Images/Pieces/White_Queen.png",isWhite)
            self.boardY = 7
        else :
            super().__init__("Resources/Images/Pieces/Black_Queen.png",isWhite)
            self.boardY = 0
        self.boardX = 4

    def canMove(self, board) :
        canMoveList = list()

        whiteNum = 1 if self.isWhite else 2
        for j in range(self.boardY -1, -1, -1) :
            if board[self.boardX][j] == whiteNum :
                break
            else :
                canMoveList.append((self.boardX, j))

        for j in range(self.boardY + 1 , 8) :
            if board[self.boardX][j] == whiteNum :
                break
            else :
                canMoveList.append((self.boardX, j))
                
        for i in range(self.boardX -1, -1, -1) :
            if board[i][self.boardY] == whiteNum :
                break
            else :
                canMoveList.append((i, self.boardY))
                
        for i in range(self.boardX + 1, 8) :
            if board[i][self.boardY] == whiteNum :
                break
            else :
                canMoveList.append((i, self.boardY))

        i = self.boardX + 1
        j = self.boardY - 1
        
        while i < 8 and j >= 0 :
            if board[i][j] == whiteNum :
                break
            canMoveList.append((i,j))
            i+=1
            j-=1

        i = self.boardX - 1
        j = self.boardY + 1

        while i >= 0 and j < 8 :
            if board[i][j] == whiteNum :
                break
            canMoveList.append((i,j))
            i-=1
            j+=1

        i = self.boardX -1
        j = self.boardY -1

        while i >= 0 and j >= 0 :
            if board[i][j] == whiteNum :
                break
            canMoveList.append((i,j))
            i-=1
            j-=1

        i = self.boardX + 1
        j = self.boardY + 1

        while i < 8 and j < 8 :
            if board[i][j] == whiteNum :
                break
            canMoveList.append((i,j))
            i+=1
            j+=1
            
        return canMoveList

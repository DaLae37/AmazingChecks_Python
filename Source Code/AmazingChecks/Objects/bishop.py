import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.simpleImage import SimpleImage
from Objects.piece import Piece

class Bishop(Piece) :
    def __init__(self, isWhite, boardX, boardY) :
        if isWhite :
            super().__init__("Resources/Images/Pieces/White_Bishop.png",isWhite)
        else :
            super().__init__("Resources/Images/Pieces/Black_Bishop.png",isWhite)

        super().setBoardPos(boardX, boardY)

    def canMove(self, board) :
        canMoveList = list()
        
        whiteNum = 1 if self.isWhite else 2

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

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.simpleImage import SimpleImage
from Objects.piece import Piece

class Rook(Piece) :
    def __init__(self, isWhite, boardX, boardY) :
        if isWhite :
            super().__init__("Resources/Images/Pieces/White_Rook.png",isWhite)
        else :
            super().__init__("Resources/Images/Pieces/Black_Rook.png",isWhite)

        super().setBoardPos(boardX, boardY)
        
    def canMove(self, board) :
        canMoveList = list()

        whiteNum = 1 if self.isWhite else 2
        for j in range(self.boardY -1, -1, -1) :
            if board[self.boardX][j] == whiteNum :
                break
            elif board[self.boardX][j] != 0 :
                canMoveList.append((self.boardX, j))
                break
            else :
                canMoveList.append((self.boardX, j))

        for j in range(self.boardY + 1 , 8) :
            if board[self.boardX][j] == whiteNum :
                break
            elif board[self.boardX][j] != 0 :
                canMoveList.append((self.boardX, j))
                break
            else :
                canMoveList.append((self.boardX, j))
                
        for i in range(self.boardX -1, -1, -1) :
            if board[i][self.boardY] == whiteNum :
                break
            elif board[i][self.boardY] != 0 :
                canMoveList.append((i, self.boardY))
                break
            else :
                canMoveList.append((i, self.boardY))
                
        for i in range(self.boardX + 1, 8) :
            if board[i][self.boardY] == whiteNum :
                break
            elif board[i][self.boardY] != 0 :
                canMoveList.append((i, self.boardY))
                break
            else :
                canMoveList.append((i, self.boardY))
            
        return canMoveList

    def getPieceValue(self) :
        return 50 if self.isWhite else -50

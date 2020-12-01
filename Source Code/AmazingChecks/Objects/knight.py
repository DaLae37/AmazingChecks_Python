import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.simpleImage import SimpleImage
from Objects.piece import Piece

class Knight(Piece) :
    def __init__(self, isWhite, boardX, boardY) :
        if isWhite :
            super().__init__("Resources/Images/Pieces/White_Knight.png",isWhite)
        else :
            super().__init__("Resources/Images/Pieces/Black_Knight.png",isWhite)

        super().setBoardPos(boardX, boardY)

    def canMove(self, board) :
        canMoveList = list()
        whiteNum = 1 if self.isWhite else 2
        knightList = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

        for knight in knightList :
            if 0 <= knight[0] + self.boardX < 8 and 0 <= knight[1] + self.boardY < 8 and board[self.boardX + knight[0]][self.boardY + knight[1]] != whiteNum :
                canMoveList.append((knight[0] + self.boardX, knight[1] + self.boardY))

        return canMoveList

    def getPieceValue(self) :
        return 30 if self.isWhite else -30

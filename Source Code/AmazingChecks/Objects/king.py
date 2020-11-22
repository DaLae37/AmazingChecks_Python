import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.simpleImage import SimpleImage
from Objects.piece import Piece

class King(Piece) :
    def __init__(self, isWhite) :
        if isWhite :
            super().__init__("Resources/Images/Pieces/White_King.png",isWhite)
            self.boardY = 7
        else :
            super().__init__("Resources/Images/Pieces/Black_King.png",isWhite)
            self.boardY = 0
        self.boardX = 3

    def canMove(self, board) :
        canMoveList = list()
        for i in range(-1,2) :
            if self.boardX + i < 0 or self.boardX + i > 7 :
                    continue
            for j in range(-1,2) :
                if self.boardY + j < 0 or self.boardY + j > 7 :
                    continue
                if i == 0 and j == 0 :
                    continue

                whiteNum = 1 if self.isWhite else 2
                if board[self.boardX + i][self.boardY + j] != whiteNum :
                    canMoveList.append((self.boardX + i, self.boardY + j))

        return canMoveList

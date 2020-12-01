import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.simpleImage import SimpleImage
from Objects.piece import Piece

class Pawn(Piece) :
    def __init__(self, isWhite, boardX, boardY) :
        if isWhite :
            super().__init__("Resources/Images/Pieces/White_Pawn.png",isWhite)
        else :
            super().__init__("Resources/Images/Pieces/Black_Pawn.png",isWhite)
        
        super().setBoardPos(boardX, boardY)
        
        self.onceMoved = False
        
    def canMove(self, board) :
        canMoveList = list()
        whiteChecker = 2
        moveChecker = 1
        if self.isWhite :
            moveChecker = -1
            whiteChecker = 1

        if self.onceMoved == False and 0 <= self.boardY + moveChecker * 2 < 8 and board[self.boardX][self.boardY + moveChecker * 2] == 0 and board[self.boardX][self.boardY + moveChecker] == 0:
            canMoveList.append((self.boardX, self.boardY + 2 * moveChecker))
        if 0 <= self.boardY + moveChecker < 8 and board[self.boardX][self.boardY + moveChecker] == 0:
            canMoveList.append((self.boardX, self.boardY + moveChecker))

        if self.boardX + 1 < 8 and 0 <= self.boardY + moveChecker < 8 and board[self.boardX + 1][self.boardY + moveChecker] != 0 and board[self.boardX + 1][self.boardY + moveChecker] != whiteChecker :
            canMoveList.append((self.boardX + 1, self.boardY + moveChecker))
        if self.boardX - 1 >= 0 and 0 <= self.boardY + moveChecker < 8 and board[self.boardX - 1][self.boardY + moveChecker] != 0 and board[self.boardX -1][self.boardY + moveChecker] != whiteChecker :
            canMoveList.append((self.boardX -1, self.boardY + moveChecker))
            
        return canMoveList
    
    def getPieceValue(self) :
        return 10 if self.isWhite else -10
    
    def setOnceMoved(self) :
        self.onceMoved = True

    def getOnceMove(self) :
        return self.onceMoved

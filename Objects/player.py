import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Objects.king import King
from Objects.queen import Queen
from Objects.rook import Rook
from Objects.bishop import Bishop
from Objects.knight import Knight
from Objects.pawn import Pawn

class Player() :
    def __init__(self, isWhite) :
        self.isWhite = isWhite
        self.isGameOver = False
        self.pieces = list()

    def inputCheck(self, piece) :
        for pc in self.pieces :
            if pc == piece :
                return True
        return False
        
    def makePieces(self) :
        piecesLane = 0
        if self.isWhite :
            piecesLane = 7
            
        self.pieces.append(King(self.isWhite))
        self.pieces.append(Queen(self.isWhite))
        self.pieces.append(Rook(self.isWhite, 0, piecesLane))
        self.pieces.append(Rook(self.isWhite, 7, piecesLane))
        self.pieces.append(Bishop(self.isWhite, 1, piecesLane))
        self.pieces.append(Bishop(self.isWhite, 6, piecesLane))
        self.pieces.append(Knight(self.isWhite, 2, piecesLane))
        self.pieces.append(Knight(self.isWhite, 5, piecesLane))

        if self.isWhite :
            piecesLane = 6
        else :
            piecesLane = 1

        for i in range(8) :
            self.pieces.append(Pawn(self.isWhite, i, piecesLane))

    def getPieces(self) :
        return self.pieces

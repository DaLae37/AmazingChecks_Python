import pygame
import math
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.simpleImage import SimpleImage
from Framework.sceneManager import SceneManager
from Objects.king import King
from Objects.queen import Queen
from Objects.rook import Rook
from Objects.bishop import Bishop
from Objects.knight import Knight
from Objects.pawn import Pawn

class ChessBoard(SimpleImage) :
    def __init__(self) :
        super().__init__("Resources/Images/Board/board.png")
        self.board = [[0 for i in range(8)] for j in range(8)] #None 0, White 1, Black 2
        self.pieces = list()

        self.isSelected = False
        self.selectedPieceMovableList = list()
        self.selectedPiece = None
        
        self.selectedPos = (0,0)
        self.selectedImage = SimpleImage("Resources/Images/Board/select.png")
        self.movableImage = SimpleImage("Resources/Images/Board/movable.png")

        self.whiteKing = None
        self.blackKing = None
        
    def update(self, screen) :
        screen.blit(super().getSurface(), super().getPos())
        for pc in self.pieces :
            if not pc.getIsDead() :
                x = pc.getBoardPos()[0]
                y = pc.getBoardPos()[1]
                screen.blit(pc.getSurface(), (x * 90 + 10, y * 90 + 10))

        if self.isSelected :
            screen.blit(self.selectedImage.getSurface(), (self.selectedPos[0] * 90, self.selectedPos[1] * 90))
            for pos in self.selectedPieceMovableList :
                screen.blit(self.movableImage.getSurface(), (pos[0] * 90, pos[1] * 90))

    def isGameEnd(self) : #return isGameEnd, isWhiteWin
        return (self.whiteKing.getIsDead() or self.blackKing.getIsDead(), self.blackKing.getIsDead())

    def makeBoard(self, whitePieces, blackPieces) :
        for white in whitePieces :
            self.pieces.append(white)
            if isinstance(white, King) :
                self.whiteKing = white
            w = white.getBoardPos()            
            self.board[w[0]][w[1]] = 1

        for black in blackPieces :
            self.pieces.append(black)
            if isinstance(black, King) :
                self.blackKing = black
            b = black.getBoardPos()
            self.board[b[0]][b[1]] = 2

    def getPiece(self, boardX, boardY) :
        for pc in self.pieces :
            if pc.getBoardPos() == (boardX, boardY) :
                return pc

        return None

    def setPieceNotation(self, piece) :
        self.isSelected = True
        self.selectedPiece = piece
        self.selectedPieceMovableList = piece.canMove(self.board)
        self.selectedPos = piece.getBoardPos()

    def movePiece(self, boardX, boardY) :
        isFind = False
        for movable in self.selectedPieceMovableList :
            if movable == (boardX, boardY) :
                isFind = True

                piece = self.getPiece(boardX, boardY) 
                if piece is not None :
                    piece.setIsDead(True)

                self.board[self.selectedPos[0]][self.selectedPos[1]] = 0
                self.board[boardX][boardY] = 1 if self.selectedPiece.getIsWhite() else 2
                self.selectedPiece.setBoardPos(boardX,boardY)
                self.isSelected = False
                if isinstance(self.selectedPiece, Pawn) :
                    self.selectedPiece.setOnceMoved()
                break
            
        return isFind

    def setIsSelected(self, isSelected) :
        self.isSelected = isSelected

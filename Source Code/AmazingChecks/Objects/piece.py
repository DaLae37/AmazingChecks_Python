import pygame
import math
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.simpleImage import SimpleImage

class Piece(SimpleImage) :
    instance = None
    def __init__(self, imgDir, isWhite) :
        super().__init__(imgDir)
        self.boardX = 0
        self.boardY = 0
        self.isWhite = isWhite
        self.isDead = False

    def canMove(self) :
        pass

    def setIsDead(self, isDead) :
        self.isDead = isDead

    def getIsDead(self) :
        return self.isDead

    def setBoardPos(self, boardX, boardY) :
        self.boardX = boardX
        self.boardY = boardY

    def getBoardPos(self) :
        return (self.boardX, self.boardY)

    def getIsWhite(self) :
        return self.isWhite

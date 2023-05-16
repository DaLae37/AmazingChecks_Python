import pygame
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Objects.chessBoard import ChessBoard
from Objects.player import Player

from Framework.sceneManager import Scene, SceneManager
from Framework.simpleImage import SimpleImage

class GameScene(Scene) :
       
    def __init__(self, screen, clock) :
        self.screen = screen
        self.clock = clock

        self.load_resources()
        self.isWhiteTurn = True
        self.isPlayerSelected = False
        self.selectedPiece = None

    def update(self) :
        self.chessBoard.update(self.screen)
            
        isGameEnd = self.chessBoard.isGameEnd()
        if isGameEnd[0] :
            if isGameEnd[1] :
                print("white win!")
            else :
                print("black win!")
            SceneManager.getInstance().changeScene("MainScene")
                
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                SceneManager.getInstance().isQuit = True
                return

            if event.type == pygame.MOUSEBUTTONDOWN :
                mousePos = pygame.mouse.get_pos()
                selectedPiece = self.chessBoard.getPiece(mousePos[0] // 90, mousePos[1] // 90)
                if not self.isPlayerSelected :
                    if (self.isWhiteTurn and self.whitePlayer.inputCheck(selectedPiece)) or not self.isWhiteTurn and self.blackPlayer.inputCheck(selectedPiece) :
                            self.selectedPiece =  selectedPiece
                            self.isPlayerSelected = True
                            self.chessBoard.setPieceNotation(selectedPiece)
                                
                else :
                    if self.selectedPiece == selectedPiece :
                        self.selectedPiece = None
                        self.isPlayerSelected = False
                        self.chessBoard.setIsSelected(False)
                            
                    else :
                        if self.chessBoard.movePiece(mousePos[0] // 90, mousePos[1] // 90) :
                            self.isWhiteTurn = not self.isWhiteTurn
                        self.selectedPiece = None
                        self.isPlayerSelected = False
                        self.chessBoard.setIsSelected(False)

    def load_resources(self) :
        self.chessBoard = ChessBoard()
        self.whitePlayer = Player(True)
        self.blackPlayer = Player(False)

        self.whitePlayer.makePieces()
        self.blackPlayer.makePieces()

        self.chessBoard.makeBoard(self.whitePlayer.getPieces(), self.blackPlayer.getPieces())

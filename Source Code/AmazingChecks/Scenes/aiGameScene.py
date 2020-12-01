import pygame
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Objects.chessBoard import ChessBoard
from Objects.player import Player
from Objects.ai import AI

from Framework.sceneManager import Scene, SceneManager
from Framework.simpleImage import SimpleImage

class AIGameScene(Scene) :
       
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

            if self.isWhiteTurn :
                if event.type == pygame.MOUSEBUTTONDOWN :
                    mousePos = pygame.mouse.get_pos()
                    selectedPiece = self.chessBoard.getPiece(mousePos[0] // 90, mousePos[1] // 90)
                    if not self.isPlayerSelected :
                        if (self.isWhiteTurn and self.whitePlayer.inputCheck(selectedPiece))  :
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

            else :
                move = self.blackPlayer.minimaxRoot(3, self.chessBoard.getChessBoard(), self.chessBoard.getPieces(), True)
                print(self.chessBoard.movePieceWithAI(move[0], move[1][0], move[1][1]))
                self.isWhiteTurn = not self.isWhiteTurn
                    

    def load_resources(self) :
        self.chessBoard = ChessBoard()
        self.whitePlayer = Player(True)
        self.blackPlayer = AI(False)

        self.whitePlayer.makePieces()
        self.blackPlayer.makePieces()

        self.chessBoard.makeBoard(self.whitePlayer.getPieces(), self.blackPlayer.getPieces())


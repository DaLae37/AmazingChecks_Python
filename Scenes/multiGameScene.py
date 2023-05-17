import pygame
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Objects.chessBoard import ChessBoard
from Objects.player import Player

from Framework.sceneManager import Scene, SceneManager
from Framework.simpleImage import SimpleImage

from unittest import mock

class MultiGameScene(Scene) :
    def __init__(self, screen, clock) :
        self.screen = screen
        self.clock = clock

        self.load_resources()
        self.isWhiteTurn = True
        self.isPlayerSelected = False
        self.selectedPiece = None

        self.mock = mock.Mock()
        self.mock.getPlayerSelect.return_value = 0, 1
        self.mock.getPlayerSelect.side_effect = print("상대방 입력 완료")

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

            if not self.isWhiteTurn :
                x, y =self.mock.getPlayerSelect()
                print("상대방 선택 X : {}, Y : {}".format(x,y))
                selectedPiece = self.chessBoard.getPiece(x ,y)
                self.isWhiteTurn = not self.isWhiteTurn
                
            else :
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


    def load_resources(self) :
        self.chessBoard = ChessBoard()
        self.whitePlayer = Player(True)
        self.blackPlayer = Player(False)

        self.whitePlayer.makePieces()
        self.blackPlayer.makePieces()

        self.chessBoard.makeBoard(self.whitePlayer.getPieces(), self.blackPlayer.getPieces())
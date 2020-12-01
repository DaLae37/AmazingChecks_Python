import pygame
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Objects.chessBoard import ChessBoard
from Objects.player import Player

from Framework.sceneManager import Scene, SceneManager
from Framework.simpleImage import SimpleImage

class MultiGameScene(Scene) :
       
    def __init__(self, screen, clock) :
        self.screen = screen
        self.clock = clock

    def update(self) :
        print("To Be Continue")
        SceneManager.getInstance().changeScene("MainScene")

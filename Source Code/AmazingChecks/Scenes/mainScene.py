import pygame
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.scene import Scene
from Framework.sceneManager import SceneManager
from Framework.soundManager import SoundManager
from Framework.animation import Animation
from Framework.simpleImage import SimpleImage

class MainScene(Scene) :

    simpleImage_list = []

    def __init__(self, screen, clock) :
        self.screen = screen
        self.clock = clock

        self.load_resources()

    def update(self) :
        for si in self.simpleImage_list :
            self.screen.blit(si.getSurface(), si.getPos())

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                SceneManager.getInstance().isQuit = True
                return

            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.chessButton.isCollisionRect(pygame.mouse.get_pos()) :
                    SceneManager.getInstance().changeScene("GameScene")
                    return

    def load_resources(self) :
        SoundManager.getInstance().load_music("Resources/Sounds/BGM.mp3")

        self.background = SimpleImage("Resources/Images/Background/background.png")
        self.background.setPos((0,0))
        self.background.setSize((720,720))
        self.simpleImage_list.append(self.background)

        self.chessButton = SimpleImage("Resources/Images/UI/chess.png")
        self.chessButton.setCenterMode(True)
        self.chessButton.setPos((500, 600))
        self.chessButton.setSize((250, 100))
        self.simpleImage_list.append(self.chessButton)

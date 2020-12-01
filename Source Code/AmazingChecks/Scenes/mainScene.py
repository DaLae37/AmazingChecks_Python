import pygame
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Framework.scene import Scene
from Framework.sceneManager import SceneManager
from Framework.soundManager import SoundManager
from Framework.simpleImage import SimpleImage

from Scenes.gameScene import GameScene
from Scenes.aiGameScene import AIGameScene
from Scenes.multiGameScene import MultiGameScene

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
                if self.normalGameButton.isCollisionRect(pygame.mouse.get_pos()) :
                    SceneManager.getInstance().changeScene("GameScene")
                    return
                elif self.aiGameButton.isCollisionRect(pygame.mouse.get_pos()) :
                    SceneManager.getInstance().changeScene("AIGameScene")
                    return
                elif self.multiGameButton.isCollisionRect(pygame.mouse.get_pos()) :
                    SceneManager.getInstance().changeScene("MultiGameScene")
                    return

    def load_resources(self) :
        SoundManager.getInstance().load_music("Resources/Sounds/BGM.mp3")

        self.background = SimpleImage("Resources/Images/Background/background.png")
        self.background.setPos((0,0))
        self.background.setSize((720,720))
        self.simpleImage_list.append(self.background)

        self.background = SimpleImage("Resources/Images/Background/title.png")
        self.background.setPos((0,10))
        self.background.setSize((720,200))
        self.simpleImage_list.append(self.background)

        self.normalGameButton = SimpleImage("Resources/Images/UI/normalGame.png")
        self.normalGameButton.setPos((20, 600))
        self.normalGameButton.setSize((200, 100))
        self.simpleImage_list.append(self.normalGameButton)

        self.aiGameButton = SimpleImage("Resources/Images/UI/aiGame.png")
        self.aiGameButton.setPos((260, 600))
        self.aiGameButton.setSize((200, 100))
        self.simpleImage_list.append(self.aiGameButton)

        self.multiGameButton = SimpleImage("Resources/Images/UI/multiGame.png")
        self.multiGameButton.setPos((500, 600))
        self.multiGameButton.setSize((200, 100))
        self.simpleImage_list.append(self.multiGameButton)

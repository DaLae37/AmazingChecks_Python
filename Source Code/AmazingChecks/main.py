import pygame

from Framework.sceneManager import SceneManager
from Framework.simpleImage import SimpleImage
from Scenes.mainScene import MainScene
from Scenes.gameScene import GameScene
from Scenes.aiGameScene import AIGameScene
from Scenes.multiGameScene import MultiGameScene

if __name__ == '__main__' :
    pygame.init()
    pygame.display.set_caption("Amazing Checks")
    pygame.display.set_icon(SimpleImage("Resources/Images/UI/logo.png").getSurface())
    pygame.mixer.pre_init(44100, 16, 2, 4096) #Frequency, Size, Channels, BufferSize

    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()
    run = True
    
    SceneManager.getInstance().registerGameObjects(screen, clock)
    SceneManager.getInstance().registerScene("MainScene", MainScene(screen,clock))
    SceneManager.getInstance().registerScene("GameScene", GameScene(screen,clock))
    SceneManager.getInstance().registerScene("AIGameScene", AIGameScene(screen,clock))
    SceneManager.getInstance().registerScene("MultiGameScene", MultiGameScene(screen,clock))
    SceneManager.getInstance().changeScene("MainScene")

    while run:
        SceneManager.getInstance().update()
        
        pygame.display.flip()
        clock.tick(144)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if SceneManager.getInstance().isQuit :
            run = False

    pygame.quit()

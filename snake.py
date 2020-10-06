import pygame
pygame.init()

class GameLoop:
    def __init__(self):
        self.width = 852
        self.height = 480
        self.x = self.width//2        
        self.y = self.height//2   
        self.red = (255,0,0)     
        self.green = (0,255,0)     
        self.blue = (0,0,255)     
        win = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Snake")
        def snake():
            pygame.draw.rect(win,self.blue,(self.x,self.y,20,20))
            pygame.display.update()
        self.run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            snake()
        
Game = GameLoop()

pygame.quit()
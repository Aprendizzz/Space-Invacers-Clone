from ship import *
# import pygame
# from pygame.locals import *
class Player(Ship):
    def __init__(self, screensize):
        super().__init__(50,screensize[1]*0.95, 100)
        self.sprite = pygame.image.load("../imagens/player/ship.png")
        self.x = self.getPositionX()
        self.y = self.getPositionY()
        self.positionShot = Vector2D(self.x,self.y)
    def assets(self):
        pass
    def input(self):
        self.teclas = pygame.key.get_pressed()
        if self.teclas[K_LEFT]:
            self.setPositionX(int(self.getPositionX() - 2))
        if self.teclas[K_RIGHT]:
            self.setPositionX(round(self.getPositionX() + 2))
    def draw(self, screen):
        screen.blit(self.sprite, (self.getPositionX(), self.getPositionY()))
    def shot(self, screen):
        
        if self.teclas[K_UP] or self.teclas[K_SPACE]:
            print("entrou")
            self.x = self.getPositionX()
            self.y = self.getPositionY()
            pygame.draw.rect(screen, (0,127,127), (self.x,self.y,5,10))

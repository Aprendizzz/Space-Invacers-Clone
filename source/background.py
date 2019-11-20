import pygame
from vector2D import Vector2D
class BackGround:
    def __init__(self,x,y):
        self.position = Vector2D(x, y)
        self.sprite = pygame.image.load("../imagens/background/space.png")
    def setPositionX(self, x):
        self.position.x = x
    def setPositionY(self, y):
        self.position.y = y
    def getPositionX(self):
        return self.position.x
    def getPositionY(self):
        return self.position.y
    def move(self):
        self.setPositionY(self.getPositionY() + 0.4)
        if self.getPositionY() > 0:
            self.setPositionY(self.getPositionY() - 450)
    def draw(self, screen):
        screen.blit(self.sprite, (self.getPositionX(),self.getPositionY()))
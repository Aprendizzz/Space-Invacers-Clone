from vector2D import Vector2D
import pygame
from pygame.locals import *
class Player():

    def __init__(self, screensize, x, y, life):
        self.position = Vector2D(x,y)
        self.positionShot = Vector2D(self.getPositionX(), self.getPositionY())
        self.life = life
        self.sprite = pygame.image.load("../imagens/player/ship.png")
        self.shotY = 0
        self.shotBool = False
        self.velocity = 10
        self.colorShot  = (0,255,127)
    
    def assets(self):
        pass

    def input(self):
        self.teclas = pygame.key.get_pressed()
        if self.teclas[K_LEFT]:
            self.setPositionX(int(self.getPositionX() - self.velocity))
        if self.teclas[K_RIGHT]:
            self.setPositionX(int(self.getPositionX() + self.velocity))
        if self.shotBool == False:
            if self.teclas[K_UP] or self.teclas[K_SPACE]:
                self.setPositionShotX(self.getPositionX())
                self.setPositionShotY(self.getPositionY())
                self.shotY = self.getPositionShotY()
                self.shotBool = True
        if self.shotY < 0:
            self.shotBool = False
    
    def draw(self, screen):
        screen.blit(self.sprite, (self.getPositionX(), self.getPositionY()))
        if self.shotBool == True:
            self.shotY -= 10
            pygame.draw.rect(screen, self.colorShot, (self.getPositionShotX()+12, self.shotY,5,10))
    
    #Getters and Setters of shot
    def setPositionShotX(self, x):
        self.positionShot.x = x

    def setPositionShotY(self, y):
        self.positionShot.y = y

    def getPositionShotX(self):
        return self.positionShot.x

    def getPositionShotY(self):
        return self.positionShot.y

    #Getters and Setters of player
    def setPositionX(self, x):
        self.position.x = x

    def setPositionY(self, y):
        self.position.y = y

    def getPositionX(self):
        return self.position.x

    def getPositionY(self):
        return self.position.y

    #Getters and Setters of Life
    def setLife(self, life):
        self.life = life
    
    def getLife(self):
        return self.life

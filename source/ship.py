from vector2D import Vector2D
import pygame
from pygame.locals import *
class Ship:
    def __init__(self, x,y, life):
        self.position = Vector2D(x, y)
        self.life = life
    def move(self):
        pass
    def shot(self):
        pass
    def skills(self):
        pass

    #Getters and Setters
    def setPosition(self, x, y):
        self.position.x = x
        self.position.y = y
    def setPositionX(self, x):
        self.position.x = x
    def setPositionY(self, y):
        self.position.y = y
    def getPosition(self):
        return self.position.x, self.position.y
    def getPositionX(self):
        return self.position.x
    def getPositionY(self):
        return self.position.y
    def setLife(self, life):
        self.life = life
    def getLife(self):
        return self.life
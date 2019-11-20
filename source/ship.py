from vector2D import Vector2D
import pygame
from pygame.locals import *
from random import randint
class Ship:

    def __init__(self, x,y, life):
        self.position = Vector2D(x, y)
        #self.positionShot = Vector2D(self.getPositionX(), self.getPositionY())
        self.life = life
        # self.sizeOfEnemy = 30
        # self.spaceOfEnemy = [30,10]
        # self.startPosition = [10,50]
        self.velocity = 5
        self.shotY = 0
        self.shotBool = False
        self.colorShot = (255,34,200)
        self.directionRight = True

    def move(self):
        pass

    def shot(self):
        self.positionShot = Vector2D(self.getPositionX(), self.getPositionY())
        return self.positionShot.x, self.positionShot.y

    def skills(self):
        pass

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
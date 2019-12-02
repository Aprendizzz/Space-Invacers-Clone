
from vector2D import Vector2D
import pygame
from pygame.locals import *
from random import randint

class Enemy(object):

    def __init__(self, number, x, y, life):
        self.position = Vector2D(x,y)
        self.number = number
        self.sprite = []
        #sprites
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyPurple/enemy1_1.png"))
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyPurple/enemy1_2.png"))

        self.sprite.append(pygame.image.load("../imagens/enemy/enemyBlue/enemy1_1.png"))
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyBlue/enemy1_2.png"))

        self.sprite.append(pygame.image.load("../imagens/enemy/enemyGreen/enemy1_1.png"))
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyGreen/enemy1_2.png"))

        self.directionRight = True
        self.velocity = 5
        self.acelerate = 0.0
        
    def assets(self):
        return self.sprite
    
    def move(self, screensize, enemy):
        if self.directionRight == True:
            enemy.setPositionX((enemy.getPositionX() + self.velocity))
        if self.directionRight == False:
            enemy.setPositionX((enemy.getPositionX() - self.velocity))
        if enemy.getPositionX() > (screensize[0]): # - max(enemy[0] for enemy in matrixOfEnemy) - sizeOfEnemy):
            enemy.setPositionX(0)
            enemy.setPositionY((enemy.getPositionY() + 5))
            #self.directionRight = False
        if enemy.getPositionX() < (10): # - min(enemy[0] for enemy in matrixOfEnemy)):
            enemy.setPositionX(screensize[0])
            enemy.setPositionY((enemy.getPositionY() + (self.velocity + 5)))
            #self.directionRight = True
                
    
    def move2(self, screensize, enemy, direction):
        # enemy.setPositionX(int(enemy.getPositionX() + (self.velocity)))
        if (direction == 0):
            enemy.setPositionX(int(enemy.getPositionX() + (self.velocity)))
        if (direction == 1):
            enemy.setPositionX(int(enemy.getPositionX() - (self.velocity)))
        if(enemy.getPositionX() > screensize[0]):
            enemy.setPositionX(0)
            enemy.setPositionY(enemy.getPositionY() + 50)

    def getDirectionRight(self):
        return self.directionRight

    #Getters and Setters of player
    def setPositionX(self, x):
        self.position.x = x

    def setPositionY(self, y):
        self.position.y = y

    def getPositionX(self):
        return self.position.x

    def getPositionY(self):
        return self.position.y
    

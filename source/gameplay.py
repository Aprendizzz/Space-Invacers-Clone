from player import Player
from enemy import Enemy
from stars import Stars
import pygame
from pygame.locals import *
from sys import exit
from random import randint
import sqlite3
import os.path
import pygame.locals as pl
import time
import ctypes


class GamePlay():
    def __init__(self):

        #public variables
        pygame.init()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #pygame.FULLSCREEN
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Space Invaders Clone")
        

        #private variables
        self.user32 = ctypes.windll.user32
        self.screensize = [self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1)]
        self.gameEnd = False
        self.direction = 0
        self.moveEnemyX = 0
        self.moveEnemyY = 0
        self.matrixOfEnemy = []
        self.controllerAnimation = False

    def makeMatrix(self):
        for i in range(60):
            coluna = i % 5
            linha = i // 5
            self.matrixOfEnemy.append(Enemy(i, (int(self.getScreenSize()[0]*0.3) +  linha * 55), ( coluna * 45), 100))

    
    def drawMatrix(self):
        i = 0
        for enemy in self.matrixOfEnemy:
            i +=1
            coluna = i % 5
            if (coluna  == 1):
                self.getScreen().blit(enemy.assets()[self.getAnimation()[0]],(enemy.getPositionX() , enemy.getPositionY()))
            elif (coluna >= 2 and coluna < 4):
                self.getScreen().blit(enemy.assets()[self.getAnimation()[1]],(enemy.getPositionX() , enemy.getPositionY()))
            else:
                self.getScreen().blit(enemy.assets()[self.getAnimation()[2]],(enemy.getPositionX() , enemy.getPositionY()))
    def getClock(self):
        return self.clock.tick(60) 

    def getScreen(self):
        return self.screen

    def getScreenSize(self):
        return self.screensize[0], self.screensize[1]

    def setDirection(self):
        if (max(enemy[0] for enemy in self.matrixOfEnemy) > self.getScreenSize[0]):
                self.direction = 1
        elif (min(enemy[0] for enemy in self.matrixOfEnemy) < 10):
            self.direction = 0
    
    def getAnimation(self):
        if self.controllerAnimation == True:
            return [1,3,5]
        else:
            return [0,2,4]

    def input(self, player):
        player.input()
        pass
    
    def update(self):
        for enemy in self.matrixOfEnemy:
            enemy.move2(self.getScreenSize(), enemy, self.direction)
            #print(enemy.getPositionX())
        #print(max(self.matrixOfEnemy))
        # self.setDirection()

  
    def render(self, stars, player):
        stars.draw(self.getScreen(), self.getScreenSize())
        player.draw(self.getScreen())
        
        self.drawMatrix()
        # print(self.matrixOfEnemy[0].getPositionX())
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    self.gameEnd = True
    
    def gameLoop(self):
        self.getScreen()
        contador = 0
        while self.gameEnd == False:
            
            if contador > 20:
                self.controllerAnimation = True
            if contador >= 20 and contador < 40:
                self.controllerAnimation = False
            if contador > 40:
                contador = 0
            contador += 1

            print(contador)
            self.getClock()
            self.input(player)
            self.update()
            self.render(stars, player)


gamePlay = GamePlay()
gamePlay.makeMatrix()
player = Player(gamePlay.getScreenSize(),gamePlay.getScreenSize()[0] * 0.5,gamePlay.getScreenSize()[1] * 0.95,100)
stars = Stars(400, gamePlay.getScreenSize())
gamePlay.gameLoop()

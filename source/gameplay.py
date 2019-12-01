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
        self.directionRight = False
        self.moveEnemyX = 0
        self.moveEnemyY = 0
        self.matrixOfEnemy = []
        self.sizeOfEnemy = 30
        self.spaceOfEnemy = [30,10]
        self.startPosition = [10,50]

    def makeMatrix(self):
        for i in range(60):
            coluna = i % 5
            linha = i // 5
            self.matrixOfEnemy.append(Enemy(i, (int(self.getScreenSize()[0]*0.3) +  linha * (15 + 30)), ( coluna * (15 + 30)), 100))

    
    def drawMatrix(self):
        for enemy in self.matrixOfEnemy:
            self.getScreen().blit(enemy.assets()[0],(enemy.getPositionX() , enemy.getPositionY()))
            
    def getClock(self):
        return self.clock.tick(60) 

    def getScreen(self):
        return self.screen

    def getScreenSize(self):
        return self.screensize[0], self.screensize[1]

    # def instaces(self):
    #     player = Player(self.getScreenSize())
    #     stars = Stars(200, self.getScreenSize())
    #     enemyPurple = EnemyPurple(0, 0,0,0)

    def input(self, player):
        player.input()
        pass
    
    def update(self):
        for enemy in self.matrixOfEnemy:
            enemy.move2(self.getScreenSize(), enemy)
            #return enemy
        pass
    
    def render(self, stars, player):
        stars.draw(self.getScreen(), self.getScreenSize())
        player.draw(self.getScreen())
        
        self.drawMatrix()
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
        while self.gameEnd == False:
            self.getClock()
            self.input(player)
            self.update()
            self.render(stars, player)


gamePlay = GamePlay()
player = Player(gamePlay.getScreenSize(),0,0,0)
stars = Stars(200, gamePlay.getScreenSize())
gamePlay.makeMatrix()
gamePlay.gameLoop()
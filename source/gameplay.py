from player import Player
from enemyBlue import EnemyBlue
from enemyGreen import EnemyGreen
from enemyPurple import EnemyPurple
from stars import Stars
from ship import *
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
            self.matrixOfEnemy.append(EnemyPurple(i, (linha * (15 + 30)), ( coluna * (15 + 30)), 100))

    
    def drawMatrix(self):
        for enemy in self.matrixOfEnemy:
            self.getScreen().blit(enemy.assets()[0],(enemy.getPositionX() , enemy.getPositionY()))
            enemy.setPositionX(enemy.getPositionX() + 5)
            if(enemy.getPositionX() > self.screensize[0]):
                enemy.setPositionX(0)


    def getClock(self):
        return self.clock.tick(60) 

    def getScreen(self):
        return self.screen

    def getScreenSize(self):
        return self.screensize[0], self.screensize[1]

    def instaces(self):
        player = Player(self.getScreenSize())
        stars = Stars(200, self.getScreenSize())
        enemyPurple = EnemyPurple(0, 0,0,0)

    def input(self, player):
        player.input()
        #player.shot(self.getScreen())
        pass
    
    def update(self):
        
        pass
    
    def render(self, stars, player):
        stars.draw(self.getScreen(), self.getScreenSize())
        player.draw(self.getScreen())
        
        self.drawMatrix()
        #player.shot(self.getScreen())
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
player = Player(gamePlay.getScreenSize())
stars = Stars(200, gamePlay.getScreenSize())
gamePlay.makeMatrix()
#gamePlay.render(stars)
gamePlay.gameLoop()
# #screensize
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# # init pygame
# pygame.init()
# screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
# clock = pygame.time.Clock()
# pygame.display.set_caption("Space Invaders Clone")
# #variables
# gameEnd = False
# directionRight = False
# moveEnemyX = 0
# moveEnemyY = 0
# matrixOfEnemy = []
# sizeOfEnemy = 30
# spaceOfEnemy = [30,10]
# startPosition = [10,50]
# def makeMatrix():
#     j=0
#     while j < 5:
#         i = 0
#         while i < 12:
#             matrixOfEnemy.append([startPosition[0] + i * (sizeOfEnemy+spaceOfEnemy[0]), startPosition[1] + j * (sizeOfEnemy+spaceOfEnemy[1])])
#             i += 1
#         j += 1
# makeMatrix()
# #instancias
# player = Player(screensize)
# enemyBlue = EnemyBlue()
# enemyGreen = EnemyGreen()
# enemyPurple = EnemyPurple()
# stars = Stars(200, screensize)
# gameplay = GamePlay()
# controllerFrameAnimation = 0
# frameAnimation = 0
# contador = 0
# def drawMatrix():
#     for i in range(len(matrixOfEnemy)):
#         if i < 12:
#             screen.blit(enemyPurple.assets()[frameAnimation],(enemyPurple.getPositionX() +  matrixOfEnemy[i][0], enemyPurple.getPositionY() + matrixOfEnemy[i][1]))
#         elif i >= 12 and i < 36:
#             screen.blit(enemyBlue.assets()[frameAnimation],(enemyBlue.getPositionX() +  matrixOfEnemy[i][0], enemyBlue.getPositionY() + matrixOfEnemy[i][1]))
#         elif i >= 36:
#             screen.blit(enemyGreen.assets()[frameAnimation],(enemyGreen.getPositionX() + matrixOfEnemy[i][0], enemyGreen.getPositionY() + matrixOfEnemy[i][1]))
# while not gameEnd:
#     directionRight = enemyPurple.getDirectionRight()
#     enemyPurple.move(screensize, matrixOfEnemy, sizeOfEnemy)
#     enemyBlue.move(screensize, matrixOfEnemy, sizeOfEnemy)
#     enemyGreen.move(screensize, matrixOfEnemy, sizeOfEnemy)
#     stars.draw(screen, screensize)
#     contador += 1
#     print(gameplay.getScreenSize())
#     #####
#     # if contador < 1000:
#     #     radomENemy = randint(0 , len(matrixOfEnemy)-1)
#     #     enemyPurple.shot(screen, radomENemy, moveEnemyX)
#     # else: 
#     #     contador = 0
#     controllerFrameAnimation += 1
#     if (controllerFrameAnimation > 20):
#         frameAnimation = 1
        
#     if controllerFrameAnimation > 40: 
#         frameAnimation = 0
#         controllerFrameAnimation = 0
#     clock.tick(30)
#     player.input()
#     player.draw(screen)
#     player.shot(screen)
#     drawMatrix()
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == K_ESCAPE:
#                 gameEnd = True
#     pygame.display.update()

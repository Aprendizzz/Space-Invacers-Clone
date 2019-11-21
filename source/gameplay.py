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

#screensize
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# init pygame
pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders Clone")
#variables
gameEnd = False
directionRight = False
moveEnemyX = 0
moveEnemyY = 0
matrixOfEnemy = []
sizeOfEnemy = 30
spaceOfEnemy = [30,10]
startPosition = [10,50]
def makeMatrix():
    j=0
    while j < 5:
        i = 0
        while i < 12:
            matrixOfEnemy.append([startPosition[0] + i * (sizeOfEnemy+spaceOfEnemy[0]), startPosition[1] + j * (sizeOfEnemy+spaceOfEnemy[1])])
            i += 1
        j += 1
makeMatrix()
#instancias
player = Player(screensize)
enemyBlue = EnemyBlue()
enemyGreen = EnemyGreen()
enemyPurple = EnemyPurple()
stars = Stars(200, screensize)
controllerFrameAnimation = 0
frameAnimation = 0
contador = 0
def drawMatrix():
    for i in range(len(matrixOfEnemy)):
        if i < 12:
            screen.blit(enemyPurple.assets()[frameAnimation],(enemyPurple.getPositionX() +  matrixOfEnemy[i][0], enemyPurple.getPositionY() + matrixOfEnemy[i][1]))
        elif i >= 12 and i < 36:
            screen.blit(enemyBlue.assets()[frameAnimation],(enemyBlue.getPositionX() +  matrixOfEnemy[i][0], enemyBlue.getPositionY() + matrixOfEnemy[i][1]))
        elif i >= 36:
            screen.blit(enemyGreen.assets()[frameAnimation],(enemyGreen.getPositionX() + matrixOfEnemy[i][0], enemyGreen.getPositionY() + matrixOfEnemy[i][1]))
while not gameEnd:
    directionRight = enemyPurple.getDirectionRight()
    enemyPurple.move(screensize, matrixOfEnemy, sizeOfEnemy)
    enemyBlue.move(screensize, matrixOfEnemy, sizeOfEnemy)
    enemyGreen.move(screensize, matrixOfEnemy, sizeOfEnemy)
    stars.draw(screen, screensize)
    contador += 1
    #####
    # if contador < 1000:
    #     radomENemy = randint(0 , len(matrixOfEnemy)-1)
    #     enemyPurple.shot(screen, radomENemy, moveEnemyX)
    # else: 
    #     contador = 0
    controllerFrameAnimation += 1
    if (controllerFrameAnimation > 20):
        frameAnimation = 1
        
    if controllerFrameAnimation > 40: 
        frameAnimation = 0
        controllerFrameAnimation = 0
    clock.tick(30)
    player.input()
    player.draw(screen)
    player.shot(screen)
    drawMatrix()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                gameEnd = True
    pygame.display.update()

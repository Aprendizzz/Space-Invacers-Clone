from player import Player
from enemyBlue import EnemyBlue
from enemyGreen import EnemyGreen
from enemyPurple import EnemyPurple
from background import BackGround
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

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders Clone")
gameEnd = False

matrix = []
def makeMatrix():
    j=0
    while j < 5:
        i = 0
        while i < 12:
            matrix.append((10+i*(30+35), 50+j*(30+10)))
            i += 1
        j += 1
makeMatrix()

player = Player(screensize)
enemyBlue = EnemyBlue()
enemyGreen = EnemyGreen()
enemyPurple = EnemyPurple()
stars = Stars(200, screensize)
contador = 0
frameAnimation = 0
x = 0
y = 0
def drawMatrix(matrix):
    for i in range(len(matrix)):
        if i < 12:
            screen.blit(enemyPurple.assets()[frameAnimation],(matrix[i][0], matrix[i][1]))
        elif i >= 12 and i < 36:
            screen.blit(enemyBlue.assets()[frameAnimation],(matrix[i][0], matrix[i][1]))
        elif i >= 36:
            screen.blit(enemyGreen.assets()[frameAnimation],(matrix[i][0], matrix[i][1]))
while not gameEnd:
    stars.draw(screen, screensize)
    contador += 1
    if (contador > 20):
        frameAnimation = 1
    if contador > 40: 
        frameAnimation = 0
        contador = 0
    clock.tick(30)
    player.input()
    player.draw(screen)
    player.shot(screen)
    drawMatrix(matrix)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                gameEnd = True
    pygame.display.update()
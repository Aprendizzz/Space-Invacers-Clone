from ship import *
#import pygame
class EnemyPurple(Ship):
    def __init__(self):
        super().__init__(200,200, 300)
        self.sprite = []
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyPurple/enemy1_1.png"))
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyPurple/enemy1_2.png"))
    def assets(self):
        return self.sprite
    def draw(self, screen, frameAnimation):
        #self.x += 3
        screen.blit(self.sprite[frameAnimation], (50,50))
        #pygame.time.delay(10)
        screen.blit(self.sprite[frameAnimation],(50, 50))

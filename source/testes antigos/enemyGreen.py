from ship import *

class EnemyGreen(Ship):

    def __init__(self):
        super().__init__(0,0, 250)
        self.sprite = []
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyGreen/enemy1_1.png"))
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyGreen/enemy1_2.png"))

    def assets(self):
        return self.sprite
    
    def move(self, screensize, matrixOfEnemy, sizeOfEnemy):
        if self.directionRight == True:
            self.setPositionX(int(self.getPositionX() + self.velocity))
        if self.directionRight == False:
            self.setPositionX(int(self.getPositionX() - self.velocity))
        if self.getPositionX() > (screensize[0] - max(enemy[0] for enemy in matrixOfEnemy) - sizeOfEnemy):
            self.setPositionY(int(self.getPositionY() + 5))
            self.directionRight = False
        if self.getPositionX() < (10 - min(enemy[0] for enemy in matrixOfEnemy)):
            self.setPositionY(int(self.getPositionY() + (self.velocity * 2)))
            self.directionRight = True
    def getDirectionRight(self):
        return self.directionRight

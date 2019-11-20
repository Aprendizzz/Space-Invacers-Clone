from ship import *

class EnemyPurple(Ship):

    def __init__(self):
        super().__init__(0,0, 300)
        self.sprite = []
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyPurple/enemy1_1.png"))
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyPurple/enemy1_2.png"))
        
    def assets(self):
        return self.sprite
    
    def move(self, screensize, matrixOfEnemy, sizeOfEnemy):
        if self.directionRight == True:
            self.setPositionX(int(self.getPositionX() + self.velocity))
        if self.directionRight == False:
            self.setPositionX(int(self.getPositionX() - self.velocity))
        if self.getPositionX() > (screensize[0] - max(enemy[0] for enemy in matrixOfEnemy) - sizeOfEnemy):
            print(self.getPositionY())
            self.setPositionY(int(self.getPositionY() + 5))
            self.directionRight = False
        if self.getPositionX() < (10 - min(enemy[0] for enemy in matrixOfEnemy)):
            print(self.getPositionY())
            self.setPositionY(int(self.getPositionY() + (self.velocity * 2)))
            self.directionRight = True
    def getDirectionRight(self):
        return self.directionRight

    def shot(self, screen, radomENemy, moveEnemyX):
        if self.shotBool == False:
            super().shot()
            self.shotY = super().getPositionShotY()
            self.shotBool = True
        if self.shotBool == True:
            self.shotY += 10
            pygame.draw.rect(screen, self.colorShot, (moveEnemyX + radomENemy, self.shotY,5,10))
        if self.shotY > 1000:
            self.shotBool = False

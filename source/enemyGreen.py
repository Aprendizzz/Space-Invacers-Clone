from ship import *

class EnemyGreen(Ship):
    def __init__(self):
        super().__init__(150,150, 250)
        self.sprite = []
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyGreen/enemy1_1.png"))
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyGreen/enemy1_2.png"))
    def assets(self):
        return self.sprite

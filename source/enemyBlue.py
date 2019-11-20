from ship import *

class EnemyBlue(Ship):
    def __init__(self):
        super().__init__(100,100, 200)
        self.sprite = []
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyBlue/enemy1_1.png"))
        self.sprite.append(pygame.image.load("../imagens/enemy/enemyBlue/enemy1_2.png"))
    def assets(self):
        return self.sprite

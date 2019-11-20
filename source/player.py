from ship import *
class Player(Ship):
    def __init__(self, screensize):
        super().__init__(50,screensize[1]*0.95, 100)
        self.sprite = pygame.image.load("../imagens/player/ship.png")
        self.shotY = 0
        self.shotBool = False
    def assets(self):
        pass
    def input(self):
        self.teclas = pygame.key.get_pressed()
        if self.teclas[K_LEFT]:
            self.setPositionX(int(self.getPositionX() - 2))
        if self.teclas[K_RIGHT]:
            self.setPositionX(round(self.getPositionX() + 2))
    def draw(self, screen):
        screen.blit(self.sprite, (self.getPositionX(), self.getPositionY()))
    def shot(self, screen):
        if self.shotBool == False:
            if self.teclas[K_UP] or self.teclas[K_SPACE]:
                super().shot()
                self.shotY = super().getPositionShotY()
                self.shotBool = True
        if self.shotBool == True:
            self.shotY -= 10
            pygame.draw.rect(screen, (0,255,127), (super().getPositionShotX(), self.shotY,5,10))
        if self.shotY < 0:
            self.shotBool = False
    def drawShot(self):
        pass

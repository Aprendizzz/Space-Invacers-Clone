from ship import *
class Player(Ship):

    def __init__(self, screensize):
        super().__init__(screensize[0] * 0.50,screensize[1]*0.95, 100)
        self.sprite = pygame.image.load("../imagens/player/ship.png")
        self.shotY = 0
        self.shotBool = False
        self.velocity = 10
        self.colorShot  = (0,255,127)
    
    def assets(self):
        pass

    def input(self):
        self.teclas = pygame.key.get_pressed()
        if self.teclas[K_LEFT]:
            self.setPositionX(int(self.getPositionX() - self.velocity))
        if self.teclas[K_RIGHT]:
            self.setPositionX(int(self.getPositionX() + self.velocity))
        if self.shotBool == False:
            if self.teclas[K_UP] or self.teclas[K_SPACE]:
                super().shot()
                self.shotY = super().getPositionShotY()
                self.shotBool = True
        if self.shotY < 0:
            self.shotBool = False
    
    def draw(self, screen):
        screen.blit(self.sprite, (self.getPositionX(), self.getPositionY()))
        if self.shotBool == True:
            self.shotY -= 10
            pygame.draw.rect(screen, self.colorShot, (super().getPositionShotX()+12, self.shotY,5,10))
    
    def shot(self, screen):
        pass

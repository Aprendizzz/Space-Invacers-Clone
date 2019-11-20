import pygame
from random import randint
class Stars:

    def __init__(self, numberStars, screensize):
        self.numberStars = numberStars
        self.stars = [
	        [randint(0, screensize[0]),randint(0, screensize[1])]
	        for x in range(self.numberStars)
        ]
    
    def draw(self, screen, screensize):
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0,0,0))
        for star in self.stars:
            pygame.draw.line(background,(255, 255, 255), (star[0], star[1]), (star[0], star[1]))
            star[1] = star[1] + 1
            if star[0] < 0:
                star[0] = screensize[0]
                star[1] = randint(0, screensize[1])
            if star[1] > screensize[1]:
                star[0] = randint(0, screensize[0])
                star[1] = 0
        screen.blit(background,(0,0))
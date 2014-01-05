import pygame
RED = (255, 0, 0)


class Hurdle:
    def __init__(self, screen):
        self.screen = screen
        self.x = 610
        self.y = 200
        self.width = 10
        self.height = 50

    def draw(self):
        pygame.draw.rect(self.screen, RED, [self.x, self.y, self.width, self.height])

    def update(self):
        if self.x > 0:
            self.x -= 10
        else:
            self.x = 610
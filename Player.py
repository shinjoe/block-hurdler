import pygame
BLUE = (0, 0, 255)


class Player:
    def __init__(self, screen):
        self.x = 0
        self.y = 175
        self.old_y = self.y
        self.old_old_y = self.y
        self.y_velo = 0
        self.y_accel = .5
        self.width = 30
        self.height = 75
        self.screen = screen
        self.jumping = False

    def draw(self):
        pygame.draw.rect(self.screen, BLUE, [self.x, self.old_old_y, self.width, self.height])
        pygame.draw.rect(self.screen, BLUE, [self.x, self.old_y, self.width, self.height])
        pygame.draw.rect(self.screen, BLUE, [self.x, self.y, self.width, self.height])

    def update(self):
        self.y_velo += self.y_accel
        self.old_old_y = self.old_y
        self.old_y = self.y
        self.y += self.y_velo

        if self.touching_ground():
            self.y = 175
            self.y_velo = 0
            self.jumping = False

    def jump(self):
        if not self.jumping:
            self.y_velo = -12
            self.jumping = True

    def touching_ground(self):
        return self.y >= 175

    def collides_with(self, hurdle):
        return not ((self.x > hurdle.x + hurdle.width) or
                    (self.x + self.width < hurdle.x) or
                    (self.y > hurdle.y + hurdle.height) or
                    (self.y + self.height < hurdle.y))


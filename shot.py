import pygame
from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        white_colour = (255, 255, 255)
        pygame.draw.circle(screen, white_colour, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
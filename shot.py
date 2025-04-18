from constants import *
from circleshape import CircleShape      # Import the base class
from player import *
import pygame


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "Green", self.position, self.radius, 2)

    def update(self, dt):
        # Add (velocity * dt) to position
        self.position += self.velocity * dt
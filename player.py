from constants import *
from circleshape import CircleShape      # Import the base class
import pygame
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # Call the parent class's constructor
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # Use Pygame's draw.polygon method to render the player
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # This is where we'll implement the vector math logic
        # to move the player in the direction they're facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.timer <= 0:
            shot_position = self.position  # Player's current position
            direction = pygame.Vector2(0, 1).rotate(self.rotation)  # Direction based on player's rotation
            bullet_velocity = direction * PLAYER_SHOOT_SPEED
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)  # Create the Shot
            shot.velocity = bullet_velocity                             # Set its velocity
            self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") # Displays startup message and screen variables to terminal
    
    clock = pygame.time.Clock() 

    # Object Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable 

    # Create player ONCE before the loop
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    # Create the asteroid field
    asteroid_field = AsteroidField()

    # Main game loop
    running = True
    while running:
        # Calculate dt at the beginning of each frame
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
    
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        # Update game objects
        updatable.update(dt)
    
        # Clear screen and draw
        pygame.Surface.fill(screen, (0,0,0))
        for entity in drawable:
            entity.draw(screen)
    
        # Update display
        pygame.display.flip()


if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        black_colour = (0, 0, 0)
        updatable.update(dt)
        for ast in asteroids_group:
            if ast.collisions(player1):
                raise SystemExit("Game over!")
            for bullet in shots:
                if ast.collisions(bullet):
                    ast.split()
                    bullet.kill()

        screen.fill(black_colour)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
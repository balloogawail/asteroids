import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    num_pass, num_fail = pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        for a in asteroids:
            if a.is_colliding_with(player):
                exit()
            for s in shots:
                if s.is_colliding_with(a):
                    s.kill()
                    a.split()
        pygame.display.flip()
        dt = clock.tick(60) / 1000            
                      
if __name__ == "__main__":
    main()

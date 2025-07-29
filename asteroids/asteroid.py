import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        if type(self.velocity) != pygame.math.Vector2:
            raise Exception(f"Expected Vector2, got {type(self.velocity)}")
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        right_split_vector = self.velocity.rotate(-angle)
        left_split_vector = self.velocity.rotate(angle)

        if type(right_split_vector) != pygame.math.Vector2 or type(left_split_vector) != pygame.math.Vector2:
            raise Exception(f"Right Type: {type(right_split_vector)}\nLeft Type: {type(left_split_vector)}")

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x = self.position.x
        y = self.position.y

        right_asteroid = Asteroid(x, y, new_radius)
        right_asteroid.velocity += self.velocity.rotate(-angle) * 1.2

        left_asteroid = Asteroid(x, y, new_radius)
        left_asteroid.velocity += self.velocity.rotate(angle) * 1.2
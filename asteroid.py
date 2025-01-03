

import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)
        
        as1 = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
        as2 = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
        
        as1.velocity = vec1 *1.2
        as2.velocity = vec2 *1.2
        
        
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt
import pygame, random

class Food:
    def __init__(self, x, y, size = 10):
        self.x = x
        self.y = y
        self.size = size
    
    def teleport(self):
        w, h = pygame.display.get_surface().get_size()
        self.x = random.randrange(0, w, self.size)
        self.y = random.randrange(0, h, self.size)

    def update(self):
        self.teleport()
    
    def render(self, surface):
        foodRect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(surface, [200, 0, 0], foodRect)

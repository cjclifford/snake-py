import pygame

class Player:
    def __init__(
        self,
        size = 10,
    ):
        self.vx, self.vy = 0, 1
        self.size = size
        self.length = 4
        self.reset()
    
    def reset(self):
        w, h = pygame.display.get_surface().get_size()
        self.segments = [[w / 2, h / 2]]
        self.grow(3)
        self.length = 4

    def grow(self, amount = 1):
        for i in range(amount):
            self.segments.append(
                [self.segments[i][0] - self.vx * self.size,
                self.segments[i][1] - self.vy * self.size]
            )
            self.length += 1
    
    def move(self):
        self.segments.insert(0, [self.segments[0][0] + self.vx * self.size, self.segments[0][1] + self.vy * self.size])
        self.segments.pop()
    
    def turn(self, vx, vy):
        if vx != -self.vx:
            self.vx = vx
        if vy != -self.vy:
            self.vy = vy

    def eat(self, food):
        head = self.segments[0]
        if head[0] == food.x and head[1] == food.y:
            return True
        return False
    
    def die(self):
        w, h = pygame.display.get_surface().get_size()
        for segment in self.segments:
            if segment[0] < 0 or segment[0] > w - 1:
                self.reset()
                return
            if segment[1] < 0 or segment[1] > h - 1:
                self.reset()
                return
            if self.segments.count(segment) > 1:
                self.reset()
                return


    
    def update(self):
        self.move()
        self.die()
    
    def render(self, surface):
        for segment in self.segments:
            segmentRect = pygame.Rect(segment[0], segment[1], self.size, self.size)
            pygame.draw.rect(surface, [0, 200, 0], segmentRect)

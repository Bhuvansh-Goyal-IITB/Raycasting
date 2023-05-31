import pygame
from settings import *

class Map(pygame.sprite.Sprite):
    def __init__(self, map):
        super().__init__()
        self.map = map
    
        self.rows, self.cols = len(self.map), len(self.map[0])
        self.tile_size = WIDTH // self.cols
        
        
        self.image = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))

    def draw_map(self):
        for y, row in enumerate(self.map):
            for x, val in enumerate(row):
                if val == 1:
                    pygame.draw.rect(self.image, "Black", pygame.Rect((x * self.tile_size, y * self.tile_size), (self.tile_size, self.tile_size)), border_radius=0)
                # else:
                #     pygame.draw.rect(self.image, "Black", pygame.Rect((x * self.tile_size, y * self.tile_size), (self.tile_size, self.tile_size)), width=BORDER)
                
    def update(self):
        self.draw_map()
        
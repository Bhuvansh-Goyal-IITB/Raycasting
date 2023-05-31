import pygame
import math
from settings import *

class Player:
    def __init__(self, game, initial_pos, size):
        self.game = game
        self.size = size
        self.move_vector = (0, 0)
        self.x, self.y = initial_pos
        self.direction = (1, 0)
        self.angle = 0
    
    def mouse_control(self):
        mx, my = pygame.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pygame.mouse.set_pos((WIDTH // 2, HEIGHT // 2))
        rel = pygame.mouse.get_rel()[0]
        rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, rel))
        self.angle += rel / 10

        
        rot_x = (math.cos(math.radians(self.angle))) 
        rot_y = (math.sin(math.radians(self.angle)))
        self.direction = (rot_x, rot_y)

    def update(self, input, dt):
        self.mouse_control()
        
        direction = (self.direction[0], self.direction[1])

        if input == None:
            self.move_vector = (0, 0)
            return

        rot_x = (direction[0] * math.cos(input)) - (direction[1] * math.sin(input))
        rot_y = (direction[0] * math.sin(input)) + (direction[1] * math.cos(input))

        speed = PLAYER_SPEED * dt
        self.move_vector = (rot_x * speed, rot_y * speed)
        
        self.x += self.move_vector[0]
        self.y += self.move_vector[1]

    def draw(self):
        pygame.draw.circle(self.game.screen, "White", (self.x, self.y), self.size // 2)
        pygame.draw.circle(self.game.screen, "Black", (self.x, self.y), self.size // 2, PLAYER_BORDER)

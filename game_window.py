import pygame
from game_states import GameStates
from settings import *
from player import Player
from map import Map
import math
from raycasting import DDA
import time

class GameWindow:
    def __init__(self, game):
        self.game = game
    
    @property
    def screen(self):
        return self.game.screen 
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.set_state(GameStates.quit)
            self.handle_event(event)

    def handle_event(self, event):
        pass

    def loop(self):
        raise NotImplementedError
    
class RayCastingGame(GameWindow):
    def __init__(self, game):
        super().__init__(game)
        
        self.player = Player(self, (WIDTH // 2, HEIGHT // 2), PLAYER_SIZE)
        
        self.map = Map(MAP)
        self.map_group = pygame.sprite.Group()
        self.map_group.add(self.map)

        self.input_vector = (0, 0)
    
    def handle_event(self, event):
        keys = pygame.key.get_pressed()
        self.input_vector = None
        if keys[pygame.K_w]:
            self.input_vector = math.radians(0)
        elif keys[pygame.K_a]:
            self.input_vector = math.radians(-90)
        elif keys[pygame.K_s]:
            self.input_vector = math.radians(180)
        elif keys[pygame.K_d]:
            self.input_vector = math.radians(90)

    def loop(self):
        clock = pygame.time.Clock()
        dt = 1
        points = []
        while self.game.state == GameStates.game:
            self.handle_events()

            self.screen.fill("White")

            self.map_group.update()

            self.player.update(self.input_vector, dt)
            
            self.map_group.draw(self.screen)
            self.player.draw()

            points.clear()
            points.append((self.player.x, self.player.y))
            angle = -(FOV // 2)
            for i in range(NUM_RAYS):
                radian_angle = math.radians(angle)
                rot_dx = (self.player.direction[0] * math.cos(radian_angle)) - (self.player.direction[1] * math.sin(radian_angle))
                rot_dy = (self.player.direction[0] * math.sin(radian_angle)) + (self.player.direction[1] * math.cos(radian_angle))
                point = DDA(rot_dx, rot_dy, (self.player.x, self.player.y), self.map.map, self.map.tile_size)
                points.append(point)
                perp_dist = math.sqrt(((point[0] - self.player.x) ** 2) + ((point[1] - self.player.y) ** 2)) * math.cos(radian_angle)
                height = HEIGHT * 100 / (perp_dist + 1e-30)
                if height > HEIGHT:
                    height = HEIGHT
                # pygame.draw.line(self.screen, "Red", (self.player.x, self.player.y), point, 1)
                # print(SCREEN_DIST)
                color = [255 / (1 + perp_dist ** 4 * 0.00000000002)] * 3
                # print(color)
                # pygame.draw.rect(self.screen, color, pygame.Rect((i * SCALE, (HEIGHT // 2) - (height // 2)), (SCALE, height)))
                angle += FOV / NUM_RAYS

                # pygame.draw.circle(self.screen, "Orange", point, 10, 3)
            pygame.draw.polygon(self.screen, "Yellow", points, width=0)
            #pygame.draw.polygon(self.screen, "Yellow", points, width=2)
  

            pygame.display.flip()

            pygame.display.set_caption(str(clock.get_fps()))    
            dt = clock.tick(0)
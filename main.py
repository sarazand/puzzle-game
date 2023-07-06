import pygame
import random 
import time
from sprite import *
from setting import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
    def new(self):
        pass

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick()
            self.events()
            self.draw()
            self.update()



    def update(self):
        pass

    def draw_graid(self):
         for row in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
              pygame.draw.line(self.screen, LIGHTGREY, (row,0), (row, GAME_SIZE*TILESIZE))
         for col in range(-1, GAME_SIZE * TILESIZE, TILESIZE):
              pygame.draw.line(self.screen, LIGHTGREY, (0,col), (GAME_SIZE*TILESIZE, col))


    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_graid()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type ==pygame.quit:
                pygame.quit()
                quit(0)



game = Game()
while True:
    game.new()
    game.run()
    
 

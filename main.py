from cgi import test
import pygame, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        # create x and y position
        self.x = random.randint(0, cell_no - 1)
        self.y = random.randint(0, cell_no - 1)
        self.pos = Vector2(self.x, self.y)
        # draw a square
    def draw_fruit(self):
        # create a rect
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        # draw the rect
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

pygame.init()
cell_size = 30
cell_no = 20
screen = pygame.display.set_mode((cell_no * cell_size, cell_no * cell_size))

# Title and Icon
pygame.display.set_caption("SNAKE")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# Time object to influence time in Pygame
clock = pygame.time.Clock()

# FRUIT class
fruit = FRUIT()

# Surface 
# test_surface = pygame.Surface((100, 200)) # size of surface
# test_surface.fill((0, 0, 250))

# Rectangle object
# test_rect = pygame.Rect((100, 200, 100, 100))  # (x, y, w, h)
# test_rect = test_surface.get_rect(center = (200, 250))
# place the rect around surface and put it in the middle of screen

running = True
while running:
    # draw all elements
    pygame.display.update()
    
    # background color RGB
    screen.fill((175, 215, 70))
    # screen.fill(pygame.Color('gold'))   # predefined color
    
    # test_rect.right += 1
    
    # background surface
    # screen.blit(test_surface, (200, 250))   # position of surface
                                            # top-left of the surface    
    # screen.blit(test_surface, test_rect)
    
    # Draw rectangle
    # pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)      # time-frame: number of time while loop runs per sec
    fruit.draw_fruit()
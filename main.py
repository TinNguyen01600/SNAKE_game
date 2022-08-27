from cgi import test
import sys
import pygame, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        # create a rect
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        # draw the rect
        # pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
        screen.blit(apple, fruit_rect)
    def randomize(self):    # create a random new position for the fruit
        self.x = random.randint(0, cell_no - 1)
        self.y = random.randint(0, cell_no - 1)
        self.pos = Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
    def draw_snake(self):
        for block in self.body:
            body_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), body_rect)
    # MOVING THE SNAKE
    # The head is moved to a new block, each following block 
    # is moved to the position of the previous block used to be
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]    # get all snake's body
            self.new_block = False
        else:
            body_copy = self.body[:-1]  # get all body except for the last block
        body_copy.insert(0, body_copy[0] + self.direction)  # add a new block head and direction
        self.body = body_copy[:]
    def add_block(self):
        self.new_block = True

# This class contains snake, fruit and other game logic
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_die()
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # reposition the fruit
            self.fruit.randomize()
            # add another block to the snake
            self.snake.add_block()
    def check_die(self):
        # check if snake is outside of the screen
        if not(0 <= self.snake.body[0].x <= cell_no) or not(0 <= self.snake.body[0].y <= cell_no):
            self.game_over()
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()

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

apple = pygame.image.load('apple.png').convert_alpha()

# Surface 
# test_surface = pygame.Surface((100, 200)) # size of surface
# test_surface.fill((0, 0, 250))

# Rectangle object
# test_rect = pygame.Rect((100, 200, 100, 100))  # (x, y, w, h)
# test_rect = test_surface.get_rect(center = (200, 250))
# place the rect around surface and put it in the middle of screen

main_game = MAIN()

# Event 
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)   # trigger SCREEN_UPDATE event every 150ms
                                            # 150ms is the speed of the moving snake
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
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # make sure we dont push UP when snake's moving downward
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
    clock.tick(60)      # time-frame: number of time while loop runs per sec
    main_game.draw_elements()
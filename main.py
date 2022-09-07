from cgi import test
import sys
from tkinter import CENTER
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
        
        self.head_up = pygame.image.load('head_up.png').convert_alpha()
        self.head_down = pygame.image.load('head_down.png').convert_alpha()
        self.head_right = pygame.image.load('head_right.png').convert_alpha()
        self.head_left = pygame.image.load('head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('body_bl.png').convert_alpha()
        
        self.crunch_sound = pygame.mixer.Sound('crunch.wav')
          
    def draw_snake(self):
        # 3. Snake head direction update
        self.update_head_graphics()
        
        # 4. Snake tail direction update
        self.update_tail_graphics()
        
        # We have to look for each body block AND (its before and after block)
        for index, block in enumerate(self.body):
            # 1. We still need a rect for positioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            # 2. What direction is the face heading
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)   
            else:
                # pygame.draw.rect(screen, (150, 100, 100), block_rect)
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:    # if 2 adjecent blocks has same x, they're both vertical
                    screen.blit(self.body_vertical, block_rect)
                if previous_block.y == next_block.y:    # if 2 adjecent blocks has same x, they're both horizontal
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if (previous_block.x == -1 and next_block.y == -1) or (previous_block.y == -1 and next_block.x == -1):
                        screen.blit(self.body_tl, block_rect)
                    elif (previous_block.x == -1 and next_block.y == 1) or (previous_block.y == 1 and next_block.x == -1):
                        screen.blit(self.body_bl, block_rect)
                    elif (previous_block.x == 1 and next_block.y == -1) or (previous_block.y == -1 and next_block.x == 1):
                        screen.blit(self.body_tr, block_rect)
                    elif (previous_block.x == 1 and next_block.y == 1) or (previous_block.y == 1 and next_block.x == 1):
                        screen.blit(self.body_br, block_rect)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0):   self.head = self.head_left
        elif head_relation == Vector2(-1,0):self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1):self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0):   self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0):self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1):self.tail = self.tail_down    
        
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
        
    def play_sound(self) :
        self.crunch_sound.play()

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
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # reposition the fruit
            self.fruit.randomize()
            # add another block to the snake
            self.snake.add_block()
            self.snake.play_sound()
    def check_die(self):
        # check if snake is outside of the screen
        if not(0 <= self.snake.body[0].x < cell_no) or not(0 <= self.snake.body[0].y < cell_no):
            self.game_over()
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()
    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_no//2):
            for col in range(cell_no//2):
                grass_rect1 = pygame.Rect(col * 2 * cell_size, row * 2 * cell_size, cell_size, cell_size)
                grass_rect2 = pygame.Rect((col * 2 + 1) * cell_size, (row * 2 + 1) * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, grass_color, grass_rect1)
                pygame.draw.rect(screen, grass_color, grass_rect2)
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)  # there is 3 blocks initially
        score_surface = game_font.render(score_text, True, (255,0,0))
        score_x = int(cell_size * cell_no - 60)
        score_y = int(cell_size * cell_no - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left - 6, apple_rect.top - 6, apple_rect.width + score_rect.width + 15, apple_rect.height + 12)
        
        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (0,0,0), bg_rect, 2)
        
                
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_no = 20
screen = pygame.display.set_mode((cell_no * cell_size, cell_no * cell_size))

# Title and Icon
pygame.display.set_caption("SNAKE")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# Time object to influence time in Pygame
clock = pygame.time.Clock()

apple = pygame.image.load('apple.png').convert_alpha()

game_font = pygame.font.Font('One_Crayon.ttf', 30)

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
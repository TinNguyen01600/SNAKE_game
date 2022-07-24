import pygame

pygame.init()
screen = pygame.display.set_mode((400, 500))

# Title and Icon
pygame.display.set_caption("SNAKE")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# Time object to influence time in Pygame
clock = pygame.time.Clock()

# Surface 
test_surface = pygame.Surface((100, 200)) # size of surface
test_surface.fill((0, 0, 250))

running = True
while running:
    # draw all elements
    pygame.display.update()
    
    # background color RGB
    screen.fill((175, 215, 70))
    # screen.fill(pygame.Color('gold'))   # predefined color
    
    # background surface
    screen.blit(test_surface, (200, 250))   # position of surface
                                            # top-left of the surface    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)      # time-frame: number of time while loop runs per sec
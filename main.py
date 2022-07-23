import pygame

pygame.init()
screen = pygame.display.set_mode((400, 500))

# Title and Icon
pygame.display.set_caption("SNAKE")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# Time object to influence time in Pygame
clock = pygame.time.Clock()

running = True
while running:
    # draw all elements
    pygame.display.update()
    # background color RGB
    screen.fill((0,0,0))    # screen should be drawn first, below all others
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)      # time-frame: number of time while loop runs per sec
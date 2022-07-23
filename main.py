import pygame

pygame.init()
screen = pygame.display.set_mode((400, 500))

running = True
while running:
    # draw all elements
    pygame.display.update()
    # background color RGB
    screen.fill((0,0,0))    # screen should be drawn first, below all others
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
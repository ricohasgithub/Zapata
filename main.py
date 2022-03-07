import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()
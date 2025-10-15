import pygame 

"""
Gestion de la fenêtre: même fonctionnement qu'avec sdl2
Initialisation de pygame
"""
#initialisation pygame + gestion fenêtre / fps
pygame.init
screen = pygame.display.set_mode((900,900))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("purple")


    clock.tick(60)
#Ne pas supprimer éssentiel au programme d'initialisation
running()
pygame.quit
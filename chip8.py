import pygame 
from fonts import chip8_fontset
import numpy
"""
Gestion de la fenêtre: même fonctionnement qu'avec sdl2
Initialisation de pygame
"""
#initialisation pygame + gestion fenêtre / fps
pygame.init
screen = pygame.display.set_mode((64,32)) #affichage du chip-8
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Chip8')
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    clock.tick(60)

#chip-8 
"""
Mémoire: 4Ko
Screen: 64x32
16 bits
adressage en 16 bits w/
8 bit delay timer (60hz)
8 bit sound timer w/
8 bit of variable registers 
"""
#Mémoire du chip-8
memory = [0] * 4096
for i, byte in enumerate(chip8_fontset):
    memory[0x50 + i] = byte

#Sound Timer 8 bits:


















#Ne pas supprimer éssentiel au programme d'initialisation
pygame.quit
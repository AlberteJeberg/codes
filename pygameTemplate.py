import pygame
import random

#constants
WIDHT = 1280
HEIGHT = 800
FPS = 30

# DEFINE COLORS
WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#initializer pygame
pygame.init()
#initializer mixer der bruges til lyd
pygame.mixer.init()

#sets screen to width og height
screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Binary Bastards")
#funktion som skal styre tiden/overholde FPS
clock = pygame.time.Clock()

#Laver en gruppe for alle vores sprites
all_sprites = pygame.sprite.Group()

# the GAME LOOP

#GameLoop, starter med en boolean, for at while loop kan stoppe.
running = True

while running:
    #keep the loop running at the right speed
    clock.tick(FPS)
    #process input (event).
    #opretter funktion som giver events 'adgang' til at ske altid
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
    #update - travl hvis mange sprites. Derfor group sprites (all_sprites)
    all_sprites.update()
    #draw or render
    screen.fill(BLACK)
    #tegner hele gruppen all_sprites
    all_sprites.draw(screen)
    #double buffering --> display skal altid flippes EFTER
    # noget er tegnet
    pygame.display.flip()

#command som kan kaldes fra loop, og lukker vinduet
pygame.quit()

import pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255,165,0)

PI = 3.141592653



size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MC Birdie spil")

done= False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
# Draw on the screen a line from (0,0) to (100,100)
# 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
# Draw on the screen several lines from (0,10) to (100,110)
# 5 pixels wide using a loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)
# Draw a rectangle
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)
# Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
# Draw an arc as part of an ellipse.
# Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI / 2, 2)
    pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI / 2, PI, 2)
    pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)
# This draws a triangle using the polygon command
    pygame.draw.polygon(screen, ORANGE, [[100, 100], [0, 200], [200, 200]], 5)
# Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
# Render the text. "True" means anti-aliased text.
# Black is the color. This creates an image of the
# letters, but does not put it on the screen
    text = font.render("FYN FOR THE WIN!!!", True, BLACK)
# Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])
    text2 = font.render("SOENDERJYLLAND!!!", True, RED)
    screen.blit(text2, [150, 350])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

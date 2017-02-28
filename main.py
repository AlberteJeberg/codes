# platformer game
# as pg renames pygame to pg (so we have to type less)
# yoyoyoyo
import pygame as pg
import random
# smartere end import from
from settings import *
from sprites import *

class Game:
    #initialize game window
    def __init__(self):
        # python command that says do nothing (for empty def)
        #initializer pygame
        pg.init()
        #initializer mixer der bruges til lyd
        pg.mixer.init()
        # self. is needed for class variables
        self.screen = pg.display.set_mode((WIDHT, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        #start new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        # add player from sprites player class
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            # star * is a smart way to "explode the list"
            # else we would have to (plat[0], y, w, h) call all elements in the list
            # individually. when we exlode the list it breaks it up for us
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()
    def run(self):
    #game loop

    #keep the loop running at the right speed
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
    #game loop update
        self.all_sprites.update()
        #check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                # if player reaches top 1/4 of the screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
        #spawn new platforms to keep some average number
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDHT-width),
                            random.randrange(-75, -30),
                            width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)


    def events(self):
    #game loop events
        #process input (event)
        for event in pg.event.get():
            #check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
    #game loop draw
        #draw or render
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        #double buffering --> display skal altid flippes EFTER
        # noget er tegnet
        pg.display.flip()
    def show_start_screen(self):
        #game splash start screen
        pass
    def show_gameover_screen(self):
        #game over/continuer
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_gameover_screen()
pg.quit()

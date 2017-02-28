#sprite classes for platformer game
import pygame as pg
from settings import *
vec = pg.math.Vector2
#laver en player class sprite
class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        # er en referance saa player kan se indeholdet i game class (bruges saa vi kan tjekke om player rammer platformen)
        self.game = game
        # saetter stoerrelsen
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        # saetter player rect i midten af skaermen
        self.rect.center = (WIDHT / 2, HEIGHT / 2)
        self.pos = vec(WIDHT / 2, HEIGHT /2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        # jump only if standing on platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        #
        self.acc = vec(0, PLAYER_GRAV) #x and y 0.5 makes the player move downwards (gravity)
        #checker om der er blevet tastet paa en tastet
        # vores rect rykkes 5 pixel til hoejre eller venstre naar pilenetasterne bruges
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        # her laves fysike love til player

        # apply friction
        # .x sets friction on the x axis only (so we accelerete when falling)
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #acceleration
        self.vel += self.acc

        self.pos += self.vel + 0.5 * self.acc
        #wrap around the side of the screen
        # if position is more than WIDHT then its setted to 0
        if self.pos.x > WIDHT:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDHT
        # set to midbottom so it can stand on the platforms
        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

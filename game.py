from obj import Obj, Hero
import pygame


class Game:

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.crystal = pygame.sprite.Group()
        self.all_platforms = pygame.sprite.Group()

        self.bg = Obj('assets/bg.png', 0, 0, self.all_sprites)

        self.tree1 = Obj('assets/tree1.png', 80, 250, self.all_sprites)
        self.tree2 = Obj('assets/tree2.png', 450, 250, self.all_sprites)
        self.tree3 = Obj('assets/tree1.png', 1060, 250, self.all_sprites)

        self.plat1 = Obj('assets/plat1.png', 50, 550, self.all_sprites, self.all_platforms)
        self.plat2 = Obj('assets/plat3.png', 430, 550, self.all_sprites, self.all_platforms)
        self.plat3 = Obj('assets/plat2.png', 1080, 550, self.all_sprites, self.all_platforms)

        self.crystal1 = Obj('assets/crystal.png', 520, 400, self.all_sprites, self.crystal)
        self.crystal2 = Obj('assets/crystal.png', 870, 400, self.all_sprites, self.crystal)
        self.crystal3 = Obj('assets/crystal.png', 1155, 400, self.all_sprites, self.crystal)

        self.enemy1 = Obj('assets/enemy0.png', 520, 502, self.all_sprites, self.enemy)

        self.player = Hero('assets/idle0.png', 100, 250, self.all_sprites)

        self.hud = Obj('assets/hud.png', 50, 50, self.all_sprites)

    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.all_sprites.update()
        self.player.colisions(self.all_platforms, False)

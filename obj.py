import pygame


class Obj(pygame.sprite.Sprite):

    def __init__(self, image,  *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(image)



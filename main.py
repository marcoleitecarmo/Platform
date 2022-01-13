import pygame


class Main:

    def __init__(self):
        self.window = pygame.display.set_mode([1280, 720])
        pygame.display.set_caption('Platform')

        self.loop = True
        self.fps = pygame.time.Clock()

    def draw(self):
        pass

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            self.fps.tick(30)

Main().update()


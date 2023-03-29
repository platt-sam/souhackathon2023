import sys
import pygame


#display settings
DEFAULT_IMAGE_SIZE = (300, 300)
FPS = 120
HEIGHT = 1000
WIDTH = 1600

#images
BG_IMAGE_PATH = 'pics/shakespear.jpg'


class Game:
    def __init__(self):

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juliet's Balcony Slot Machine")
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)

        #to do: creat machine class
        self.machine = Machine()
        self.delta_time = 0

        #sound
        main_sound = pygame.mixer.sound('sound/royal.mp3')
        main_sound.play(loops = -1)

    def run(self):

        self.start_time = pygame.time.get_ticks()

        while True:
            #handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #time variables
            self.delta_time = (pygame.time.get_ticks() - slef. start_time) /1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.screen.blit(self.bg_image, (0, 0))
            self.machine.update(self.delta_time)
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
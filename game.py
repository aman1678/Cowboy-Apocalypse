import pygame
import sys
from sprites import Player, Zombie

class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Cowboy Apocalypse")

        self.clock = pygame.time.Clock()

    def run(self):
        dt = 0

        cords =[(0,0),(1230,0),(1230,600),(0,600)]
        zombies = [Zombie(x,y) for x,y in cords]
        player = Player()
        sand = pygame.rect.Rect(0,650,1280,70)

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill((251,165,51))
            pygame.draw.rect(self.screen,(194,178,128),sand)
            keys = pygame.key.get_pressed()

            player.move(keys, dt)
            for zombie in zombies:
                zombie.move(player.rect, dt)
            
            pygame.draw.rect(self.screen, (255, 0, 0), player.rect)
            for zombie in zombies:
                pygame.draw.rect(self.screen,(0,255,0), zombie.rect)
            self.screen.blit(player.image, player.rect)
            
            pygame.display.flip()
            dt = self.clock.tick(60) / 1000        
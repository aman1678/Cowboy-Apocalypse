import pygame
import sys
from sprites import Player, Zombie, Bullet

class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Cowboy Apocalypse")

        self.clock = pygame.time.Clock()

    def run(self):
        dt = 0

        shoot_cd = 250
        last_shot_time = 0
        bullets = []

        cords = [(0,0),(1230,0)]
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

            if keys[pygame.K_SPACE]:
                if pygame.time.get_ticks() - last_shot_time >= shoot_cd:
                    bullets.append(Bullet(player.arm_rect.x, player.arm_rect.y + 5, 
                                        player.last_key, True))
                    last_shot_time = pygame.time.get_ticks()
                
            pygame.draw.rect(self.screen, (255, 0, 0), player.rect)

            for bullet in bullets:
                if bullet.shoot:
                    pygame.draw.rect(self.screen, (0,0,0), bullet.rect)
                    bullet.move(dt)

            for zombie in zombies:
                if zombie.health > 0:
                    pygame.draw.rect(self.screen, (0,255,0), zombie.rect)
                    self.screen.blit(zombie.image, zombie.rect)

                for bullet in bullets:
                    if zombie.health and zombie.collision(bullet.rect.x, bullet.rect.y) and bullet.shoot:
                        bullet.shoot = False
                        zombie.health -= 10
        
            self.screen.blit(player.image, player.rect)
            self.screen.blit(player.arm_sprite, player.arm_rect)
            
            pygame.display.flip()
            dt = self.clock.tick(60) / 1000        
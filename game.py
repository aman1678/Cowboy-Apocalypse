import pygame
import sys
import random
from sprites import Player, Zombie, Bullet, Background
from utilities import Platform, Audio, display_message

SAND = (194,178,128)
SKY = (224,123,57)

class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Cowboy Apocalypse")
        self.clock = pygame.time.Clock()

    def run(self):
        
        # Player init
        player = Player()

        # Shooting setup
        shoot_cd = 250
        last_shot_time = 0
        reload_cd = 3250
        bullets = []

        # Zombie spawn setup
        cords = [(-100,650),(1280,650)]
        zombies = [Zombie(cord) for cord in cords]

        # General setup
        sand = pygame.rect.Rect(0,650,1280,70)
        plat = Platform()
        sounds = Audio()
        background = Background()
        dt = 0

        # Main game loop
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if random.randint(0,500) == 0:
                zombies.append(Zombie(random.choice(cords)))

            self.screen.fill(SKY)
            self.screen.blit(background.image, (0,0))
            pygame.draw.rect(self.screen,SAND,sand)
            keys = pygame.key.get_pressed()

            # Player and zombie movement
            player.move(keys, dt, plat)
            for zombie in zombies:
                zombie.move(player.rect, dt)

            # Reload mechanic
            if player.shots == 6:
                player.reload = True
                player.shots = 0
                sounds.reload.play()
            elif pygame.time.get_ticks() - last_shot_time >= reload_cd:
                player.reload = False

            # Ammo display
            if player.reload:
                display_message("Ammo: Reloading...", self.screen,(255,255,255),(10,10),"tl")
            else:
                display_message(f"Ammo: {6-player.shots}",self.screen,(255,255,255),(10,10),"tl")

            # Shooting mechanics
            if keys[pygame.K_SPACE]:
                t = pygame.time.get_ticks()
                if not player.reload:
                    if t - last_shot_time >= shoot_cd:
                        bullets.append(Bullet(player.arm_rect.x, player.arm_rect.y + 5, 
                                            player.last_key, True))
                        player.shots += 1
                        last_shot_time = pygame.time.get_ticks()
                        sounds.gun_shot.play()

            pygame.draw.rect(self.screen, (255, 0, 0), player.rect)

            # Drawing everything to screen
            for bullet in bullets:
                if bullet.shoot:
                    self.screen.blit(bullet.image, bullet.rect)
                    bullet.move(dt)

            for zombie in zombies:
                if zombie.health > 0:
                    pygame.draw.rect(self.screen, (0,255,0), zombie.rect)
                    self.screen.blit(zombie.image, zombie.rect)

                for bullet in bullets:
                    if zombie.health and zombie.collision(bullet.rect.x, bullet.rect.y) and bullet.shoot:
                        bullet.shoot = False
                        zombie.health -= 10

            
            pygame.draw.rect(self.screen,(194,178,128), plat.rect)
            self.screen.blit(player.image, player.rect)
            self.screen.blit(player.arm_sprite, player.arm_rect)
            
            pygame.display.flip()
            dt = self.clock.tick(60) / 1000        
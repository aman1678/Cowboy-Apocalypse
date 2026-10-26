import pygame
import random

PLATFORM_WIDTH = 500
PLATFORM_HEIGHT = 50

class Platform():
    def __init__(self):
        self.rect = pygame.rect.Rect(random.randint(320,960),random.randint(270,430),PLATFORM_WIDTH,PLATFORM_HEIGHT)

class Menu():
    def __init__(self, screen):
        self.screen = screen

class Audio():
     def __init__(self):
        pygame.mixer.init()

        self.gun_shot = pygame.mixer.Sound("./assets/sounds/gunshot.mp3")
        self.gun_shot.set_volume(0.5)
        self.reload = pygame.mixer.Sound("./assets/sounds/gun_reload.mp3")
        self.reload.set_volume(0.5)

        
def display_message(message, screen, color, pos, zone):
            font = pygame.font.Font(None, 36)
            
            message_surface = font.render(message, True, color)
            message_rect = message_surface.get_rect()

            if zone == "tl":
                message_rect.topleft = pos
            elif zone == "c":
                message_rect.center = pos
            screen.blit(message_surface, message_rect)
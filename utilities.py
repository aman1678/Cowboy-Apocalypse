import pygame
import random

PLATFORM_WIDTH = 500
PLATFORM_HEIGHT = 50

class Platform():
    def __init__(self):
        self.rect = pygame.rect.Rect(random.randint(320,960),random.randint(180,540),PLATFORM_WIDTH,PLATFORM_HEIGHT)


    

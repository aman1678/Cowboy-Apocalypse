import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./assets/cowboy.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        self.rect = self.image.get_rect(center=(640,360))
        self.flip = True

    def move(self, keys, dt):

        if keys[pygame.K_a]:
            self.rect.move_ip(-300 * dt, 0)
            if self.flip:
                self.image = pygame.transform.flip(self.image, True, False)
                self.flip = False

        if keys[pygame.K_w]:
            self.rect.move_ip(0, -300 * dt)
        else:
            if int(self.rect.bottom) <= 650:
                self.rect.move_ip(0, 300 * dt)

        if keys[pygame.K_d]:
            self.rect.move_ip(300 * dt, 0)
            if not self.flip:
                self.image = pygame.transform.flip(self.image, True, False)
                self.flip = True

class Zombie(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        """uncomment when image is ready"""
        # super().__init__()

        # self.image = pygame.image.load("./assets/zombie.png").convert_alpha()
        # self.image = pygame.transform.scale_by(self.image, 3)
        # self.rect = self.image.get_rect(center=(640,360))
        # self.flip = True

        self.rect = pygame.rect.Rect(x,y,50,50)

    def move(self, target, dt):
        if self.rect.x > target.x:
            self.rect.x -= 100 * dt
        elif self.rect.x < target.x:
            self.rect.x += 100 * dt
        if self.rect.y > target.y:
            self.rect.y -= 100 * dt
        elif self.rect.y < target.y:
            self.rect.y += 100 * dt
        
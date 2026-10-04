import pygame

BASE_PATH = "./assets/"

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image0 = pygame.image.load(BASE_PATH + "cowboy/cowboy.png").convert_alpha()
        self.image = self.image0
        self.image1 = pygame.image.load(BASE_PATH + "cowboy/cowboy_walk_1.png").convert_alpha()
        self.image2 = pygame.image.load(BASE_PATH + "cowboy/cowboy_walk_2.png").convert_alpha()
        self.arm_sprite = pygame.image.load(BASE_PATH + "cowboy/arm.png").convert_alpha()

        self.arm_sprite = pygame.transform.scale_by(self.arm_sprite, 3)
        self.image0 = pygame.transform.scale_by(self.image0, 3)
        self.image = pygame.transform.scale_by(self.image, 3)
        self.image1 = pygame.transform.scale_by(self.image1, 3)
        self.image2 = pygame.transform.scale_by(self.image2, 3)

        self.rect = self.image.get_rect(center=(640,360))
        self.arm_rect = self.arm_sprite.get_rect(topleft=(self.rect.x + 65, self.rect.y + 57))


        self.flip = True
        self.delay = 12
        self.last_key = "d"

    def move(self, keys, dt):

        if keys[pygame.K_a]:
            self.rect.move_ip(-300 * dt, 0)
            self.arm_rect.x = self.rect.x - 42
            self.last_key = "a"
            if self.delay == 0:
                if self.image == self.image1:
                    self.image = self.image2
                else:
                    self.image = self.image1
                self.delay = 12
            if self.flip:
                self.arm_sprite = pygame.transform.flip(self.arm_sprite, True, False)
                self.image1 = pygame.transform.flip(self.image1, True, False)
                self.image2 = pygame.transform.flip(self.image2, True, False)
                self.flip = False
            self.delay -= 1

        if keys[pygame.K_w]:
            self.rect.move_ip(0, -300 * dt)
        else:
            if int(self.rect.bottom) <= 650:
                self.rect.move_ip(0, 300 * dt)

        if keys[pygame.K_d]:
            self.rect.move_ip(300 * dt, 0)
            self.arm_rect.x = self.rect.x + 65
            self.last_key = "d"
            if self.delay == 0:
                if self.image == self.image1:
                    self.image = self.image2
                else:
                    self.image = self.image1
                self.delay = 12
            if not self.flip:
                self.arm_sprite = pygame.transform.flip(self.arm_sprite, True, False)
                self.image1 = pygame.transform.flip(self.image1, True, False)
                self.image2 = pygame.transform.flip(self.image2, True, False)
                self.flip = True
            self.delay -= 1

        if not (keys[pygame.K_a] + keys[pygame.K_d]):
            if self.last_key == "a":
                self.image = pygame.transform.flip(self.image0, True, False)
            else:
                self.image = self.image0
            
        self.arm_rect.y = self.rect.y + 57

class Zombie(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(BASE_PATH + "zombie.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 5)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.flip = True

    def move(self, target, dt):
        if self.rect.x > target.x:
            self.rect.x -= 100 * dt
        elif self.rect.x < target.x:
            self.rect.x += 100 * dt
        if self.rect.y > target.y:
            self.rect.y -= 100 * dt
        elif self.rect.y < target.y:
            self.rect.y += 100 * dt
        
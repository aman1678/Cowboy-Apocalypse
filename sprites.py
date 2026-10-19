import pygame

BASE_PATH = "./assets/"

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
    
        self.image0 = pygame.image.load(BASE_PATH + "cowboy/cowboy.png").convert_alpha()
        self.image1 = pygame.image.load(BASE_PATH + "cowboy/cowboy_walk_1.png").convert_alpha()
        self.image2 = pygame.image.load(BASE_PATH + "cowboy/cowboy_walk_2.png").convert_alpha()
        self.arm_sprite = pygame.image.load(BASE_PATH + "cowboy/arm.png").convert_alpha()
        self.image = self.image0

        self.arm_sprite = pygame.transform.scale_by(self.arm_sprite, 3)
        self.image0 = pygame.transform.scale_by(self.image0, 3)
        self.image1 = pygame.transform.scale_by(self.image1, 3)
        self.image2 = pygame.transform.scale_by(self.image2, 3)
        self.image = pygame.transform.scale_by(self.image, 3)

        self.rect = self.image.get_rect(bottomleft=(640,650))
        self.arm_rect = self.arm_sprite.get_rect(topleft=(self.rect.x + 65, self.rect.y + 57))

        self.flip = True
        self.delay = 8
        self.last_key = "d"
        self.jump = False
        self.reload = False
        self.shots = 0

    def move(self, keys, dt, plat):

        # Left motion
        if keys[pygame.K_a]:
            self.rect.x -= 500 * dt
            self.arm_rect.x = self.rect.x - 42
            self.last_key = "a"
        
            if self.delay == 0:
                if self.image == self.image1:
                    self.image = self.image2
                else:
                    self.image = self.image1

                self.delay = 8
        
            if self.flip:
                self.arm_sprite = pygame.transform.flip(self.arm_sprite, True, False)
                self.image1 = pygame.transform.flip(self.image1, True, False)
                self.image2 = pygame.transform.flip(self.image2, True, False)
                self.flip = False

            self.delay -= 1
            
        # Right motion 
        elif keys[pygame.K_d]:
            self.rect.x += 500 * dt 
            self.arm_rect.x = self.rect.x + 65
            self.last_key = "d"

            if self.delay == 0:
                if self.image == self.image1:
                    self.image = self.image2
                else:
                    self.image = self.image1

                self.delay = 8

            if not self.flip:
                self.arm_sprite = pygame.transform.flip(self.arm_sprite, True, False)
                self.image1 = pygame.transform.flip(self.image1, True, False)
                self.image2 = pygame.transform.flip(self.image2, True, False)
                self.flip = True

            self.delay -= 1

        # Jumping and gravity 
        if keys[pygame.K_w] and int(self.rect.bottom) >= 650:
            self.jump = True
        else:
            if int(self.rect.bottom) < 650 and not self.jump:
                if not self.rect.colliderect(plat.rect): 
                    self.rect.y += 1000 * dt

        if self.jump and int(self.rect.bottom) >= 360:
            self.rect.y -= 1000 * dt
        else:
            self.jump = False

        # Standing image if no motion
        if not (keys[pygame.K_a] + keys[pygame.K_d]):
            if self.last_key == "a":
                self.image = pygame.transform.flip(self.image0, True, False)
            else:
                self.image = self.image0
            
        self.arm_rect.y = self.rect.y + 57

class Zombie(pygame.sprite.Sprite):
    
    def __init__(self, cord):
        super().__init__()

        self.image0 = pygame.image.load(BASE_PATH + "/zombie/zombie.png").convert_alpha()
        self.image1 = pygame.image.load(BASE_PATH + "/zombie/zombie_1.png").convert_alpha()
        self.image2 = pygame.image.load(BASE_PATH + "/zombie/zombie_2.png").convert_alpha()
        self.image = self.image0

        self.image0 = pygame.transform.scale_by(self.image0, 5)
        self.image1 = pygame.transform.scale_by(self.image1, 5)
        self.image2 = pygame.transform.scale_by(self.image2, 5)
        self.image = pygame.transform.scale_by(self.image, 5)

        self.rect = self.image.get_rect(bottomleft=cord)

        self.flip = True
        self.delay = 30
        self.last_key = "a"
        self.health = 50

    def collision(self, x,y):
        return pygame.rect.Rect.collidepoint(self.rect, x, y)
    
    def move(self, target, dt):
    
        # Zombie's x,y "follow" target's x,y (in this case the player's)

        if self.rect.x > target.x:
            self.rect.x -= 100 * dt
            self.last_key = "a"

            if self.delay == 0:
                if self.image == self.image1:
                    self.image = self.image2
                else:
                    self.image = self.image1
                self.delay = 30

            if not self.flip:
                self.image1 = pygame.transform.flip(self.image1, True, False)
                self.image2 = pygame.transform.flip(self.image2, True, False)
                self.flip = True

            self.delay -= 1

        elif self.rect.x < target.x:
            self.rect.x += 100 * dt
            self.last_key = "d"

            if self.delay == 0:
                if self.image == self.image1:
                    self.image = self.image2
                else:
                    self.image = self.image1

                self.delay = 30

            if self.flip:
                self.image1 = pygame.transform.flip(self.image1, True, False)
                self.image2 = pygame.transform.flip(self.image2, True, False)
                self.flip = False

            self.delay -= 1

        else:
            if self.last_key == "d":
                self.image = pygame.transform.flip(self.image0, True, False)
            else:
                self.image = self.image0
            
        if int(self.rect.bottom) <= 650:
            self.rect.y += 100 * dt

class Bullet(pygame.sprite.Sprite):

    def __init__(self,x,y, dir, shoot):
        super().__init__()

        # Add bullet sprite when drawn 

        self.rect = pygame.rect.Rect(x,y,10,5)
        self.shoot = shoot
        self.dir = dir

    def move(self, dt):
        if self.shoot:
            if self.dir == "a":
                self.rect.x -= 1000 * dt
            elif self.dir == "d":
                self.rect.x += 1000 * dt

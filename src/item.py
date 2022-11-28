import random
from src.setting import load_sprite_sheet
from src.setting import pygame
from src.setting import screen
from src.setting import width, height
from src.game_value import *

class CoinItem(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('coin.png', 1, 7, sizex, sizey, -1)
        self.item_height = [height * ITEM_HEIGHT, height * ITEM_HEIGHT2, height * ITEM_HEIGHT3]
        self.rect.centery = self.item_height[random.randrange(0, 3)]
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]
        self.index = 0
        self.counter = 0

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2
        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter + 1)

        if self.rect.right < 0:
            self.kill()

class ShieldItem(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet('item.png', 2, 1, sizex, sizey, -1)
        self.item_height = [height*0.82, height*0.75, height*0.60]
        self.rect.centery = self.item_height[random.randrange(0, 3)]
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]
        self.index = 0
        self.counter = 0

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2
        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter + 1)
        if self.rect.right < 0:
            self.kill()


class LifeItem(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet("heart_bullet.png", 1, 1, sizex, sizey, -1)
        self.heart_height = [height*0.82, height*0.75, height*0.60]
        self.rect.centery = self.heart_height[random.randrange(3)]
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]
        self.index = 0
        self.counter = 0

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2
        self.image = self.images[0]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter + 1)

        if self.rect.right < 0:
            self.kill()


class SlowItem(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprite_sheet("slow_pic.png", 2, 1, sizex, sizey, -1)
        self.slow_height = [height*0.82, height*0.75, height*0.60]
        self.rect.centery = self.slow_height[random.randrange(3)]
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]
        self.index = 0
        self.counter = 0

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2
        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter + 1)

        if self.rect.right < 0:
            self.kill()

### 미사일을 쉽게 만들기 위한 미사일 클래스 # 11/1 표기 변경
class Obj(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.move = 0
        self.x_move = 0  # self.xmove => self.x_move
        self.y_move = 0  # self.ymove => self.y_move
        self.movement = [0, 0]
        self.rect=None
    
    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
            self.rect = self.img.get_rect
        else :
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()
    
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    
    def show(self):
        screen.blit(self.img, (self.x,self.y))

class Water_item(pygame.sprite.Sprite):
    def __init__(self, speed=4, sizex=-1, sizey=-1, type = -1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images, self.rect = load_sprite_sheet('umbrella_icon.png', 1, 1, sizex, sizey, -1)
        if type == 1:
            self.rect.bottom = random.randrange(int(0.05*height), int(height*0.37))
        elif type == 2:
            self.rect.bottom = random.randrange(int(0.45*height), int(height*0.87))
        else:
            self.rect.bottom = random.randrange(int(0.45*height), int(height*0.87))

        
        self.rect.left = width + self.rect.width
        self.image = self.images[0] #0과 3 사이의 난수를 반환
        self.movement = [-1*speed, 0] #캐릭터에게 speed의 속도로 다가옴
        
    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()

class Dust_item(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1, type = -1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images, self.rect = load_sprite_sheet('dust_item.png', 1, 1, sizex, sizey, -1)
        if type == 1:
            self.rect.bottom = random.randrange(int(0.05*height), int(height*0.37))
        elif type == 2:
            self.rect.bottom = random.randrange(int(0.45*height), int(height*0.87))
        else:
            self.rect.bottom = random.randrange(int(0.45*height), int(height*0.87))

        
        self.rect.left = width + self.rect.width
        self.image = self.images[0] #0과 3 사이의 난수를 반환
        self.movement = [-1*speed, 0] #캐릭터에게 speed의 속도로 다가옴
        
    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()

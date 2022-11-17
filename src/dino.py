import pygame
from pygame import mixer
# from src.setting import check_point_sound
from src.setting import width, height, screen, gravity
from src.setting import load_sprite_sheet
from src.game_value import *

class Dino:
    def __init__(self, sizex=-1, sizey=-1, type = None ,loc=-1):
        self.type = type
        if type == 'ORIGINAL':
            self.images, self.rect = load_sprite_sheet('dino.png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_ducking.png',
                                                         2, 1, 59, sizey, -1)
        elif type == 'RED':
            self.images, self.rect = load_sprite_sheet('red_dino.png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('red_dino_ducking.png',
                                                         2, 1, 59, sizey, -1)
        elif type == 'YELLOW':
            self.images, self.rect = load_sprite_sheet('yellow_dino.png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('yellow_dino_ducking.png',
                                                         2, 1, 59, sizey, -1)
        elif type == 'PURPLE':
            self.images, self.rect = load_sprite_sheet('purple_dino.png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('purple_dino_ducking.png',
                                                         2, 1, 59, sizey, -1)
        elif type == 'TUX':
            self.images, self.rect = load_sprite_sheet('tux_walk.png',
                                                       6, 1, 60, 58, -1)
            self.images1, self.rect1 = load_sprite_sheet('tux_ducking.png',
                                                         2, 1, 60, 58, -1)
        elif type == '2p_original':
            self.images, self.rect = load_sprite_sheet('dino(pvp).png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_ducking(pvp).png',
                                                         2, 1, 59, sizey, -1)
        else:
            self.images, self.rect = load_sprite_sheet('dino.png',
                                                       6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_ducking.png',
                                                         2, 1, 59, sizey, -1)
        if loc == -1:
            self.rect.bottom = int(DEFAULT_HEIGHT * height)
            self.rect.left = width / 15
        elif loc == -2:
            self.rect.bottom = int(DEFAULT_HEIGHT_2P * height)
            self.rect.left = width /15
        else:
            self.rect.bottom = int(DEFAULT_HEIGHT * height)
            self.rect.left = width * (13 / 15)
        self.image = self.images[0]
        self.type = type
        self.index = 0
        self.counter = 0
        self.score = 0
        self.score2 = 0
        self.item_time = 0
        self.is_jumping = False
        self.is_dead = False
        self.is_ducking = False
        self.is_blinking = False
        self.movement = [0, 0]
        self.jump_speed = 11.5
        self.jump_speed_runnung = 10.5
        self.super_jump_speed = self.jump_speed * 1.3
        self.super_jump_speed_running = self.jump_speed_runnung * 1.3
        self.collision_immune = False
        self.is_super = False
        self.stand_width = self.rect.width
        self.duck_width = self.rect1.width
        self.is_battle = False
        self.player1 = False
        if loc == -1:
            self.player1 = True
        elif loc == -2:
            self.is_battle = True
        else:
            self.is_battle = False
        self.life = LIFE

        # 아이템 사용 상태
        self.Superglass = False
        self.Sovel = False
        self.Mask = False

        self.stand_pos_width = self.rect.width
        self.duck_pos_width = self.rect1.width      
        

    def draw(self):
        screen.blit(self.image, self.rect)

    # 충돌판단
    def check_bounds(self):
        if self.is_battle == True and self.player1 == False :
            if self.rect.bottom > int(0.475 * height):
                self.rect.bottom = int(0.475 * height)
                self.is_jumping = False             
        if self.rect.bottom > int(DEFAULT_HEIGHT * height):
            self.rect.bottom = int(DEFAULT_HEIGHT * height)
            self.is_jumping = False 


    def update(self, mode=''):
        if self.is_jumping: 
            self.movement[1] = self.movement[1] + gravity

        if self.Superglass: # 안경쓰고 있을 때
            if self.is_jumping: self.index = 5 # 뛰고있을 때
            # 걸어갈 때
            if self.is_ducking: # 숙이고있으면
                if self.counter % 5 == 0: 
                    if self.index==2: self.index=3
                    elif self.index==3: self.index=2
                    else: self.index=2
            else: # 서있으면
                if self.counter % 5 == 0: 
                    if self.index == 6: self.index=7
                    elif self.index == 7: self.index=6
                    else: self.index = 6

        elif self.Sovel: # 삽들고 있을 때
            if self.is_jumping: self.index = 8 # 뛰고있을 때
            # 걸어갈 때
            if not self.is_ducking: # 서있으면
                if self.counter % 5 == 0:
                    if self.index==9: self.index=10
                    elif self.index==10: self.index=9
                    else: self.index=9
            else: # 숙이고있으면
                if self.counter % 5 == 0:
                    if self.index==4: self.index=5
                    elif self.index==5: self.index=4
                    else: self.index=4

        elif self.Mask: # 마스크 쓰고 있을 때
            if self.is_jumping: self.index = 11 # 뛰고있을 때
            # 걸어갈 때
            if not self.is_ducking: # 서있으면
                if self.counter % 5 == 0:
                    if self.index==12: self.index=13
                    elif self.index==13: self.index=12
                    else: self.index=12
            else: # 숙이고있으면
                if self.counter % 5 == 0:
                    if self.index==6: self.index=7
                    elif self.index==7: self.index=6
                    else: self.index=6

        elif self.is_blinking: # 눈 깜빡이기
            if self.index == 0:
                if self.counter % 400 == 399:
                    self.index = 1
            else:
                if self.counter % 20 == 19:
                    self.index = 1

        else: # 아무것도 안입고 있을 때
            if self.is_jumping: self.index = 0 # 뛰고있을 때
             # 걸어갈 때
            if not self.is_ducking: # 서있으면
                if self.counter % 5 == 0:
                    if self.index==1: self.index=2
                    elif self.index==2: self.index=1
                    else: self.index=1
            else: # 숙이고있으면
                if self.counter % 5 == 0:
                    if self.index==0: self.index=1
                    elif self.index==1: self.index=0
                    else: self.index=0

        if self.is_dead: # 죽었을 경우
            self.index = 4

        if self.collision_immune:
            if self.counter % 10 == 0: self.index = 1

        # 숙이고 있는 모션 구현
        if not self.is_ducking:
            if self.counter % 5 == 0:
                self.image = self.images[self.index]
            self.rect.width = self.stand_pos_width
        else:
            if self.counter % 5 == 0: 
                self.image = self.images1[self.index]
            if self.collision_immune is True:
                if self.counter % 5 == 0:
                    self.image = self.images[5]
            self.rect.width = self.duck_pos_width

        self.rect = self.rect.move(self.movement)
        self.check_bounds()

        if not self.is_dead and self.counter % 7 == 6 and self.is_blinking == False:
            self.score += 1
            self.score2 += 1
            self.item_time += 1
            # if self.score % 100 == 0 and self.score != 0:
            #     if pygame.mixer.get_init() != None:
            #         checkPoint_sound.play()

        self.counter = (self.counter + 1)
        # if self.is_jumping:
        #     self.movement[1] = self.movement[1] + gravity
        # ##
        # if self.is_jumping:
        #     self.index = 0
        # #
        # elif self.is_blinking:
        #     if self.index == 0:
        #         if self.counter % 400 == 399:
        #             # 눈깜빡
        #             self.index = (self.index + 1) % 2
        #     else:  # 눈 깜빡
        #         if self.counter % 20 == 19:
        #             self.index = (self.index + 1) % 2
        # # is ducking이 True면
        # elif self.is_ducking:
        #     if self.counter % 5 == 0:
        #         self.index = (self.index + 1) % 2
        # else:
        #     if self.counter % 5 == 0:
        #         self.index = (self.index + 1) % 2 + 2
        # if self.is_dead:
        #     self.index = 4
        # if self.collision_immune:
        #     if self.counter % 10 == 0:
        #         self.index = 5
        # #
        # if not self.is_ducking:
        #     self.image = self.images[self.index]
        #     self.rect.width = self.stand_width
        # else:
        #     self.image = self.images1[self.index % 2]
        #     if self.collision_immune is True:
        #         if self.counter % 5 == 0:
        #             self.image = self.images[5]
        #     self.rect.width = self.duck_width
        # self.rect = self.rect.move(self.movement)
        # self.check_bounds()

        # if not self.is_dead and self.counter % 7 == 6 and not self.is_blinking:
        #     self.score += 1
        #     # if mode != 'pvp':
        #     #     if self.score % 100 == 0 and self.score != 0:
        #     #         if mixer.get_init() is not None:
        #     #             check_point_sound.play()
        # self.counter = (self.counter + 1)

    def increase_life(self):
        self.life += 1

    def decrease_life(self):
        self.life -= 1

    def is_life_zero(self):
        if self.life == 0:
            return True 
        else:
            False

    def add_score(self, score):
        self.score += score

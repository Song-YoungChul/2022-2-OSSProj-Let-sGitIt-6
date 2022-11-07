from src.dino import *
from src.obstacle import *
from src.item import *
from src.interface import *
import src.game 
from db.db_interface import InterfDB
from time import sleep

db = InterfDB("db/score.db")
clearScore = 100
item_story1 = False
item_story2 = False
item_story3 = False
item_story4 = False
#아이템 체크 횟수
item_cnt=0



def ItemSelectMode():
    global item_story1
    global item_story2
    global item_story3
    global item_story4
    global item_cnt
    ALPHA_MOVE = 20
    width_offset = 0.2
    resized_screen_center = (0, 0)
    global resized_screen
    game_start = False

    # 배경 이미지
    # back_store, back_store_rect = load_image('intro_bg.png', width, height)
    alpha_back, alpha_back_rect = alpha_image('selectitem.png', width + ALPHA_MOVE, height)
    alpha_back_rect.left = -ALPHA_MOVE

    # 버튼 이미지
    sung_btn_image, sung_btn_rect = alpha_image('Superglass.png', 150, 150, -1)
    r_sung_btn_image, r_sung_btn_rect = alpha_image(*resize('Superglass.png', 150, 150, -1))
    shov_btn_image, shov_btn_rect = alpha_image('shovel.png', 150, 150, -1)
    r_shov_btn_image, r_shov_btn_rect = alpha_image(*resize('shovel.png', 150, 150, -1))
    umbr_btn_image, umbr_btn_rect = alpha_image('umbrella.png', 150, 150, -1)
    r_umbr_btn_image, r_umbr_btn_rect = alpha_image(*resize('umbrella.png', 150, 150, -1))
    mask_btn_image, mask_btn_rect = alpha_image('mask.png', 150, 150, -1)
    r_mask_btn_image, r_mask_btn_rect = alpha_image(*resize('mask.png', 150, 150, -1))
    


    item_story1 = False
    item_story2 = False
    item_story3 = False
    item_story4 = False
    item_cnt=0
    
    warning_image, warning_rect = alpha_image('warning_bigger_circle.png', 150, 150, -1)
    lets_btn_image, lets_btn_rect = alpha_image('LetsGo.png', 100, 30, -1)
    r_lets_btn_image, r_lets_btn_rect = alpha_image(*resize('LetsGo.png', 100, 30, -1))
    option_btn_image, option_btn_rect = alpha_image('btn_option.png', 100, 30, -1)
    r_option_btn_image, r_option_btn_rect = alpha_image(*resize('btn_option.png', 100, 30, -1))

    while not game_start:
        for event in pygame.event.get():
            # if event.type == pygame.VIDEORESIZE and not full_screen:
            #     back_store_rect.bottomleft = (width * 0, height)
            if event.type == pygame.VIDEORESIZE:
                check_scr_size(event.w, event.h)
            if event.type == pygame.QUIT:
                game_start = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    x, y = pygame.mouse.get_pos()
                    if r_sung_btn_rect.collidepoint(x, y):
                        if item_story1==False:
                            item_story1=True
                            item_cnt+=1
                        else:
                            item_story1=False
                            item_cnt-=1
                    if r_shov_btn_rect.collidepoint(x, y):
                        if item_story2==False:
                            item_story2=True
                            item_cnt+=1
                        else:
                            item_story2=False
                            item_cnt-=1
                    if r_umbr_btn_rect.collidepoint(x, y):
                        if item_story3==False:
                            item_story3=True
                            item_cnt+=1
                        else:
                            item_story3=False
                            item_cnt-=1
                    if r_mask_btn_rect.collidepoint(x, y):
                        if item_story4==False:
                            item_story4=True
                            item_cnt+=1 
                        else:
                            item_story4=False
                            item_cnt-=1
                    if r_lets_btn_rect.collidepoint(x, y):
                        gameplay_story1()


        if item_story1 == False:
            sung_btn_image, sung_btn_rect = alpha_image('Superglass.png', 150, 150, -1)
            r_sung_btn_image, r_sung_btn_rect = alpha_image(*resize('Superglass.png', 150, 150, -1))
        else:
            sung_btn_image, sung_btn_rect = alpha_image('Superglasson.png', 150, 150, -1)
            r_sung_btn_image, r_sung_btn_rect = alpha_image(*resize('Superglasson.png', 150, 150, -1))
        
        if item_story2 == False:
            shov_btn_image, shov_btn_rect = alpha_image('shovel.png', 150, 150, -1)
            r_shov_btn_image, r_shov_btn_rect = alpha_image(*resize('shovel.png', 150, 150, -1))
        else:
            shov_btn_image, shov_btn_rect = alpha_image('shovelon.png', 150, 150, -1)
            r_shov_btn_image, r_shov_btn_rect = alpha_image(*resize('shovelon.png', 150, 150, -1))
        
        if item_story3 == False:
            umbr_btn_image, umbr_btn_rect = alpha_image('umbrella.png', 150, 150, -1)
            r_umbr_btn_image, r_umbr_btn_rect = alpha_image(*resize('umbrella.png', 150, 150, -1))
        else:
            umbr_btn_image, umbr_btn_rect = alpha_image('umbrellaon.png', 150, 150, -1)
            r_umbr_btn_image, r_umbr_btn_rect = alpha_image(*resize('umbrellaon.png', 150, 150, -1))
        
        if item_story4 == False:
            mask_btn_image, mask_btn_rect = alpha_image('mask.png', 150, 150, -1)
            r_mask_btn_image, r_mask_btn_rect = alpha_image(*resize('mask.png', 150, 150, -1))
        else:
            mask_btn_image, mask_btn_rect = alpha_image('maskon.png', 150, 150, -1)
            r_mask_btn_image, r_mask_btn_rect = alpha_image(*resize('maskon.png', 150, 150, -1))
        

        r_sung_btn_rect.centerx = resized_screen.get_width() * 0.2
        r_sung_btn_rect.centery = resized_screen.get_height() * 0.6
        r_shov_btn_rect.centerx = resized_screen.get_width() * (0.2 + width_offset)
        r_shov_btn_rect.centery = resized_screen.get_height() * 0.6
        r_umbr_btn_rect.centerx = resized_screen.get_width() * (0.2 + 2 * width_offset)
        r_umbr_btn_rect.centery = resized_screen.get_height() * 0.6
        r_mask_btn_rect.centerx = resized_screen.get_width() * (0.2 + 3 * width_offset)
        r_mask_btn_rect.centery = resized_screen.get_height() * 0.6
        r_lets_btn_rect.centerx = resized_screen.get_width() * 0.1
        r_lets_btn_rect.centery = resized_screen.get_height() * 0.1
        # r_start_btn_rect.centerx = resized_screen.get_width() * 0.1
        # r_start_btn_rect.centery = resized_screen.get_height() * 0.1
        # screen.blit(back_store, back_store_rect)
        screen.blit(alpha_back, alpha_back_rect)
        disp_store_buttons(sung_btn_image, shov_btn_image, umbr_btn_image, lets_btn_image, mask_btn_image)
        resized_screen.blit(
            pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
            resized_screen_center)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()



Shovel = False #삽

## 미세먼지 ##
def gameplay_story1():
    global item_story1
    Sunglass = False #선글라스
    global resized_screen
    global high_score
    result = db.query_db("select score from user order by score desc;", one=True)
    if result is not None:
        high_score = result['score']
    #    if bgm_on:
    #       pygame.mixer.music.play(-1) # 배경음악 실행
    game_speed = 4
    startMenu = False
    game_over = False
    gameClear = False
    game_quit = False
    ###
    life = 5
    ###
    paused = False
    if item_story1==True:
        Sunglass_cnt=2
    else:
        Sunglass_cnt=0
    Shovel_time=0
    if item_story2==True:
        Shovel_cnt=2
    else:
        Shovel_cnt=0
    Umbrella_time=0
    if item_story3==True:
        Umbrella_cnt=2
    else:
        Umbrella_cnt=0
    if item_story4==True:
        Maskplus_cnt=2
    else:
        Maskplus_cnt=0

    #배경이미지
    back_image,back_rect = load_image('dust_with_items.png',800,400,-1)
    #먼지이미지
    dust_image,dust_rect = load_image('dust.png',800,400,-1)


    #불투명도
    dustnum=0
    dust_image.set_alpha(dustnum)

    player_dino = Dino(dino_size[0], dino_size[1])

    new_ground = Ground(-1 * game_speed)
    heart = HeartIndicator(life)
    counter = 0

    cacti = pygame.sprite.Group()
    fire_cacti = pygame.sprite.Group()
    pteras = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    # add stones
    stones = pygame.sprite.Group()

    last_obstacle = pygame.sprite.Group()

    Stone.containers = stones

    Cactus.containers = cacti
    fire_Cactus.containers = fire_cacti
    Ptera.containers = pteras
    Cloud.containers = clouds

    # BUTTON IMG LOAD
    # retbutton_image, retbutton_rect = load_image('replay_button.png', 70, 62, -1)
    gameover_image, gameover_rect = load_image('game_over.png', 380, 22, -1)

    #방향키 구현
    global go_right
    global go_left
    global jumpingx2
    go_left=False
    go_right=False
    #2단 점프
    jumpingx2=False

    while not game_quit:
        while startMenu:
            pass
        while not game_over and not gameClear:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                game_over = True


            else:
                screen.fill(background_col)
                screen.blit(back_image,back_rect)
                

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:  # 스페이스 누르는 시점에 공룡이 땅에 닿아있으면 점프한다.
                            if player_dino.rect.bottom == int(0.98 * height):
                                player_dino.is_jumping = True
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()
                                player_dino.movement[1] = -1 * player_dino.jump_speed

                        if event.key == pygame.K_DOWN:  # 아래방향키를 누르는 시점에 공룡이 점프중이지 않으면 숙인다.
                            if not (player_dino.is_jumping and player_dino.is_dead):
                                player_dino.is_ducking = True

                        if event.key == pygame.K_LEFT:
                            # print("left")
                            go_left=True

                        if event.key == pygame.K_RIGHT:
                            # print("right")
                            go_right=True

                        if event.key == pygame.K_ESCAPE:
                            paused = not paused
                            paused = src.game.pausing()


                        # jumping x2 ( press key s)
                        if event.key == pygame.K_s:
                            jumpingx2=True

                        # 2. a키를 누르면, 미사일이 나갑니다.
                        if event.key == pygame.K_a:
                            space_go=True
                            bk=0
                        #

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            player_dino.is_ducking = False

                        # 3.a키에서 손을 떼면, 미사일이 발사 되지 않습니다.
                        if event.key == pygame.K_a:
                            space_go = False
                        
                        # 방향키 추가
                        if event.key == pygame.K_LEFT:
                            go_left=False

                        if event.key == pygame.K_RIGHT:
                            go_right=False
                        #

                        ## jumgpingx2
                        if event.key == pygame.K_s:
                            jumpingx2 = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed() == (1, 0, 0) and player_dino.rect.bottom == int(0.98 * height):
                            # (mouse left button, wheel button, mouse right button)
                            player_dino.is_jumping = True
                            if pygame.mixer.get_init() != None:
                                jump_sound.play()
                            player_dino.movement[1] = -1 * player_dino.jump_speed

                        if pygame.mouse.get_pressed() == (0, 0, 1):
                            # (mouse left button, wheel button, mouse right button)
                            if not (player_dino.is_jumping and player_dino.is_dead):
                                player_dino.is_ducking = True

                    if event.type == pygame.MOUSEBUTTONUP:
                        player_dino.is_ducking = False

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)
                #미세먼지 등장

                if 0<=player_dino.score%100<50:
                    dustnum=0
                    dust_image.set_alpha(dustnum)
                elif 50<=player_dino.score%100<100:
                    dustnum=255
                    dust_image.set_alpha(dustnum)

            if not paused:
                if go_left:
                    if player_dino.rect.left < 0:
                        player_dino.rect.left = 0
                    else:
                        player_dino.rect.left = player_dino.rect.left - game_speed
                if go_right:
                    if player_dino.rect.right > width:
                        player_dino.rect.right = width
                    else:
                        player_dino.rect.left = player_dino.rect.left + game_speed

                if jumpingx2 :
                    if  player_dino.rect.bottom == int(height * 0.98):
                        player_dino.is_jumping = True
                        player_dino.movement[1] = -1 * player_dino.super_jump_speed


                if item_story1==True:
                    if Sunglass == True:
                        player_dino.Superglass = True
                        if player_dino.score % 50 ==0:
                            Sunglass=False
                            Sunglass_cnt-=1
                            player_dino.Superglass = False
                        for s in stones:
                            s.movement[0] = -1 * game_speed
                            if not player_dino.collision_immune:
                                if pygame.sprite.collide_mask(player_dino, s):
                                    player_dino.collision_immune = True
                                    life -= 1
                                    collision_time = pygame.time.get_ticks()
                                    if life == 0:
                                        player_dino.is_dead = True
                                    if pygame.mixer.get_init() is not None:
                                        die_sound.play()
                        for c in cacti:
                            c.movement[0] = -1 * game_speed
                            if not player_dino.collision_immune:
                                if pygame.sprite.collide_mask(player_dino, c):
                                    player_dino.collision_immune = True
                                    life -= 1
                                    collision_time = pygame.time.get_ticks()
                                    if life == 0:
                                        player_dino.is_dead = True
                                    if pygame.mixer.get_init() is not None:
                                        die_sound.play()

                            elif not player_dino.is_super:
                                immune_time = pygame.time.get_ticks()
                                if immune_time - collision_time > collision_immune_time:
                                    player_dino.collision_immune = False
                        
                        for f in fire_cacti:
                            f.movement[0] = -1 * game_speed
                            if not player_dino.collision_immune:
                                if pygame.sprite.collide_mask(player_dino, f):
                                    player_dino.collision_immune = True
                                    life -= 1
                                    collision_time = pygame.time.get_ticks()
                                    if life == 0:
                                        player_dino.is_dead = True
                                    if pygame.mixer.get_init() is not None:
                                        die_sound.play()

                            elif not player_dino.is_super:
                                immune_time = pygame.time.get_ticks()
                                if immune_time - collision_time > collision_immune_time:
                                    player_dino.collision_immune = False
                        
                        for p in pteras:
                            p.movement[0] = -1 * game_speed
                            if not player_dino.collision_immune:
                                if pygame.sprite.collide_mask(player_dino, p):
                                    player_dino.collision_immune = True
                                    life -= 1
                                    collision_time = pygame.time.get_ticks()
                                    if life == 0:
                                        player_dino.is_dead = True
                                    if pygame.mixer.get_init() is not None:
                                        die_sound.play()

                            elif not player_dino.is_super:
                                immune_time = pygame.time.get_ticks()
                                if immune_time - collision_time > collision_immune_time:
                                    player_dino.collision_immune = False


                            elif not player_dino.is_super:
                                immune_time = pygame.time.get_ticks()
                                if immune_time - collision_time > collision_immune_time:
                                    player_dino.collision_immune = False
                    else:
                        for s in stones:
                            if 0<=player_dino.score%100<50:
                                s.image.set_alpha(255)
                            elif 50<=player_dino.score%100<100:
                                s.image.set_alpha(70)
                            
                            s.movement[0] = -1 * game_speed
                            if not player_dino.collision_immune:
                                if pygame.sprite.collide_mask(player_dino, s):
                                    player_dino.collision_immune = True
                                    life -= 1
                                    collision_time = pygame.time.get_ticks()
                                    if life == 0:
                                        player_dino.is_dead = True
                                    if pygame.mixer.get_init() is not None:
                                        die_sound.play()

                        for c in cacti:
                            if 0<=player_dino.score%100<50:
                                c.image.set_alpha(255)
                            elif 50<=player_dino.score%100<100:
                                c.image.set_alpha(70)
                            c.movement[0] = -1 * game_speed
                            if not player_dino.collision_immune:
                                if pygame.sprite.collide_mask(player_dino, c):
                                    player_dino.collision_immune = True
                                    life -= 1
                                    collision_time = pygame.time.get_ticks()
                                    if life == 0:
                                        player_dino.is_dead = True
                                    if pygame.mixer.get_init() is not None:
                                        die_sound.play()

                            elif not player_dino.is_super:
                                immune_time = pygame.time.get_ticks()
                                if immune_time - collision_time > collision_immune_time:
                                    player_dino.collision_immune = False

                        for f in fire_cacti:
                            if 0<=player_dino.score%100<50:
                                f.image.set_alpha(255)
                            elif 50<=player_dino.score%100<100:
                                f.image.set_alpha(70)
                            f.movement[0] = -1 * game_speed
                            if not player_dino.collision_immune:
                                if pygame.sprite.collide_mask(player_dino, f):
                                    player_dino.collision_immune = True
                                    life -= 1
                                    collision_time = pygame.time.get_ticks()
                                    if life == 0:
                                        player_dino.is_dead = True
                                    if pygame.mixer.get_init() is not None:
                                        die_sound.play()

                            elif not player_dino.is_super:
                                immune_time = pygame.time.get_ticks()
                                if immune_time - collision_time > collision_immune_time:
                                    player_dino.collision_immune = False

                        for p in pteras:
                            if 0<=player_dino.score%100<50:
                                p.image.set_alpha(255)
                            elif 50<=player_dino.score%100<100:
                                p.image.set_alpha(70)
                            p.movement[0] = -1 * game_speed
                            if not player_dino.collision_immune:
                                if pygame.sprite.collide_mask(player_dino, p):
                                    player_dino.collision_immune = True
                                    life -= 1
                                    collision_time = pygame.time.get_ticks()
                                    if life == 0:
                                        player_dino.is_dead = True
                                    if pygame.mixer.get_init() is not None:
                                        die_sound.play()

                            elif not player_dino.is_super:
                                immune_time = pygame.time.get_ticks()
                                if immune_time - collision_time > collision_immune_time:
                                    player_dino.collision_immune = False


                            elif not player_dino.is_super:
                                immune_time = pygame.time.get_ticks()
                                if immune_time - collision_time > collision_immune_time:
                                    player_dino.collision_immune = False

                        
                else:
                    for s in stones:
                        if 0<=player_dino.score%100<50:
                            s.image.set_alpha(255)
                        elif 50<=player_dino.score%100<100:
                            s.image.set_alpha(70)
                        
                        s.movement[0] = -1 * game_speed
                        if not player_dino.collision_immune:
                            if pygame.sprite.collide_mask(player_dino, s):
                                player_dino.collision_immune = True
                                life -= 1
                                collision_time = pygame.time.get_ticks()
                                if life == 0:
                                    player_dino.is_dead = True
                                if pygame.mixer.get_init() is not None:
                                    die_sound.play()

                    for c in cacti:
                        if 0<=player_dino.score%100<50:
                            c.image.set_alpha(255)
                        elif 50<=player_dino.score%100<100:
                            c.image.set_alpha(70)
                        c.movement[0] = -1 * game_speed
                        if not player_dino.collision_immune:
                            if pygame.sprite.collide_mask(player_dino, c):
                                player_dino.collision_immune = True
                                life -= 1
                                collision_time = pygame.time.get_ticks()
                                if life == 0:
                                    player_dino.is_dead = True
                                if pygame.mixer.get_init() is not None:
                                    die_sound.play()

                        elif not player_dino.is_super:
                            immune_time = pygame.time.get_ticks()
                            if immune_time - collision_time > collision_immune_time:
                                player_dino.collision_immune = False

                    for f in fire_cacti:
                        if 0<=player_dino.score%100<50:
                            f.image.set_alpha(255)
                        elif 50<=player_dino.score%100<100:
                            f.image.set_alpha(70)
                        f.movement[0] = -1 * game_speed
                        if not player_dino.collision_immune:
                            if pygame.sprite.collide_mask(player_dino, f):
                                player_dino.collision_immune = True
                                life -= 1
                                collision_time = pygame.time.get_ticks()
                                if life == 0:
                                    player_dino.is_dead = True
                                if pygame.mixer.get_init() is not None:
                                    die_sound.play()

                        elif not player_dino.is_super:
                            immune_time = pygame.time.get_ticks()
                            if immune_time - collision_time > collision_immune_time:
                                player_dino.collision_immune = False

                    for p in pteras:
                        if 0<=player_dino.score%100<50:
                            p.image.set_alpha(255)
                        elif 50<=player_dino.score%100<100:
                            p.image.set_alpha(70)
                        p.movement[0] = -1 * game_speed
                        if not player_dino.collision_immune:
                            if pygame.sprite.collide_mask(player_dino, p):
                                player_dino.collision_immune = True
                                life -= 1
                                collision_time = pygame.time.get_ticks()
                                if life == 0:
                                    player_dino.is_dead = True
                                if pygame.mixer.get_init() is not None:
                                    die_sound.play()

                        elif not player_dino.is_super:
                            immune_time = pygame.time.get_ticks()
                            if immune_time - collision_time > collision_immune_time:
                                player_dino.collision_immune = False


                        elif not player_dino.is_super:
                            immune_time = pygame.time.get_ticks()
                            if immune_time - collision_time > collision_immune_time:
                                player_dino.collision_immune = False

                        
                STONE_INTERVAL = 50
                CACTUS_INTERVAL = 50
                PTERA_INTERVAL = 300
                CLOUD_INTERVAL = 300
                OBJECT_REFRESH_LINE = width * 0.8
                MAGIC_NUM = 10

                if len(cacti) < 2:
                    if len(cacti) == 0:
                        last_obstacle.empty()
                        last_obstacle.add(Cactus(game_speed, object_size[0], object_size[1]))
                    else:
                        for l in last_obstacle:
                            if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL) == MAGIC_NUM:
                                last_obstacle.empty()
                                last_obstacle.add(Cactus(game_speed, object_size[0], object_size[1]))

                if len(fire_cacti) < 2:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL * 5) == MAGIC_NUM:
                            last_obstacle.empty()
                            last_obstacle.add(fire_Cactus(game_speed, object_size[0], object_size[1]))

                if len(stones) < 2:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(STONE_INTERVAL * 3) == MAGIC_NUM:
                            last_obstacle.empty()
                            last_obstacle.add(Stone(game_speed, object_size[0], object_size[1]))

                if len(pteras) == 0 and random.randrange(PTERA_INTERVAL) == MAGIC_NUM and counter > PTERA_INTERVAL:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE:
                            last_obstacle.empty()
                            last_obstacle.add(Ptera(game_speed, ptera_size[0], ptera_size[1]))

                if len(clouds) < 5 and random.randrange(CLOUD_INTERVAL) == MAGIC_NUM:
                    Cloud(width, random.randrange(height / 5, height / 2))



                player_dino.update()
                cacti.update()
                fire_cacti.update()
                pteras.update()
                clouds.update()
                new_ground.update()
                heart.update(life)
                stones.update()
                
                if pygame.display.get_surface() != None:
                    screen.blit(dust_image,dust_rect)
                    new_ground.draw()
                    clouds.draw(screen)

                    heart.draw()

                    cacti.draw(screen)
                    stones.draw(screen)
                    fire_cacti.draw(screen)
                    pteras.draw(screen)
                    player_dino.draw()
                    resized_screen.blit(
                        pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                        resized_screen_center)
                    pygame.display.update()

                    


                clock.tick(FPS)

                if player_dino.is_dead:
                    game_over = True
                    # ingame_m.stop() # 죽으면 배경음악 멈춤
                    # pygame.mixer.music.stop()  # 죽으면 배경음악 멈춤
                    if player_dino.score > high_score:
                        high_score = player_dino.score

                if counter % speed_up_limit == speed_up_limit - 1:
                    new_ground.speed -= 1
                    game_speed += 1

                counter = (counter + 1)

                if player_dino.score >= clearScore:
                    gameClear = True
                    break
                

        if game_quit:
            break

        while gameClear:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_n:
                            gameplay_story1()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        gameplay_story1()
            if pygame.display.get_surface() != None:
                # screen.blit(clearImage, clearImage_rect)
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            break


        while game_over:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                # game_over = False

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            game_over = False
                            game_quit = True
                            src.game.intro_screen()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_over = False
                        game_quit = True
                        src.game.intro_screen()

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)


            if pygame.display.get_surface() != None:
                disp_gameover_msg(gameover_image)
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            clock.tick(FPS)

    pygame.quit()
    quit()

def gameplay_story2(): # 지진모드
    global item_story2
    #아이템 관련 변수 설정
    Shovel = False #삽
    Shovel_time=0
    global resized_screen
    global high_score
    result = db.query_db("select score from user order by score desc;", one=True)
    if result is not None:
        high_score = result['score']
    #    if bgm_on:
    #       pygame.mixer.music.play(-1) # 배경음악 실행
    game_speed = 4
    startMenu = False
    game_over = False
    gameClear = False
    game_quit = False
    life = 5

    paused = False

    if item_story1==True:
        Sunglass_cnt=2
    else:
        Sunglass_cnt=0
    Shovel_time=0
    if item_story2==True:
        Shovel_cnt=2
    else:
        Shovel_cnt=0
    Umbrella_time=0
    if item_story3==True:
        Umbrella_cnt=2
    else:
        Umbrella_cnt=0
    if item_story4==True:
        Maskplus_cnt=2
    else:
        Maskplus_cnt=0

    player_dino = Dino(dino_size[0], dino_size[1], type=dino_type[type_idx])
    Background, Background_rect = alpha_image('rocks_with_items.png', 800, 400, -1)
    
    new_ground = Ground(-1 * game_speed)
    heart = HeartIndicator(life)
    counter = 0

    cacti = pygame.sprite.Group()
    fire_cacti = pygame.sprite.Group()
    pteras = pygame.sprite.Group()
    clouds = pygame.sprite.Group()

    stones = pygame.sprite.Group()
    holes = pygame.sprite.Group()

    last_obstacle = pygame.sprite.Group()

    Stone.containers = stones
    Hole.containers = holes

    Cactus.containers = cacti
    fire_Cactus.containers = fire_cacti
    Ptera.containers = pteras
    Cloud.containers = clouds

    # BUTTON IMG LOAD
    # retbutton_image, retbutton_rect = load_image('replay_button.png', 70, 62, -1)
    
    gameover_image, gameover_rect = load_image('game_over.png', 380, 22, -1)
    clear_image, clear_rect = load_image('intro_bg.png', width, height, -1)

    # 방향키 구현
    go_left=False
    go_right=False
    jumpingx2=False

    while not game_quit:
        while startMenu:
            pass
        while not game_over and not gameClear:
            
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                game_over = True


            else:
                screen.fill(background_col)
                screen.blit(Background, Background_rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # 종료
                        game_quit = True
                        game_over = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:  # 스페이스 누르는 시점에 공룡이 땅에 닿아있으면 점프한다.
                            if player_dino.rect.bottom == int(0.9 * height):
                                player_dino.is_jumping = True
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()
                                player_dino.movement[1] = -1 * player_dino.jump_speed

                        if event.key == pygame.K_DOWN:  # 아래방향키를 누르는 시점에 공룡이 점프중이지 않으면 숙인다.
                            if not (player_dino.is_jumping and player_dino.is_dead):
                                player_dino.is_du = True

                        if event.key == pygame.K_LEFT:
                            # print("left")
                            go_left=True

                        if event.key == pygame.K_RIGHT:
                            # print("right")
                            go_right=True

                        # jumping x2 ( press key s)
                        if event.key == pygame.K_s:
                            jumpingx2=True

                        if event.key == pygame.K_d:
                            if (item_story2 == True) and (Shovel_cnt!=0):
                                Shovel = True
                        
                        if event.key == pygame.K_ESCAPE:
                            paused = not paused

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            player_dino.is_du = False

                        # 방향키 추가
                        if event.key == pygame.K_LEFT:
                            go_left=False

                        if event.key == pygame.K_RIGHT:
                            go_right=False
                        #

                        ## jumgpingx2
                        if event.key == pygame.K_s:
                            jumpingx2 = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed() == (1, 0, 0) and player_dino.rect.bottom == int(0.9 * height):
                            # (mouse left button, wheel button, mouse right button)
                            player_dino.is_jumping = True
                            if pygame.mixer.get_init() != None:
                                jump_sound.play()
                            player_dino.movement[1] = -1 * player_dino.jump_speed

                        if pygame.mouse.get_pressed() == (0, 0, 1):
                            # (mouse left button, wheel button, mouse right button)
                            if not (player_dino.is_jumping and player_dino.is_dead):
                                player_dino.is_du = True

                    if event.type == pygame.MOUSEBUTTONUP:
                        player_dino.is_du = False

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)

            if not paused:
                if Shovel==True:
                    player_dino.Sovel=True
                else:
                    player_dino.Sovel=False
                if go_left:
                    if player_dino.rect.left < 0:
                        player_dino.rect.left = 0
                    else:
                        player_dino.rect.left = player_dino.rect.left - game_speed

                if go_right:
                    if player_dino.rect.right > width:
                        player_dino.rect.right = width
                    else:
                        player_dino.rect.left = player_dino.rect.left + game_speed

                if jumpingx2 :
                    if  player_dino.rect.bottom == int(height * 0.9):
                        player_dino.is_jumping = True
                        player_dino.movement[1] = -1 * player_dino.super_jump_speed


                for h in holes:
                    h.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, h):
                            if Shovel==True:
                                h.image.set_alpha(0)                      
                            else:
                                player_dino.collision_immune = True
                                life -= 5
                                collision_time = pygame.time.get_ticks()
                                if life <= 0:
                                    player_dino.is_dead = True
                                if pygame.mixer.get_init() is not None:
                                    die_sound.play()
                
                for s in stones:
                    s.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, s):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                for c in cacti:
                    c.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, c):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False

                for f in fire_cacti:
                    f.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, f):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False

                for p in pteras:
                    p.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, p):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False


                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False

                HOLE_INTERVAL = 50
                STONE_INTERVAL = 50
                CACTUS_INTERVAL = 50
                PTERA_INTERVAL = 340
                CLOUD_INTERVAL = 300
                OBJECT_REFRESH_LINE = width *0.95 
                MAGIC_NUM = 10

                if len(cacti) < 2:
                    if len(cacti) == 0 and player_dino.score <= 1:
                        last_obstacle.empty()
                        last_obstacle.add(Cactus(game_speed, object_size[0], object_size[1]))
                    else:
                        for l in last_obstacle:
                            if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL) == MAGIC_NUM:
                                last_obstacle.empty()
                                last_obstacle.add(Cactus(game_speed, object_size[0], object_size[1]))

                if len(fire_cacti) < 2:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL * 5) == MAGIC_NUM:
                            last_obstacle.empty()
                            last_obstacle.add(fire_Cactus(game_speed, object_size[0], object_size[1]))

                if len(stones) < 2:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(STONE_INTERVAL) == MAGIC_NUM:
                            last_obstacle.empty()
                            last_obstacle.add(Stone(game_speed, object_size[0], object_size[1]))
                if Shovel ==True:
                    pass
                else:
                    if len(holes) < 2:
                        for l in last_obstacle:
                            if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(HOLE_INTERVAL) == MAGIC_NUM:
                                last_obstacle.empty()
                                last_obstacle.add(Hole(game_speed, object_size[0], object_size[1]))

                if len(pteras) == 0 and random.randrange(PTERA_INTERVAL) == MAGIC_NUM and counter > PTERA_INTERVAL:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE:
                            last_obstacle.empty()
                            last_obstacle.add(Ptera(game_speed, ptera_size[0], ptera_size[1]))


                if len(clouds) < 5 and random.randrange(CLOUD_INTERVAL) == MAGIC_NUM:
                    Cloud(width, random.randrange(height / 5, height / 2))

                player_dino.update()
                cacti.update()
                fire_cacti.update()
                pteras.update()
                clouds.update()
                new_ground.update()
                # s_scb.update(player_dino.score)
                heart.update(life)
                # item_s.update(Sunglass_cnt,Shovel_cnt,Umbrella_cnt,Maskplus_cnt)

                stones.update()
                holes.update()

                if (Shovel==True):
                    Shovel_time+=1

                if (Shovel_time!=1) and (Shovel_time % 300 == 1):
                    Shovel_time=0
                    Shovel=False
                    Shovel_cnt-=1

                if pygame.display.get_surface() != None:
                    new_ground.draw()
                    clouds.draw(screen)
                    # s_scb.draw()
                    heart.draw()
                    # item_s.draw()
                    cacti.draw(screen)
                    stones.draw(screen)
                    holes.draw(screen)
                    fire_cacti.draw(screen)
                    pteras.draw(screen)
                    player_dino.draw()
                    resized_screen.blit(
                        pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                        resized_screen_center)
                    pygame.display.update()
                clock.tick(FPS)

                if player_dino.is_dead:
                    game_over = True
                    # ingame_m.stop() 
                    # pygame.mixer.music.stop()  # 죽으면 배경음악 멈춤
                    if player_dino.score > high_score:
                        high_score = player_dino.score

                if counter % speed_up_limit == speed_up_limit - 1:
                    new_ground.speed -= 1
                    game_speed += 1

                counter = (counter + 1)

                if player_dino.score >= clearScore:
                    gameClear = True
                    break

        if game_quit:
            break

        

        while gameClear:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_n:
                            gameplay_story3()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        gameplay_story3()
            if pygame.display.get_surface() != None:
                # screen.blit(clearImage, clearImage_rect)
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            break

        while game_over:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                # game_over = False

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            game_over = False
                            game_quit = True
                            src.game.intro_screen()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_over = False
                        game_quit = True
                        src.game.intro_screen()

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)


            if pygame.display.get_surface() != None:
                disp_gameover_msg(gameover_image)
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            clock.tick(FPS)


    pygame.quit()
    quit()

def gameplay_story3():
    global resized_screen
    global high_score
    global item_story3
    result = db.query_db("select score from user order by score desc;", one=True)
    if result is not None:
        high_score = result['score']
    #    if bgm_on:
    #       pygame.mixer.music.play(-1) # 배경음악 실행
    game_speed = 4
    startMenu = False
    game_over = False
    gameClear = False
    game_quit = False
    Umbrella = False
    Umbrella_time=0
    ###
    life = 5
    ###
    paused = False

    if item_story1==True:
        Sunglass_cnt=2
    else:
        Sunglass_cnt=0
    Shovel_time=0
    if item_story2==True:
        Shovel_cnt=2
    else:
        Shovel_cnt=0
    Umbrella_time=0
    if item_story3==True:
        Umbrella_cnt=2
    else:
        Umbrella_cnt=0
    if item_story4==True:
        Maskplus_cnt=2
    else:
        Maskplus_cnt=0

    player_dino = Dino(dino_size[0], dino_size[1], type=dino_type[type_idx])

    new_ground = Ground(-1 * game_speed)
    # s_scb = Story_Scoreboard()
    heart = HeartIndicator(life)
    # item_s = Item_status()
    counter = 0

    cacti = pygame.sprite.Group()
    fire_cacti = pygame.sprite.Group()
    pteras = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    # add stones
    stones = pygame.sprite.Group()

    last_obstacle = pygame.sprite.Group()

    Stone.containers = stones

    Cactus.containers = cacti
    fire_Cactus.containers = fire_cacti
    Ptera.containers = pteras
    Cloud.containers = clouds

    # BUTTON IMG LOAD
    # retbutton_image, retbutton_rect = load_image('replay_button.png', 70, 62, -1)
    gameover_image, gameover_rect = load_image('game_over.png', 380, 22, -1)

    #1. 미사일 발사.
    space_go=False
    m_list=[]
    a_list=[]
    bk=0

    #익룡이 격추되었을때
    isDown=False
    boomCount=0

    #방향키 구현
    go_left=False
    go_right=False

    pm_list = []
    pm_pattern1_count=0
    #2단 점프
    jumpingx2=False

    back_image, back_rect = alpha_image("rain_with_items.png", 800, 400, -1)
    


    while not game_quit:
        while startMenu:
            pass
        while not game_over and not gameClear:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                game_over = True


            else:
                screen.fill(background_col)
                screen.blit(back_image, back_rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # 종료
                        game_quit = True
                        game_over = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:  # 스페이스 누르는 시점에 공룡이 땅에 닿아있으면 점프한다.
                            if player_dino.rect.bottom == int(0.9 * height):
                                player_dino.is_jumping = True
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()
                                player_dino.movement[1] = -1 * player_dino.jump_speed

                        if event.key == pygame.K_DOWN:  # 아래방향키를 누르는 시점에 공룡이 점프중이지 않으면 숙인다.
                            if not (player_dino.is_jumping and player_dino.is_dead):
                                player_dino.is_du = True
                        
                        if event.key == pygame.K_LEFT:
                            go_left=True
                        
                        if event.key == pygame.K_RIGHT:
                            go_right=True

                        if event.key == pygame.K_ESCAPE:
                            paused = not paused
                            paused = src.game.pausing()


                        if event.key == pygame.K_s:
                            jumpingx2=True
                        
                        if event.key == pygame.K_a:
                            space_go=True
                            bk=0

                        if event.key == pygame.K_d:
                            if (item_story3 == True) and (Umbrella_cnt!=0):
                                Umbrella = True
                           

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            player_dino.is_du = False

                        if event.key == pygame.K_a:
                            space_go=False

                        if event.key == pygame.K_LEFT:
                            go_left=False
                        
                        if event.key == pygame.K_RIGHT:
                            go_right=False

                        if event.key == pygame.K_s:
                            jumpingx2=False
                        

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed() == (1, 0, 0) and player_dino.rect.bottom == int(0.9 * height):
                            # (mouse left button, wheel button, mouse right button)
                            player_dino.is_jumping = True
                            if pygame.mixer.get_init() != None:
                                jump_sound.play()
                            player_dino.movement[1] = -1 * player_dino.jump_speed

                        if pygame.mouse.get_pressed() == (0, 0, 1):
                            # (mouse left button, wheel button, mouse right button)
                            if not (player_dino.is_jumping and player_dino.is_dead):
                                player_dino.is_du = True

                    if event.type == pygame.MOUSEBUTTONUP:
                        player_dino.is_du = False

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)

            if not paused:
                if go_left:
                    if player_dino.rect.left < 0:
                        player_dino.rect.left = 0
                    else:
                        player_dino.rect.left = player_dino.rect.left - game_speed

                if go_right:
                    if player_dino.rect.right > width:
                        player_dino.rect.right = width
                    else:
                        player_dino.rect.left = player_dino.rect.left + game_speed

                if (space_go==True) and (int(bk%100)==0):
                    # print(bk)
                    mm=Obj()

                    mm.put_img("./sprites/fire_bullet.png")
                    mm.change_size(15,15)
                    # 
                    
                    if player_dino.is_du ==False:
                        mm.x = round(player_dino.rect.centerx)
                        mm.y = round(player_dino.rect.top*1.035)
                    if player_dino.is_du ==True:
                        mm.x = round(player_dino.rect.centerx)
                        mm.y = round(player_dino.rect.centery*1.01)
                    mm.move = 15
                    m_list.append(mm)
                bk=bk+1
                d_list=[]

                #미사일 하나씩 꺼내옴
                for i in range(len(m_list)):
                    m=m_list[i]
                    m.x +=m.move
                    if m.x>width:
                        d_list.append(i)

                d_list.reverse()
                for d in d_list:
                    del m_list[d]
                #

                if jumpingx2 :
                    if  player_dino.rect.bottom == int(height * 0.9):
                        player_dino.is_jumping = True
                        player_dino.movement[1] = -1 * player_dino.super_jump_speed

                if go_left:
                    if player_dino.rect.left < 0:
                        player_dino.rect.left = 0
                    else:
                        player_dino.rect.left = player_dino.rect.left - game_speed

                if go_right:
                    if player_dino.rect.right > width:
                        player_dino.rect.right = width
                    else:
                        player_dino.rect.left = player_dino.rect.left + game_speed
               
                if  (int(pm_pattern1_count % 20) == 0):
                    pm=Obj()
                    pm.put_img("./sprites/water_drop.png")
                    pm.change_size(40,40)
                    pm.x = random.randrange(40, 800-40)
                    pm.y = 10
                    pm.move = 3
                    pm_list.append(pm)
                pm_pattern1_count += 1
                pd_list = []

                for i in range(len(pm_list)):
                    pm=pm_list[i]
                    pm.y +=pm.move
                    if pm.y>height or pm.x < 0:
                        pd_list.append(i)

                pd_list.reverse()
                for d in pd_list:
                    del pm_list[d]
                #


                for s in stones:
                    s.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, s):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                for c in cacti:
                    c.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, c):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False

                for f in fire_cacti:
                    f.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, f):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False
                
                for p in pteras:
                    p.movement[0] = -1 * game_speed

                    # 7. 익룡이 미사일에 맞으면 익룡과 미사일 모두 사라집니다.

                    if (len(m_list)==0):
                        pass
                    else:
                        if (m.x>=p.rect.left)and(m.x<=p.rect.right)and(m.y>p.rect.top)and(m.y<p.rect.bottom):
                            print("격추 성공")
                            isDown=True
                            boom=Obj()
                            boom.put_img("./sprites/boom.png")
                            boom.change_size(200,100)
                            boom.x=p.rect.centerx-round(p.rect.width)*2.5
                            boom.y=p.rect.centery-round(p.rect.height)*1.5
                            player_dino.score+=30
                            p.kill()
                            # 여기만 바꿈
                            m_list.remove(m)
                            #
                    #

                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, p):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False



                STONE_INTERVAL = 50

                CACTUS_INTERVAL = 50
                PTERA_INTERVAL = 300
                CLOUD_INTERVAL = 300
                OBJECT_REFRESH_LINE = width * 0.8
                MAGIC_NUM = 10

                if (Umbrella_time!=1) and (Umbrella_time % 300 == 1):
                    Umbrella_time=0
                    Umbrella=False
                    Umbrella_cnt-=1

                if Umbrella == True:
                    Umbrella_time+=1
                    um=Obj()
                    um.put_img("./sprites/umbrella_item.png")
                    um.change_size(70,70)
                    um.x = (player_dino.rect.left+player_dino.rect.right)/2-40
                    um.y = player_dino.rect.bottom - 70
                    um.move = 5

                    if (len(pm_list)==0):
                        pass
                    else:
                        # print("x: ",pm.x,"y: ",pm.y)
                        for pm in pm_list:
                            if (pm.y>=um.y)and(pm.x<=um.x+35)and(pm.x>=um.x-35):
                                pm.img.set_alpha(0)


                else:
                    if (len(pm_list)==0):
                        pass
                    else:
                        # print("x: ",pm.x,"y: ",pm.y)
                        for pm in pm_list:
                            if (pm.x>=player_dino.rect.left)and(pm.x<=player_dino.rect.right)and(pm.y>player_dino.rect.top)and(pm.y<player_dino.rect.bottom):
                                print("공격에 맞음.")
                                # if pygame.sprite.collide_mask(player_dino, pm):
                                player_dino.collision_immune = True
                                life -= 1
                                collision_time = pygame.time.get_ticks()
                                if life == 0:
                                    player_dino.is_dead = True
                                pm_list.remove(pm)

                if len(cacti) < 2:
                    if len(cacti) == 0 and player_dino.score <= 1:
                        last_obstacle.empty()
                        last_obstacle.add(Cactus(game_speed, object_size[0], object_size[1]))
                    else:
                        for l in last_obstacle:
                            if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL) == MAGIC_NUM:
                                last_obstacle.empty()
                                last_obstacle.add(Cactus(game_speed, object_size[0], object_size[1]))

                if len(fire_cacti) < 2:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL * 5) == MAGIC_NUM:
                            last_obstacle.empty()
                            last_obstacle.add(fire_Cactus(game_speed, object_size[0], object_size[1]))

                if len(stones) < 2:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(STONE_INTERVAL * 3) == MAGIC_NUM:
                            last_obstacle.empty()
                            last_obstacle.add(Stone(game_speed, object_size[0], object_size[1]))

                

                if len(pteras) == 0 and random.randrange(PTERA_INTERVAL) == MAGIC_NUM and counter > PTERA_INTERVAL:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE:
                            last_obstacle.empty()
                            last_obstacle.add(Ptera(game_speed, ptera_size[0], ptera_size[1]))

                if len(clouds) < 5 and random.randrange(CLOUD_INTERVAL) == MAGIC_NUM:
                    Cloud(width, random.randrange(height / 5, height / 2))

                player_dino.update()
                cacti.update()
                fire_cacti.update()
                pteras.update()
                clouds.update()
                new_ground.update()

                heart.update(life)


                stones.update()
                for a in a_list:
                    a.show()



                if pygame.display.get_surface() != None:
                    new_ground.draw()
                    clouds.draw(screen)

                    heart.draw()

                    cacti.draw(screen)
                    stones.draw(screen)
                    fire_cacti.draw(screen)
                    pteras.draw(screen)

                    for pm in pm_list:
                        pm.show()

                    if Umbrella == True:
                        um.show()

                    player_dino.draw()
                    resized_screen.blit(
                        pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                        resized_screen_center)
                    pygame.display.update()
                clock.tick(FPS)


                if player_dino.is_dead:
                    game_over = True

                    # pygame.mixer.music.stop()  # 죽으면 배경음악 멈춤
                    if player_dino.score > high_score:
                        high_score = player_dino.score

                if counter % speed_up_limit == speed_up_limit - 1:
                    new_ground.speed -= 1
                    game_speed += 1

                counter = (counter + 1)

                if player_dino.score >= clearScore:
                    gameClear = True
                    break

        if game_quit:
            break
        
        while gameClear:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_n:
                            gameplay_story4()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        gameplay_story4()
            if pygame.display.get_surface() != None:

                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            break

        while game_over:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                # game_over = False

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            game_over = False
                            game_quit = True
                            src.game.intro_screen()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_over = False
                        game_quit = True
                        src.game.intro_screen()

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)


            if pygame.display.get_surface() != None:
                disp_gameover_msg(gameover_image)
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            clock.tick(FPS)

    pygame.quit()
    quit()


def gameplay_story4():
    global resized_screen
    global high_score
    global item_story4
    result = db.query_db("select score from user order by score desc;", one=True)
    if result is not None:
        high_score = result['score']
    #    if bgm_on:
    #       pygame.mixer.music.play(-1) # 배경음악 실행
    game_speed = 4
    startMenu = False
    game_over = False
    gameClear = False
    game_quit = False
    Maskplus = False
    Maskplus_cnt=2
    mask_dino_time=0
    ###
    life = 5
    ###
    paused = False

    if item_story1==True:
        Sunglass_cnt=2
    else:
        Sunglass_cnt=0
    Shovel_time=0
    if item_story2==True:
        Shovel_cnt=2
    else:
        Shovel_cnt=0
    Umbrella_time=0
    if item_story3==True:
        Umbrella_cnt=2
    else:
        Umbrella_cnt=0
    if item_story4==True:
        Maskplus_cnt=2
    else:
        Maskplus_cnt=0

    player_dino = Dino(dino_size[0], dino_size[1])

    new_ground = Ground(-1 * game_speed)

    heart = HeartIndicator(life)
    m_time = Mask_time()
    item_s = Item_status()
    counter = 0

    cacti = pygame.sprite.Group()
    fire_cacti = pygame.sprite.Group()
    pteras = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    # add stones
    stones = pygame.sprite.Group()
    mask_items = pygame.sprite.Group()

    last_obstacle = pygame.sprite.Group()

    Stone.containers = stones

    Cactus.containers = cacti
    fire_Cactus.containers = fire_cacti
    Ptera.containers = pteras
    Cloud.containers = clouds
    Mask_item.containers = mask_items

    # BUTTON IMG LOAD
    # retbutton_image, retbutton_rect = load_image('replay_button.png', 70, 62, -1)
    gameover_image, gameover_rect = load_image('game_over.png', 380, 22, -1)

    #1. 미사일 발사.
    space_go=False
    m_list=[]
    a_list=[]
    bk=0

    #익룡이 격추되었을때
    isDown=False
    boomCount=0

    #방향키 구현
    go_left=False
    go_right=False

    pm_list = []
    pm_pattern1_count=0
    #2단 점프
    jumpingx2=False

    back_image, back_rect = alpha_image("mask_with_items.png", 800, 400, -1)
    


    while not game_quit:
        while startMenu:
            pass
        while not game_over and not gameClear:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                game_over = True


            else:
                screen.fill(background_col)
                screen.blit(back_image, back_rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # 종료
                        game_quit = True
                        game_over = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:  # 스페이스 누르는 시점에 공룡이 땅에 닿아있으면 점프한다.
                            if player_dino.rect.bottom == int(0.9 * height):
                                player_dino.is_jumping = True
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()
                                player_dino.movement[1] = -1 * player_dino.jump_speed

                        if event.key == pygame.K_DOWN:  # 아래방향키를 누르는 시점에 공룡이 점프중이지 않으면 숙인다.
                            if not (player_dino.is_jumping and player_dino.is_dead):
                                player_dino.is_du = True
                        
                        if event.key == pygame.K_LEFT:
                            go_left=True
                        
                        if event.key == pygame.K_RIGHT:
                            go_right=True

                        if event.key == pygame.K_ESCAPE:
                            paused = not paused
                            paused = src.game.pausing()


                        if event.key == pygame.K_s:
                            jumpingx2=True
                        
                        if event.key == pygame.K_a:
                            space_go=True
                            bk=0

                        if event.key == pygame.K_d:
                            if (item_story4 == True) and (Maskplus_cnt!=0):
                                Maskplus = True


                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            player_dino.is_du = False

                        if event.key == pygame.K_a:
                            space_go=False

                        if event.key == pygame.K_LEFT:
                            go_left=False
                        
                        if event.key == pygame.K_RIGHT:
                            go_right=False

                        if event.key == pygame.K_s:
                            jumpingx2=False
                        

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed() == (1, 0, 0) and player_dino.rect.bottom == int(0.9 * height):
                            # (mouse left button, wheel button, mouse right button)
                            player_dino.is_jumping = True
                            if pygame.mixer.get_init() != None:
                                jump_sound.play()
                            player_dino.movement[1] = -1 * player_dino.jump_speed

                        if pygame.mouse.get_pressed() == (0, 0, 1):
                            # (mouse left button, wheel button, mouse right button)
                            if not (player_dino.is_jumping and player_dino.is_dead):
                                player_dino.is_du = True

                    if event.type == pygame.MOUSEBUTTONUP:
                        player_dino.is_du = False

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)

            if not paused:

                if go_left:
                    if player_dino.rect.left < 0:
                        player_dino.rect.left = 0
                    else:
                        player_dino.rect.left = player_dino.rect.left - game_speed

                if go_right:
                    if player_dino.rect.right > width:
                        player_dino.rect.right = width
                    else:
                        player_dino.rect.left = player_dino.rect.left + game_speed

                if (space_go==True) and (int(bk%100)==0):
                    # print(bk)
                    mm=Obj()

                    mm.put_img("./sprites/fire_bullet.png")
                    mm.change_size(15,15)
                    # 
                    
                    if player_dino.is_du ==False:
                        mm.x = round(player_dino.rect.centerx)
                        mm.y = round(player_dino.rect.top*1.035)
                    if player_dino.is_du ==True:
                        mm.x = round(player_dino.rect.centerx)
                        mm.y = round(player_dino.rect.centery*1.01)
                    mm.move = 15
                    m_list.append(mm)
                bk=bk+1
                d_list=[]

                #미사일 하나씩 꺼내옴
                for i in range(len(m_list)):
                    m=m_list[i]
                    m.x +=m.move
                    if m.x>width:
                        d_list.append(i)

                d_list.reverse()
                for d in d_list:
                    del m_list[d]
                #

                if jumpingx2 :
                    if  player_dino.rect.bottom == int(height * 0.9):
                        player_dino.is_jumping = True
                        player_dino.movement[1] = -1 * player_dino.super_jump_speed

                if go_left:
                    if player_dino.rect.left < 0:
                        player_dino.rect.left = 0
                    else:
                        player_dino.rect.left = player_dino.rect.left - game_speed

                if go_right:
                    if player_dino.rect.right > width:
                        player_dino.rect.right = width
                    else:
                        player_dino.rect.left = player_dino.rect.left + game_speed
               


                for s in stones:
                    s.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, s):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                for c in cacti:
                    c.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, c):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False

                for f in fire_cacti:
                    f.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, f):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False
                
                
                for m in mask_items:
                    m.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, m):
                            player_dino.collision_immune = True
                            collision_time = pygame.time.get_ticks()
                            player_dino.score2 = 0
                            m.image.set_alpha(0)
                            
                            if pygame.mixer.get_init() is not None:
                                checkPoint_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False

                for p in pteras:
                    p.movement[0] = -1 * game_speed

                    # 7. 익룡이 미사일에 맞으면 익룡과 미사일 모두 사라집니다.

                    if (len(m_list)==0):
                        pass
                    else:
                        if (m.x>=p.rect.left)and(m.x<=p.rect.right)and(m.y>p.rect.top)and(m.y<p.rect.bottom):
                            print("격추 성공")
                            isDown=True
                            boom=Obj()
                            boom.put_img("./sprites/boom.png")
                            boom.change_size(200,100)
                            boom.x=p.rect.centerx-round(p.rect.width)*2.5
                            boom.y=p.rect.centery-round(p.rect.height)*1.5
                            player_dino.score+=30
                            p.kill()
                            # 여기만 바꿈
                            m_list.remove(m)
                            #
                    #

                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, p):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False


                

                STONE_INTERVAL = 50

                CACTUS_INTERVAL = 50
                MASK_INTERVAL = 50
                PTERA_INTERVAL = 300
                CLOUD_INTERVAL = 300
                OBJECT_REFRESH_LINE = width * 0.8
                MAGIC_NUM = 10
                mask_dino_time+=1
                
                if Maskplus == True:
                    player_dino.Mask=True
                    mask_dino_time=0
                    player_dino.score2 = 0
                    Maskplus = False
                    Maskplus_cnt-=1

                if mask_dino_time==30:
                    player_dino.Mask=False


                if (len(pm_list)==0):
                    pass
                else:
                    # print("x: ",pm.x,"y: ",pm.y)
                    for pm in pm_list:
                        if (pm.x>=player_dino.rect.left)and(pm.x<=player_dino.rect.right)and(pm.y>player_dino.rect.top)and(pm.y<player_dino.rect.bottom):
                            print("공격에 맞음.")
                            # if pygame.sprite.collide_mask(player_dino, pm):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            pm_list.remove(pm)

                if len(cacti) < 2:
                    if len(cacti) == 0 and player_dino.score <= 1:
                        last_obstacle.empty()
                        last_obstacle.add(Cactus(game_speed, object_size[0], object_size[1]))
                    else:
                        for l in last_obstacle:
                            if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL) == MAGIC_NUM:
                                last_obstacle.empty()
                                last_obstacle.add(Cactus(game_speed, object_size[0], object_size[1]))

                if len(fire_cacti) < 2:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL * 5) == MAGIC_NUM:
                            last_obstacle.empty()
                            last_obstacle.add(fire_Cactus(game_speed, object_size[0], object_size[1]))

                if len(stones) < 2:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(STONE_INTERVAL * 3) == MAGIC_NUM:
                            last_obstacle.empty()
                            last_obstacle.add(Stone(game_speed, object_size[0], object_size[1]))

                
                if len(mask_items) < 2:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(MASK_INTERVAL) == MAGIC_NUM:
                            last_obstacle.empty()
                            last_obstacle.add(Mask_item(game_speed, object_size[0], object_size[1]))


                if len(pteras) == 0 and random.randrange(PTERA_INTERVAL) == MAGIC_NUM and counter > PTERA_INTERVAL:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE:
                            last_obstacle.empty()
                            last_obstacle.add(Ptera(game_speed, ptera_size[0], ptera_size[1]))

                if len(clouds) < 5 and random.randrange(CLOUD_INTERVAL) == MAGIC_NUM:
                    Cloud(width, random.randrange(height / 5, height / 2))

                player_dino.update()
                cacti.update()
                fire_cacti.update()
                mask_items.update()
                m_time.update(player_dino.score2)
                pteras.update()
                clouds.update()
                new_ground.update()
                s_scb.update(player_dino.score)
                heart.update(life)
                item_s.update(Sunglass_cnt,Shovel_cnt,Umbrella_cnt,Maskplus_cnt)

                stones.update()
                for a in a_list:
                    a.show()



                if pygame.display.get_surface() != None:
                    new_ground.draw()
                    clouds.draw(screen)
                    s_scb.draw()
                    heart.draw()
                    item_s.draw()
                    cacti.draw(screen)
                    stones.draw(screen)
                    fire_cacti.draw(screen)
                    mask_items.draw(screen)
                    m_time.draw()
                    pteras.draw(screen)
                    for pm in pm_list:
                        pm.show()


                    player_dino.draw()
                    resized_screen.blit(
                        pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                        resized_screen_center)
                    pygame.display.update()
                clock.tick(FPS)

                
                if player_dino.score2 == 100:
                    player_dino.is_dead = True

                if player_dino.is_dead:
                    game_over = True
                    ingame_m.stop() 
                    # pygame.mixer.music.stop()  # 죽으면 배경음악 멈춤
                    if player_dino.score > high_score:
                        high_score = player_dino.score

                if counter % speed_up_limit == speed_up_limit - 1:
                    new_ground.speed -= 1
                    game_speed += 1

                counter = (counter + 1)

                if player_dino.score >= clearScore:
                    gameClear = True
                    break


        if game_quit:
            break
        
        while gameClear:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_n:
                            gameplay_story5()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        gameplay_story5()
            if pygame.display.get_surface() != None:
                screen.blit(clearImage, clearImage_rect)
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            break

        while game_over:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                # game_over = False

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            game_over = False
                            game_quit = True
                            src.game.intro_screen()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_over = False
                        game_quit = True
                        src.game.intro_screen()

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)


            if pygame.display.get_surface() != None:
                disp_gameover_msg(gameover_image)
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            clock.tick(FPS)


    pygame.quit()
    quit()




def gameplay_story5():
    global resized_screen
    global high_score
    global item_story1
    global item_story2
    global item_story3
    global item_story4

    result = db.query_db("select score from user order by score desc;", one=True)
    if result is not None:
        high_score = result['score']
    
    dust_image, dust_rect = load_image('dust.png',800,200,-1)
    Background, Background_rect = alpha_image('human_with_items.png', 800, 200, -1)

    dustnum=0
    dust_image.set_alpha(dustnum)

    game_speed = 4
    startMenu = False
    game_over = False
    game_quit = False
    Sunglass = False
    Shovel = False
    Umbrella = False
    Maskplus = False
    Itemtime = False
    mask_dino_time=0

    if item_story1==True:
        Sunglass_cnt=2
    else:
        Sunglass_cnt=0
    Shovel_time=0
    if item_story2==True:
        Shovel_cnt=2
    else:
        Shovel_cnt=0
    Umbrella_time=0
    if item_story3==True:
        Umbrella_cnt=2
    else:
        Umbrella_cnt=0
    if item_story4==True:
        Maskplus_cnt=2
    else:
        Maskplus_cnt=0

    life = 5
    paused = False
    player_dino = Dino(dino_size[0], dino_size[1], type = dino_type[type_idx])
    new_ground = Ground(-1 * game_speed)
    s_scb = Story_Scoreboard()
    heart = HeartIndicator(life)
    boss = boss_heart()
    m_time = Mask_time()
    item_s = Item_status()
    counter = 0

    cacti = pygame.sprite.Group()
    fire_cacti = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    last_obstacle = pygame.sprite.Group()
    holes = pygame.sprite.Group()
    mask_items = pygame.sprite.Group()

    Cactus.containers = cacti
    purple_Hole.containers = holes
    fire_Cactus.containers = fire_cacti
    Cloud.containers = clouds
    Mask_item.containers = mask_items

    gameover_image, gameover_rect = load_image('game_over.png', 380, 22, -1)
    
    # 1. 미사일 발사.
    space_go=False
    m_list=[]
    bk=0
    # 익룡이 격추되었을때
    isDown=False
    boomCount=0

    # 방향키 구현
    go_left=False
    go_right=False

    # 보스몬스터 변수설정
    isHumanTime=False
    isHumanAlive=True
    human=Human()
    pm_list = [] # 보스의 총알 개수
    rm_list = []
    pm_pattern0_count = 0 # 패턴 0 시간
    pm_pattern1_count = 0 # 패턴 1 시간
    pm_pattern2_count = 0 # 패턴 2 시간
    pm_pattern3_count = 0 # 패턴 3 시간
    human_appearance_score = 100
    
    jumpingx2 = False

    while not game_quit:
        while startMenu:
            pass
        while not game_over:

            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                game_over = True
            else:
                screen.blit(Background, Background_rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:  # 스페이스 누르는 시점에 공룡이 땅에 닿아있으면 점프한다.
                            if player_dino.rect.bottom == int(0.9 * height):
                                player_dino.is_jumping = True
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()
                                player_dino.movement[1] = -1 * player_dino.jump_speed
                        if event.key == pygame.K_DOWN:  # 아래방향키를 누르는 시점에 공룡이 점프중이지 않으면 숙인다.
                            if not (player_dino.is_jumping and player_dino.is_dead):
                                player_dino.is_du = True
                        if event.key == pygame.K_LEFT:
                            go_left=True
                        if event.key == pygame.K_RIGHT:
                            go_right=True
                        if event.key == pygame.K_ESCAPE:
                            paused = not paused
                            paused = src.game.pausing()

                        if event.key == pygame.K_s:
                            jumpingx2=True
                        if event.key == pygame.K_a:
                            space_go=True
                            bk=0
                        if event.key == pygame.K_d:
                            if (isHumanTime):
                                Itemtime=True
                                if (item_story1 == True) and (human.pattern_idx == 0) and (Sunglass_cnt!=0):
                                    Sunglass = True
                                if (item_story2 == True) and (human.pattern_idx == 1) and (Shovel_cnt!=0):
                                    Shovel = True
                                if (item_story3 == True) and (human.pattern_idx == 2) and (Umbrella_cnt!=0):
                                    Umbrella = True
                                if (item_story4 == True) and (human.pattern_idx == 3) and (Maskplus_cnt!=0):
                                    Maskplus = True
                    

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            player_dino.is_du = False
                        if event.key == pygame.K_a:
                            space_go = False
                        if event.key == pygame.K_LEFT:
                            go_left=False
                        if event.key == pygame.K_RIGHT:
                            go_right=False
                        if event.key == pygame.K_s:
                            jumpingx2 = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed() == (1, 0, 0) and player_dino.rect.bottom == int(0.9 * height):
                            # (mouse left button, wheel button, mouse right button)
                            player_dino.is_jumping = True
                            if pygame.mixer.get_init() != None:
                                jump_sound.play()
                            player_dino.movement[1] = -1 * player_dino.jump_speed
                        if pygame.mouse.get_pressed() == (0, 0, 1):
                            # (mouse left button, wheel button, mouse right button)
                            if not (player_dino.is_jumping and player_dino.is_dead):
                                player_dino.is_du = True

                    if event.type == pygame.MOUSEBUTTONUP:
                        player_dino.is_du = False

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)

            if not paused:
                if go_left:
                    if player_dino.rect.left < 0:
                        player_dino.rect.left = 0
                    else:
                        player_dino.rect.left = player_dino.rect.left - game_speed
                if go_right:
                    if player_dino.rect.right > width:
                        player_dino.rect.right = width
                    else:
                        player_dino.rect.left = player_dino.rect.left + game_speed

                #### space_go가 True이고, 일정 시간이 지나면, 미사일을 만들고, 이를 미사일 배열에 넣습니다.
                if (space_go==True) and (int(bk%100)==0):
                    mm=Obj()

                    mm.put_img("./sprites/fire_bullet.png")
                    mm.change_size(15,15)
                    
                    if player_dino.is_du ==False:
                        mm.x = round(player_dino.rect.centerx)
                        mm.y = round(player_dino.rect.top*1.035)
                    if player_dino.is_du ==True:
                        mm.x = round(player_dino.rect.centerx)
                        mm.y = round(player_dino.rect.centery*1.01)
                    mm.move = 15
                    m_list.append(mm)
                bk = bk + 1
                d_list = []

                #### 다이노의 미사일 하나씩 꺼내옴
                for i in range(len(m_list)):
                    m = m_list[i]
                    m.x += m.move
                    if m.x > width:
                        d_list.append(i)
                d_list.reverse()
                for d in d_list:
                    del m_list[d]

                if jumpingx2 :
                    if  player_dino.rect.bottom == int(height * 0.9):
                        player_dino.is_jumping = True
                        player_dino.movement[1] = -1 * player_dino.super_jump_speed


                #### 보스 몬스터 패턴 0 - 미세먼지 모드
                if (isHumanTime) and (human.pattern_idx == 0):          
                    if (player_dino.score%100) < 50: 
                        dustnum = 0       
                    elif 50 <= (player_dino.score%100) < 100: 
                        dustnum = 255


                    # 2. 장애물 이미지 처리 
                    if item_story1==True:
                        if Sunglass == True:
                            player_dino.Superglass = True
                            if (player_dino.score%100) <50:
                                player_dino.Superglass=False
                                Sunglass=False
                                Sunglass_cnt-=1
                            for c in cacti:
                                c.image.set_alpha(255)
                                c.movement[0] = -1 * game_speed
                            for f in fire_cacti:
                                f.image.set_alpha(255)
                                f.movement[0] = -1 * game_speed
                        else:
                            for c in cacti:
                                if (player_dino.score%100) <50:
                                    c.image.set_alpha(255)
                                elif 50<=(player_dino.score%100) < 100:
                                    c.image.set_alpha(30)
                                c.movement[0] = -1 * game_speed

                            for f in fire_cacti:
                                if (player_dino.score%100) <50:
                                    f.image.set_alpha(255)
                                elif 50<=(player_dino.score%100) < 100:
                                    f.image.set_alpha(30)
                                f.movement[0] = -1 * game_speed

                    else:
                        for c in cacti:
                            if (player_dino.score%100) <50:
                                c.image.set_alpha(255)
                            elif 50<=(player_dino.score%100) < 100:
                                c.image.set_alpha(30)
                            c.movement[0] = -1 * game_speed

                        for f in fire_cacti:
                            if (player_dino.score%100) <50:
                                f.image.set_alpha(255)
                            elif 50<=(player_dino.score%100) < 100:
                                f.image.set_alpha(30)
                            f.movement[0] = -1 * game_speed
                    
                    # 3. 보스의 공격
                    if (int(pm_pattern0_count % 80) == 0):
                        pm = Obj()
                        pm.put_img("./sprites/pking bullet.png")
                        pm.change_size(15, 15)
                        pm.x = round(human.rect.centerx)
                        pm.y = round(human.rect.bottom - 45)
                        pm.xmove = random.randint(10, 15)
                        pm_list.append(pm)

                pm_pattern0_count += 1
                pd_list = []

                for i in range(len(pm_list)):
                    pm = pm_list[i]
                    pm.x -= pm.xmove
                    if pm.x < 0:
                        pd_list.append(i)

                pd_list.reverse()
                for d in pd_list:
                    del pm_list[d]


                #### 보스 몬스터 패턴 1 - 지진 모드
                if (isHumanTime) and (human.pattern_idx == 1):
                    if item_story2==True:
                        if Shovel==True:
                            player_dino.Sovel = True
                        else:
                            player_dino.Sovel = False
                    # 1. 보스의 임의 점프
                    JUMP_MAGIC = 50
                    if (human.rect.bottom == int(0.9 * height)):
                        if (random.randrange(0, 100) == JUMP_MAGIC):
                        
                            
                            human.is_jumping = True
                            human.movement[1] = -1 * human.jump_speed

                            for c in cacti:
                                if c.rect.left >= human.rect.left-100: c.kill()
                            for f in fire_cacti:
                                if f.rect.left >= human.rect.left-100: f.kill()

                            new_hole_right = human.rect.left - width
                            last_obstacle.add(purple_Hole(game_speed, object_size[0], object_size[1], new_hole_right))

                    
                    # 3. 보스의 공격

                    if (int(pm_pattern1_count % 80) == 0):
                        pm=Obj()
                        pm.put_img("./sprites/pking bullet.png")
                        pm.change_size(15,15)
                        pm.x = round(human.rect.centerx)
                        pm.y = round(human.rect.bottom - 45)
                        pm.xmove = random.randint(10, 15)
                        pm_list.append(pm)
                    
                pm_pattern1_count += 1
                pd_list = []

                for i in range(len(pm_list)):
                    pm=pm_list[i]
                    pm.x -= pm.move
                    if pm.x < 0:
                        pd_list.append(i)

                pd_list.reverse()
                for d in pd_list:
                    del pm_list[d]

                #### 보스 몬스터 패턴 2 - 산성비 모드

                if (isHumanTime) and (human.pattern_idx == 2):
                    dustnum = 0
                    
                    # 3. 보스의 공격

                    if (int(pm_pattern2_count % 80) == 0):
                        pm = Obj()
                        pm.put_img("./sprites/pking bullet.png")
                        pm.change_size(15, 15)
                        pm.x = round(human.rect.centerx)
                        pm.y = round(human.rect.bottom - 45)
                        pm.xmove = random.randint(10, 15)
                        pm_list.append(pm)


                    if (int(pm_pattern2_count % 30) == 0):
                        rm=Obj()
                        rm.put_img("./sprites/water_drop.png")
                        rm.change_size(40,40)
                        rm.x = random.randrange(player_dino.rect.left, player_dino.rect.right)
                        rm.y = 10
                        rm.move = 3
                        rm_list.append(rm)
                    
                pm_pattern2_count += 1
                pd_list = []
                rd_list = []

                for i in range(len(pm_list)):
                    pm=pm_list[i]
                    pm.y +=pm.move
                    if pm.y>height or pm.x < 0:
                        pd_list.append(i)

                for i in range(len(rm_list)):
                    rm=rm_list[i]
                    rm.y +=rm.move
                    if rm.y>height or rm.x < 0:
                        rd_list.append(i)

                pd_list.reverse()
                for d in pd_list:
                    del pm_list[d]

                rd_list.reverse()
                for r in rd_list:
                    del rm_list[r]



                #### 보스 몬스터 패턴 3 - 바이러스 모드
                if (isHumanTime) and (human.pattern_idx == 3):
                    if Shovel==True:
                        Shovel=False
                        player_dino.Sovel=False

                    dustnum = 0                   
                    
                    # 3. 보스의 공격

                    if (int(pm_pattern3_count % 80) == 0):
                        pm = Obj()
                        pm.put_img("./sprites/pking bullet.png")
                        pm.change_size(15, 15)
                        pm.x = round(human.rect.centerx)
                        pm.y = round(human.rect.bottom - 45)
                        pm.xmove = random.randint(10, 15)
                        pm_list.append(pm)
                    
                pm_pattern3_count += 1
                pd_list = []

                for i in range(len(pm_list)):
                    pm=pm_list[i]
                    pm.y +=pm.move
                    if pm.y>height or pm.x < 0:
                        pd_list.append(i)

                pd_list.reverse()
                for d in pd_list:
                    del pm_list[d]                    


                
                #### 장애물 충돌처리
                for c in cacti:
                    c.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, c):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False

                for f in fire_cacti:
                    f.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, f):
                            player_dino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                player_dino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not player_dino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            player_dino.collision_immune = False
                
                for h in holes:
                    h.movement[0] = -1 * game_speed
                    if not player_dino.collision_immune:
                        if pygame.sprite.collide_mask(player_dino, h):
                            if item_story2==True:
                                if Shovel==True:
                                    player_dino.Sovel=True
                                    h.image.set_alpha(0)  
                                else:
                                    player_dino.Sovel=False
                                    player_dino.collision_immune = True
                                    life -= 5
                                    collision_time = pygame.time.get_ticks()
                                    if life <= 0:
                                        player_dino.is_dead = True
                                    if pygame.mixer.get_init() is not None:
                                        die_sound.play()
                            else: 
                                player_dino.collision_immune = True
                                life -= 5
                                collision_time = pygame.time.get_ticks()
                                if life <= 0:
                                    player_dino.is_dead = True
                                if pygame.mixer.get_init() is not None:
                                    die_sound.play()

                if (isHumanTime) and (human.pattern_idx == 3):
                    for ma in mask_items:
                        ma.movement[0] = -1 * game_speed
                        if not player_dino.collision_immune:
                            if pygame.sprite.collide_mask(player_dino, ma):
                                player_dino.collision_immune = True
                                collision_time = pygame.time.get_ticks()
                                player_dino.score2 = 0
                                ma.image.set_alpha(0)
                                
                                if pygame.mixer.get_init() is not None:
                                    checkPoint_sound.play()

                        elif not player_dino.is_super:
                            immune_time = pygame.time.get_ticks()
                            if immune_time - collision_time > collision_immune_time:
                                player_dino.collision_immune = False

                CACTUS_INTERVAL = 50
                CLOUD_INTERVAL = 300
                OBJECT_REFRESH_LINE = width * 0.8
                MAGIC_NUM = 10
                MASK_INTERVAL = 50

                um=Obj()
                um.put_img("./sprites/umbrella_item.png")
                um.change_size(70,70)
                um.x = (player_dino.rect.left+player_dino.rect.right)/2-40
                um.y = player_dino.rect.bottom - 70
                um.move = 5
                if (Umbrella_time!=1) and (Umbrella_time % 300 == 1):
                    Umbrella_time=0
                    Umbrella=False
                    Umbrella_cnt-=1


                if (isHumanTime):
                    if (Itemtime == True) and (human.pattern_idx == 2) and (Umbrella == True):
                        Umbrella_time+=1
                        if (len(rm_list)==0):
                            pass
                        else:
                            # print("x: ",pm.x,"y: ",pm.y)
                            for rm in rm_list:
                                if (rm.y>=um.y)and(rm.x<=um.x+35)and(rm.x>=um.x-35):
                                    rm.img.set_alpha(0)

                    else:
                        if (len(rm_list)==0): pass # 보스 공격 모션
                        else:
                            for rm in rm_list:
                                if (rm.x>=player_dino.rect.left)and(rm.x<=player_dino.rect.right)and(rm.y>player_dino.rect.top)and(rm.y<player_dino.rect.bottom):
                                    print("공격에 맞음.")
                                    player_dino.collision_immune = True
                                    life -= 1
                                    collision_time = pygame.time.get_ticks()
                                    if life == 0:
                                        player_dino.is_dead = True
                                    rm_list.remove(rm)

                mask_dino_time+=1

                if (isHumanTime) and (Itemtime == True) and (human.pattern_idx == 3) and (Maskplus == True):
                    player_dino.Mask=True
                    mask_dino_time=0
                    player_dino.score2 = 0
                    Maskplus = False
                    Maskplus_cnt-=1
                
                if mask_dino_time == 30:
                    player_dino.Mask=False

                if (isHumanAlive) and (player_dino.score> human_appearance_score):
                    isHumanTime = True
                else:
                    isHumanTime = False
                
                

                if len(cacti) < 2:
                        if len(last_obstacle) == 0:
                            last_obstacle.add(Cactus(game_speed, object_size[0], object_size[1]))
                        else:
                            for l in last_obstacle:
                                if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL) == MAGIC_NUM:
                                    last_obstacle.empty()
                                    last_obstacle.add(Cactus(game_speed, object_size[0], object_size[1]))

                if len(fire_cacti) < 2:
                    for l in last_obstacle:
                        if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(CACTUS_INTERVAL*5) == MAGIC_NUM:
                            last_obstacle.empty()
                            last_obstacle.add(fire_Cactus(game_speed, object_size[0], object_size[1]))

                if len(clouds) < 5 and random.randrange(CLOUD_INTERVAL) == MAGIC_NUM:
                    Cloud(width, random.randrange(height / 5, height / 2))
                # 보스몬스터 타임 - 선인장, 불선인장만 나오도록
                if isHumanTime:

                    if (len(m_list)==0): pass # 다이노 공격 모션
                    else:
                        if (m.x>=human.rect.left)and(m.x<=human.rect.right)and(m.y>human.rect.top)and(m.y<human.rect.bottom):
                            isDown=True
                            boom=Obj()
                            boom.put_img("./sprites/boom.png")
                            boom.change_size(200,100)
                            boom.x=human.rect.centerx-round(human.rect.width)
                            boom.y=human.rect.centery-round(human.rect.height/2)
                            human.hp -= 1
                            m_list.remove(m)

                            if human.hp <= 0:
                                human.kill()
                                isHumanAlive=False
                                ingame_m.stop()
                                Congratulations()


                    if (len(pm_list)==0): pass # 보스 공격 모션
                    else:
                        for pm in pm_list:
                            if (pm.x>=player_dino.rect.left)and(pm.x<=player_dino.rect.right)and(pm.y>player_dino.rect.top)and(pm.y<player_dino.rect.bottom):
                                print("공격에 맞음.")
                                player_dino.collision_immune = True
                                life -= 1
                                collision_time = pygame.time.get_ticks()
                                if life == 0:
                                    player_dino.is_dead = True
                                pm_list.remove(pm)
                    if (isHumanTime) and (human.pattern_idx == 3):
                        if len(mask_items) < 2:
                            for l in last_obstacle:
                                if l.rect.right < OBJECT_REFRESH_LINE and random.randrange(MASK_INTERVAL) == MAGIC_NUM:
                                    last_obstacle.empty()
                                    last_obstacle.add(Mask_item(game_speed, object_size[0], object_size[1]))


                player_dino.update()
                cacti.update()
                fire_cacti.update()
                clouds.update()
                holes.update()
                new_ground.update()
                s_scb.update(player_dino.score)
                boss.update(human.hp)
                heart.update(life)
                mask_items.update()
                m_time.update(player_dino.score2)
                item_s.update(Sunglass_cnt,Shovel_cnt,Umbrella_cnt,Maskplus_cnt)
                if (human.pattern_idx != 3):
                    player_dino.score2 = 0

                # 보스몬스터 타임이면,
                if isHumanTime:
                    human.update()
                

                if (Shovel==True):
                    Shovel_time+=1

                if (Shovel_time!=1) and (Shovel_time % 300 == 1):
                    Shovel_time=0
                    Shovel=False
                    Shovel_cnt-=1
                    player_dino.Sovel=True
                    

                if pygame.display.get_surface() != None:
                    screen.fill(background_col)
                    screen.blit(Background, Background_rect)
                    dust_image.set_alpha(dustnum)
                    screen.blit(dust_image, dust_rect)
                    new_ground.draw()
                    clouds.draw(screen)
                    s_scb.draw()
                    boss.draw()
                    heart.draw()
                    cacti.draw(screen)
                    holes.draw(screen)
                    fire_cacti.draw(screen)
                    item_s.draw()
                    item_s.update(Sunglass_cnt,Shovel_cnt,Umbrella_cnt,Maskplus_cnt)
                    if (isHumanTime) and (human.pattern_idx == 3):
                        mask_items.draw(screen)
                        m_time.draw()
                        

                    # pkingtime이면, 보스몬스터를 보여줘라.
                    if isHumanTime:
                        human.draw()
                        for pm in pm_list: pm.show()

                    if (isHumanTime) and (human.pattern_idx == 2):
                        human.draw()
                        for rm in rm_list: rm.show()

                   # 5. 미사일 배열에 저장된 미사일들을 게임 스크린에 그려줍니다.
                    for m in m_list:
                        m.show()
                        # print(type(mm.x))
                    if isDown :
                        boom.show()
                        boomCount+=1
                        # boomCount가 5가 될 때까지 boom이미지를 계속 보여준다.
                        if boomCount>10:
                            boomCount=0
                            isDown=False
                    #
                    if (isHumanTime):
                        if (Itemtime == True) and (human.pattern_idx == 2) and (Umbrella == True):
                            um.show()
                    
                    
                    player_dino.draw()
                    resized_screen.blit(
                        pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                        resized_screen_center)
                    pygame.display.update()
                clock.tick(FPS)

                if player_dino.score2 == 100:
                    player_dino.is_dead = True

                if player_dino.is_dead:
                    game_over = True
                    ingame_m.stop() 
                    # pygame.mixer.music.stop()  # 죽으면 배경음악 멈춤
                    if player_dino.score > high_score:
                        high_score = player_dino.score

                if counter % speed_up_limit == speed_up_limit - 1:
                    new_ground.speed -= 1
                    game_speed += 1

                counter = (counter + 1)

        if game_quit:
            break

        while game_over:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                # game_over = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            game_over = False
                            game_quit = True
                            typescore(player_dino.score)
                            if not db.is_limit_data(player_dino.score):
                                db.query_db(
                                    f"insert into user(username, score) values ('{gamername}', '{player_dino.score}');")
                                db.commit()
                                board()
                            else:
                                board()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_over = False
                        game_quit = True
                        typescore(player_dino.score)
                        if not db.is_limit_data(player_dino.score):
                            db.query_db(
                                f"insert into user(username, score) values ('{gamername}', '{player_dino.score}');")
                            db.commit()
                            board()
                        else: 
                            board()

                    if event.type == pygame.VIDEORESIZE:
                        check_scr_size(event.w, event.h)

            s_scb.update(player_dino.score)
            boss.update(human.hp)
            if pygame.display.get_surface() != None:
                disp_gameover_msg(gameover_image)
                s_scb.draw()
                boss.draw()
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            clock.tick(FPS)

    pygame.quit()
    quit()

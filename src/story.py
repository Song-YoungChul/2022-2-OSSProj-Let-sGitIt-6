from src.dino import *
from src.obstacle import *
from src.item import *
from src.interface import *
from src.game import * 
from db.db_interface import InterfDB
from time import sleep

db = InterfDB("db/score.db")
clear_score = 200
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
    game_clear = False
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

    playerDino = Dino(dino_size[0], dino_size[1])

    new_ground = Ground(-1 * game_speed)
    # s_scb = Story_Scoreboard()
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
    is_down=False
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
        while not game_over and not game_clear:
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
                            if playerDino.rect.bottom == int(0.98 * height):
                                playerDino.is_jumping = True
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()
                                playerDino.movement[1] = -1 * playerDino.jump_speed

                        if event.key == pygame.K_DOWN:  # 아래방향키를 누르는 시점에 공룡이 점프중이지 않으면 숙인다.
                            if not (playerDino.is_jumping and playerDino.is_dead):
                                playerDino.is_ducking = True
                        
                        if event.key == pygame.K_LEFT:
                            go_left=True
                        
                        if event.key == pygame.K_RIGHT:
                            go_right=True

                        if event.key == pygame.K_ESCAPE:
                            paused = not paused
                            paused = pausing()

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
                            playerDino.is_ducking = False

                        if event.key == pygame.K_a:
                            space_go=False

                        if event.key == pygame.K_LEFT:
                            go_left=False
                        
                        if event.key == pygame.K_RIGHT:
                            go_right=False

                        if event.key == pygame.K_s:
                            jumpingx2=False
                        

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed() == (1, 0, 0) and playerDino.rect.bottom == int(0.9 * height):
                            # (mouse left button, wheel button, mouse right button)
                            playerDino.is_jumping = True
                            if pygame.mixer.get_init() != None:
                                jump_sound.play()
                            playerDino.movement[1] = -1 * playerDino.jump_speed

                        if pygame.mouse.get_pressed() == (0, 0, 1):
                            # (mouse left button, wheel button, mouse right button)
                            if not (playerDino.is_jumping and playerDino.is_dead):
                                playerDino.is_ducking = True

                    if event.type == pygame.MOUSEBUTTONUP:
                        playerDino.is_ducking = False

                    if event.type == pygame.VIDEORESIZE:
                        checkscrsize(event.w, event.h)

            if not paused:

                if go_left:
                    if playerDino.rect.left < 0:
                        playerDino.rect.left = 0
                    else:
                        playerDino.rect.left = playerDino.rect.left - game_speed

                if go_right:
                    if playerDino.rect.right > width:
                        playerDino.rect.right = width
                    else:
                        playerDino.rect.left = playerDino.rect.left + game_speed

                if (space_go==True) and (int(bk%100)==0):
                    # print(bk)
                    mm=obj()
                    mm.put_img("./sprites/fire_bullet.png")
                    mm.change_size(15,15)
                    # 
                    
                    if playerDino.is_ducking ==False:
                        mm.x = round(playerDino.rect.centerx)
                        mm.y = round(playerDino.rect.top*1.035)
                    if playerDino.is_ducking ==True:
                        mm.x = round(playerDino.rect.centerx)
                        mm.y = round(playerDino.rect.centery*1.01)
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
                    if  playerDino.rect.bottom == int(height * 0.98):
                        playerDino.is_jumping = True
                        playerDino.movement[1] = -1 * playerDino.super_jump_speed 

                if go_left:
                    if playerDino.rect.left < 0:
                        playerDino.rect.left = 0
                    else:
                        playerDino.rect.left = playerDino.rect.left - game_speed

                if go_right:
                    if playerDino.rect.right > width:
                        playerDino.rect.right = width
                    else:
                        playerDino.rect.left = playerDino.rect.left + game_speed
               


                for s in stones:
                    s.movement[0] = -1 * game_speed
                    if not playerDino.collision_immune:
                        if pygame.sprite.collide_mask(playerDino, s):
                            playerDino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                playerDino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                for c in cacti:
                    c.movement[0] = -1 * game_speed
                    if not playerDino.collision_immune:
                        if pygame.sprite.collide_mask(playerDino, c):
                            playerDino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                playerDino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not playerDino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            playerDino.collision_immune = False

                for f in fire_cacti:
                    f.movement[0] = -1 * game_speed
                    if not playerDino.collision_immune:
                        if pygame.sprite.collide_mask(playerDino, f):
                            playerDino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                playerDino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not playerDino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            playerDino.collision_immune = False
                
                
                for m in mask_items:
                    m.movement[0] = -1 * game_speed
                    if not playerDino.collision_immune:
                        if pygame.sprite.collide_mask(playerDino, m):
                            playerDino.collision_immune = True
                            collision_time = pygame.time.get_ticks()
                            playerDino.score2 = 0
                            m.image.set_alpha(0)
                            
                            # if pygame.mixer.get_init() is not None:
                            #    # check_point_sound.play()

                    elif not playerDino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            playerDino.collision_immune = False

                for p in pteras:
                    p.movement[0] = -1 * game_speed

                    # 7. 익룡이 미사일에 맞으면 익룡과 미사일 모두 사라집니다.

                    if (len(m_list)==0):
                        pass
                    else:
                        if (m.x>=p.rect.left)and(m.x<=p.rect.right)and(m.y>p.rect.top)and(m.y<p.rect.bottom):
                            print("격추 성공")
                            is_down=True
                            boom=obj()                            
                            boom.put_img("./sprites/boom.png")
                            boom.change_size(200,100)
                            boom.x=p.rect.centerx-round(p.rect.width)*2.5
                            boom.y=p.rect.centery-round(p.rect.height)*1.5
                            playerDino.score+=30
                            p.kill()
                            # 여기만 바꿈
                            m_list.remove(m)
                            #
                    #

                    if not playerDino.collision_immune:
                        if pygame.sprite.collide_mask(playerDino, p):
                            playerDino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                playerDino.is_dead = True
                            if pygame.mixer.get_init() is not None:
                                die_sound.play()

                    elif not playerDino.is_super:
                        immune_time = pygame.time.get_ticks()
                        if immune_time - collision_time > collision_immune_time:
                            playerDino.collision_immune = False

                STONE_INTERVAL = 50

                CACTUS_INTERVAL = 50
                MASK_INTERVAL = 50
                PTERA_INTERVAL = 300
                CLOUD_INTERVAL = 300
                OBJECT_REFRESH_LINE = width * 0.8
                MAGIC_NUM = 10
                mask_dino_time+=1
                
                if Maskplus == True:
                    playerDino.Mask=True
                    mask_dino_time=0
                    playerDino.score2 = 0
                    Maskplus = False
                    Maskplus_cnt-=1

                if mask_dino_time==30:
                    playerDino.Mask=False


                if (len(pm_list)==0):
                    pass
                else:
                    # print("x: ",pm.x,"y: ",pm.y)
                    for pm in pm_list:
                        if (pm.x>=playerDino.rect.left)and(pm.x<=playerDino.rect.right)and(pm.y>playerDino.rect.top)and(pm.y<playerDino.rect.bottom):
                            print("공격에 맞음.")
                            # if pygame.sprite.collide_mask(playerDino, pm):
                            playerDino.collision_immune = True
                            life -= 1
                            collision_time = pygame.time.get_ticks()
                            if life == 0:
                                playerDino.is_dead = True
                            pm_list.remove(pm)

                if len(cacti) < 2:
                    if len(cacti) == 0 and playerDino.score <= 1:
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

                playerDino.update()
                cacti.update()
                fire_cacti.update()
                mask_items.update()
                m_time.update(playerDino.score2)
                pteras.update()
                clouds.update()
                new_ground.update()
                # s_scb.update(playerDino.score)
                heart.update(life)
                item_s.update(Sunglass_cnt,Shovel_cnt,Umbrella_cnt,Maskplus_cnt)

                stones.update()
                for a in a_list:
                    a.show()



                if pygame.display.get_surface() != None:
                    new_ground.draw()
                    clouds.draw(screen)
                    # s_scb.draw()
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


                    playerDino.draw()
                    resized_screen.blit(
                        pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                        resized_screen_center)
                    pygame.display.update()
                clock.tick(FPS)

                
                if playerDino.score2 == 100:
                    playerDino.is_dead = True

                if playerDino.is_dead:
                    game_over = True
                    # ingame_m.stop() 
                    # pygame.mixer.music.stop()  # 죽으면 배경음악 멈춤
                    if playerDino.score > high_score:
                        high_score = playerDino.score

                if counter % speed_up_limit == speed_up_limit - 1:
                    new_ground.speed -= 1
                    game_speed += 1

                counter = (counter + 1)

                if playerDino.score >= clear_score:
                    game_clear = True
                    break


        if game_quit:
            break
        
        while game_clear:
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
                            introscreen()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_over = False
                        game_quit = True
                        introscreen()

                    if event.type == pygame.VIDEORESIZE:
                        checkscrsize(event.w, event.h)


            if pygame.display.get_surface() != None:
                disp_game_over_msg(gameover_image)
                resized_screen.blit(
                    pygame.transform.scale(screen, (resized_screen.get_width(), resized_screen.get_height())),
                    resized_screen_center)
                pygame.display.update()
            clock.tick(FPS)


    pygame.quit()
    quit()

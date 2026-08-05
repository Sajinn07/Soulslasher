import pygame, random, math, time
pygame.init()
pygame.mixer.init()

#IMPORTING EVERY NECESSARY CLASSES AND ASSETS

import assets
from player import Player, PlayerHealthBar, SlashProjectile
from enemy import Enemy, EnemyHealthBar
from boss import  Boss, BossHealthBar, BossPunch
from level2 import Platforms, Level2
from game_states import States
from ui import UI

#MUSIC
pygame.mixer.music.load("GameAssets/Menu/music.mp3")
pygame.mixer.music.play(-1)

#OTHER 
game_window = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("SpeedSlasher")
fps = pygame.time.Clock()
mouse_click = pygame.mouse.get_pressed()
slash_text_fade = 0

#OBJECTS AND ENTITIES CREATION

player = Player(10, 560, assets)
enemy = Enemy(assets)
boss = Boss(600, 425, assets)
punch = BossPunch(assets)
level2 = Level2()
state = States()
ui = UI()
playerhealthbar = PlayerHealthBar(108.7,60, 295,10, 100)
enemyhealthbar = EnemyHealthBar(20,0, 60,5, 100)   
bosshealthbar = BossHealthBar(72,59, 292,10, 100)
projectiles = []
healthpacks = []
gate1 = pygame.draw.rect(assets.nightsky,(0, 0, 0), (850,550, 70, 70))
door = assets.door1
door_rect = door.get_rect(topleft =(830,510))

#NEW/RESET SAVE FUNCTION (WHILE GAME IS RUNNING)

def new_save():
    global player, enemy, boss, punch, level2, door
    global playerhealthbar, enemyhealthbar, bosshealthbar
    global projectiles, healthpacks, platforms
    
    
    projectiles = []
    healthpacks = []

    platforms = [
        Platforms(random.randint(540, 810),500, assets.platform1, speed=2, dir="right"),
        Platforms(random.randint(0, 270),370, assets.platform1, speed=2, dir="right"),
        Platforms(random.randint(270, 540),240, assets.platform1, speed=2, dir="left")
    ]

    punch = BossPunch( assets)

    player = Player(10, 560, assets)
    enemy = Enemy( assets)
    boss = Boss(600, 425, assets)
    playerhealthbar = PlayerHealthBar(108.7,60, 295,10, 100)
    enemyhealthbar = EnemyHealthBar(20,0, 60,5, 100)
    bosshealthbar = BossHealthBar(72,59, 292,10, 100)

    level2 = Level2()
    state.start_time = None
    state.end_time = None
    state.save_created = True

    ui.interact_text_button = ui.interact_text.get_rect(topleft=(825,530))  
    ui.controls_button = ui.controls_text.get_rect(topleft=(460, 320))
    ui.backtogame_button = ui.backtogame_text.get_rect(topleft=(435, 250))
    ui.mainmenu_button = ui.mainmenu_text.get_rect(topleft=(365, 390))


    door = assets.door1

#MAIN GAME LOOP

while state.game_running:

    #GAME MAIN MENU
    
    while state.game_state == "Menu":

        #USER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game_state = "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:

                if ui.continue_button.collidepoint(event.pos):

                    if state.save_created:
                        projectiles.clear()
                        player.x = 10
                        player.y = 560
                        player.ground_y = 560
                        player.state = "idle"
                        player.dir = "right"
                        state.game_state = "Lobby"
                
                if ui.play_button.collidepoint(event.pos):
                    if not state.save_created:
                        new_save()          
                        state.game_state = "Lobby"
                        state.start_time = time.time()    
                
                if ui.quit_button.collidepoint(event.pos):
                    state.game_state = "Quit"
                    
                if ui.options_button.collidepoint(event.pos):
                    state.previous_game_state = "Menu"
                    state.game_state = "Settings"
            
            mouse_pos = pygame.mouse.get_pos()

            #CALLING FUNCTION TO FIX UI ELEMENTS
            ui.state_fix(state)


            #DRAWIING MAIN MENU ELEMENTS
            game_window.blit(assets.background, (0,0))
            game_window.blit(ui.game_name_text, ui.game_name_rect)
            
            
            if state.save_created:
                game_window.blit(ui.continue_text, ui.continue_button)
            else:
                game_window.blit(ui.play_text, ui.play_button) 
            
           
            game_window.blit(ui.options_text, ui.options_button) 
            game_window.blit(ui.quit_text, ui.quit_button)

            fps.tick(60)
            pygame.display.update()


    #SETTINGS MENU

    while state.game_state == "Settings":
        
        #CALLING FUNCTION TO FIX UI ELEMENTS
        ui.state_fix(state)

        #USER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game_state = "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ui.controls_button.collidepoint(event.pos):
                    state.game_state = "Controls"
                if ui.mainmenu_button.collidepoint(event.pos):
                        ui.interact_text_button = ui.interact_text.get_rect(topleft=(825,530))
                        state.game_state = "Menu"
                if ui.backtogame_button.collidepoint(event.pos) and state.in_level:
                        state.game_state = state.previous_game_state
                if assets.mute_button.collidepoint(mouse_pos):
                    if state.music_state == "Unmuted":
                        state.music_state = "Muted"
                        pygame.mixer.music.pause()
                    else: 
                        state.music_state = "Unmuted"
                        pygame.mixer.music.unpause()
            
            mouse_pos = pygame.mouse.get_pos()

            #DRAWING SETTINGS MENU ELEMENTS
            game_window.blit(assets.settings_bg, (0,0))
            if state.music_state == "Unmuted":
                assets.mute = pygame.image.load("GameAssets/Menu/music_unmuted.png").convert_alpha()
                assets.mute = pygame.transform.scale(assets.mute,(64,64))
                game_window.blit(assets.mute, assets.mute_button)
            else:
                assets.mute = pygame.image.load("GameAssets/Menu/music_muted.png").convert_alpha()
                assets.mute = pygame.transform.scale(assets.mute,(64,64))
                game_window.blit(assets.mute, assets.mute_button)
            
            
            game_window.blit(ui.controls_text, ui.controls_button) 
            game_window.blit(ui.mainmenu_text, ui.mainmenu_button) 
            game_window.blit(ui.settings_text, ui.settings_rect)
            if state.in_level:
                game_window.blit(ui.backtogame_text, ui.backtogame_button)

            fps.tick(60)
            pygame.display.update()


    #CONTROLS MENU

    while state.game_state == "Controls":

        #USER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game_state = "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ui.backtosettings_button.collidepoint(event.pos):
                        
                        state.game_state = "Settings"
            
            mouse_pos = pygame.mouse.get_pos()

            #CALLING FUNCTION TO FIX UI ELEMENTS
            ui.state_fix(state)

            #DRAWING CONTROLS MENU ELEMENTS
            game_window.fill((234, 221, 199))
            game_window.blit(assets.settings_bg, (0,0))
            game_window.blit(ui.backtosettings_text, ui.backtosettings_button)

            #MOVEMENT
            game_window.blit(ui.moves_text, ui.moves_text_rect)
            game_window.blit(ui.right_text, ui.right_text_rect)
            game_window.blit(ui.left_text, ui.left_text_rect)
            game_window.blit(ui.jump_text, ui.jump_text_rect)
            game_window.blit(ui.dash_text, ui.dash_text_rect)
            game_window.blit(ui.light_text, ui.light_text_rect)
            game_window.blit(ui.slash_text, ui.slash_text_rect)

            #KEYBINDS
            game_window.blit(ui.keybinds_text, ui.keybinds_text_rect)
            game_window.blit(ui.d_text, ui.d_text_rect)
            game_window.blit(ui.a_text, ui.a_text_rect)
            game_window.blit(ui.space_text, ui.space_text_rect)
            game_window.blit(ui.l_text, ui.l_text_rect)
            game_window.blit(ui.j_text, ui.j_text_rect)
            game_window.blit(ui.k_text, ui.k_text_rect)
            
            fps.tick(60)
            pygame.display.update()


    #DEATH SCREEN

    while state.game_state == "Death Screen":
        
        #USER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game_state = "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ui.mainmenu_button.collidepoint(event.pos):
                        new_save()
                        state.save_created = False
                        state.game_state = "Menu"

            mouse_pos = pygame.mouse.get_pos()     

            #CALLING FUNCTION TO FIX UI ELEMENTS    
            ui.state_fix(state)      
            
            #DRAWING DEATH SCREEN ELEMENTS
            game_window.fill((0,0,0))
            game_window.blit(ui.death_text, ui.death_rect)    
            game_window.blit(ui.mainmenu_text, ui.mainmenu_button)    

            fps.tick(60)
            pygame.display.update()
    

    #WIN SCREEN

    while state.game_state == "Win Screen":
        
        #USER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game_state = "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ui.mainmenu_button.collidepoint(event.pos):
                        new_save()
                        state.save_created = False
                        state.game_state = "Menu"
            
            mouse_pos = pygame.mouse.get_pos()
            
            #CALLING FUNCTION TO FIX UI ELEMENTS
            ui.state_fix(state)

            #DRAWING WIN SCREEN ELEMENTS
            game_window.blit(assets.win_bg, (0,0))
            game_window.blit(total_time, (375, 430))
            game_window.blit(ui.win_text, ui.win_rect)    
            game_window.blit(ui.mainmenu_text, ui.mainmenu_button)    

            fps.tick(60)
            pygame.display.update()
    

    #LOBBY
     
    while state.game_state == "Lobby":
        
        #MAPS USER INPUT TO MOVE PLAYER RIGHT OR LEFT
        user_inp = pygame.key.get_pressed()
        player.movement(user_inp[pygame.K_a], user_inp[pygame.K_d])

        #USER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game_state = "Quit"
            if event.type == pygame.KEYDOWN:
                                                        
                if event.key == pygame.K_SPACE:
                    player.jump()

                if event.key == pygame.K_UP:  
                    player.jump()

                if event.key == pygame.K_j:
                    player.light_attk()

                if event.key == pygame.K_ESCAPE:
                        state.previous_game_state = "Lobby"
                        state.game_state = "Settings"

                if event.key == pygame.K_l:
                    player.dash()

                if event.key == pygame.K_k:
                    slash_text_fade = time.time() + 1
                    if enemy.count >= 5:
                        player.slash_attk()
                        if player.dir == "right":
                            slash = SlashProjectile(player.x +30, player.y -50, random.choice([assets.player_slash_r1, assets.player_slash_r2, assets.player_slash_r3, assets.player_slash_r4]), speed=8, dir="right", game_state = state.game_state)
                        elif player.dir == "left":
                            slash = SlashProjectile(player.x -105, player.y - 50, random.choice([assets.player_slash_l1, assets.player_slash_l2, assets.player_slash_l3, assets.player_slash_l4]), speed=8, dir="left", game_state = state.game_state)
                        projectiles.append(slash)
                    
                
                if event.key == pygame.K_e:
                    if player.rect.colliderect(gate1):
                        projectiles.clear()
                        
                        player.x = 0
                        player.y = 590
                        player.ground_y = 590
                        state.game_state = "Level1"
        
        #CALLING FUNCTION TO FIX UI ELEMENTS
        ui.state_fix(state)

        #UPDATING PLAYER STATES
        player.update()    
        
        #DRAWING LOBBY ELEMENTS, PLAYER AND HEALTHBAR
        game_window.blit(assets.nightsky, (0,0))
        game_window.blit(assets.lobby_ground, (0, 620))
        game_window.blit(assets.castle, (632, 375))
        game_window.blit(assets.sign, (580, 558))
        game_window.blit(ui.tips_text, ui.tips_text_rect)
        player.draw(game_window)
        game_window.blit(assets.playerhealthbar_img, (0,0))
        playerhealthbar.draw(assets.playerhealthbar_img, state)
        
        #DOOR INTERACTION TEXT
        if player.rect.colliderect(gate1):
            game_window.blit(ui.interact_text, ui.interact_text_button)
        
        #SLASH ATTACK UNLOCK TEXT
        if enemy.count < 5:
            if time.time() < slash_text_fade:
              game_window.blit(ui.slash_locked_text, ui.slash_locked_rect)
        
        #UPDATING, DRAWING AND ERROR HANDLING FOR SLASH PROJECTILES
        for slash in projectiles[:]:
            slash.update()
            slash.draw(game_window)
            if slash.x > 1080 or slash.x < -100:
                projectiles.remove(slash)

        fps.tick(60)
        pygame.display.update()
    

    #LEVEL 1

    while state.game_state == "Level1":

        #MAPS USER INPUT TO MOVE PLAYER RIGHT OR LEFT
        user_inp = pygame.key.get_pressed()
        player.movement(user_inp[pygame.K_a], user_inp[pygame.K_d])

        #USER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game_state = "Quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
        
                if event.key == pygame.K_j:
                    player.light_attk()
            
                if event.key == pygame.K_ESCAPE:
                        state.previous_game_state = "Level1"
                        state.game_state = "Settings"
                
                if event.key == pygame.K_k:
                    slash_text_fade = time.time() + 1
                    if enemy.count >= 5:
                        player.slash_attk()
                        if player.dir == "right":
                            slash = SlashProjectile(player.x +30, player.y -50, random.choice([assets.player_slash_r1, assets.player_slash_r2, assets.player_slash_r3, assets.player_slash_r4]), speed=8, dir="right", game_state = state.game_state)
                        elif player.dir == "left":
                            slash = SlashProjectile(player.x -105, player.y - 50, random.choice([assets.player_slash_l1, assets.player_slash_l2, assets.player_slash_l3, assets.player_slash_l4]), speed=8, dir="left", game_state = state.game_state)
                        projectiles.append(slash)

                if event.key == pygame.K_l:
                    player.dash()
   
                if event.key == pygame.K_e:
                    if player.rect.colliderect(door_rect) and enemy.count >= 5:
                        projectiles.clear()
                        player.x = 0
                        player.y = 580
                        player.ground_y = 580
                        state.game_state = "Level2"
        
        #CALLING FUNCTION TO FIX UI ELEMENTS
        ui.state_fix(state) 

        #DRAWING LEVEL 1 ELEMENTS AND PLAYER
        ui.interact_text_button = ui.interact_text.get_rect(topleft=(847,480))
        player.update()
        game_window.blit(assets.level1_bg, (0,0))
        game_window.blit(door, (830,510))
        
        #UPDATING, DRAWING AND ERROR HANDLING FOR HEALTHPACKS
        for drop in healthpacks[:]:
            drop.update()
            drop.draw(game_window)
            if player.rect.colliderect(drop.rect):
                playerhealthbar.heal(10)
                healthpacks.remove(drop)
        
        #UPDATING ENEMY INDICATOR STATES
        enemy.enemies_indicator()

        #DRAWING ENEMY, ENEMY HEALTHBAR AND CHECKING FOR INTERACTIONS WITH PLAYER
        game_window.blit(enemy.eye_state, (507,183))
        if enemy.count >= enemy.max_spawns:
            door = assets.door2
            game_window.blit(ui.slash_unlocked_text, ui.slash_unlocked_rect)

            if player.rect.colliderect(door_rect):
                game_window.blit(ui.interact_text, ui.interact_text_button)

        elif enemy.count < enemy.max_spawns:
            if time.time() < slash_text_fade:
              game_window.blit(ui.slash_locked_text, ui.slash_locked_rect)

        if enemy.state not in ("summon"):
            enemyhealthbar.draw(enemy.image, enemy, healthpacks)

        if not enemy.dead:
            enemy.draw(game_window)
            enemy.enemy_states(player, playerhealthbar,enemyhealthbar)

        
        #UPDATING, DRAWING AND ERROR HANDLING FOR SLASH PROJECTILES
        for slash in projectiles[:]:
            slash.update()
            slash.draw(game_window)
            if slash.x > 1080 or slash.x < -100:
                projectiles.remove(slash)
        
        #DRAWING LEVEL 2 PILLARS, PLAYER AND PLAYERHEALTHBAR
        player.draw(game_window)
        game_window.blit(assets.level1_pillars, (0,0))
        playerhealthbar.draw(assets.playerhealthbar_img, state)
        game_window.blit(assets.playerhealthbar_img, (0,0))


        fps.tick(60)
        pygame.display.update()
    
    
    #LEVEL 2

    while state.game_state == "Level2":

        #MAPS USER INPUT TO MOVE PLAYER RIGHT OR LEFT
        user_inp = pygame.key.get_pressed()
        player.movement(user_inp[pygame.K_a], user_inp[pygame.K_d])

        #USER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game_state = "Quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                
                if event.key == pygame.K_j:
                    player.light_attk()

                if event.key == pygame.K_k:
                    player.slash_attk()
                    if player.dir == "right":
                        slash = SlashProjectile(player.x +30, player.y -50, random.choice([assets.player_slash_r1, assets.player_slash_r2, assets.player_slash_r3, assets.player_slash_r4]), speed=8, dir="right", game_state = state.game_state)

                    elif player.dir == "left":
                        slash = SlashProjectile(player.x -105, player.y - 50, random.choice([assets.player_slash_l1, assets.player_slash_l2, assets.player_slash_l3, assets.player_slash_l4]), speed=8, dir="left", game_state = state.game_state)
                    projectiles.append(slash)
                if event.key == pygame.K_l:
                    player.dash()
                
                if event.key == pygame.K_ESCAPE:
                        state.previous_game_state = "Level2"
                        state.game_state = "Settings"

                if event.key == pygame.K_e:
                    if player.rect.colliderect(level2.door_rect) and level2.door_state == "opened":
                        projectiles.clear()
                        player.x = 0
                        player.y = 556
                        player.ground_y = 556
                        state.game_state = "BossLevel"
        
        #CALLING FUNCTION TO FIX UI ELEMENTS
        ui.state_fix(state)

        #DRAWING AND UPDATING LEVEL 2 ELEMENTS
        game_window.blit(assets.level2_bg, (0,0))
        game_window.blit(assets.playerhealthbar_img, (0,0))
        level2.update()
        level2.draw(game_window)
        game_window.blit(ui.tips2_text, ui.tips2_text_rect)

        #DRAWING AND UPDATING PLAYER AND PLAYER HEALTHBAR
        player.update()
        player.draw(game_window)
        playerhealthbar.draw(assets.playerhealthbar_img, state)
    
        #HANDLING PLATFORM COLLISIONS, MOVEMENT AND DRAWING
        for plat in platforms:
            plat.update()
            plat.draw(game_window)
            
            if player.rect.colliderect(plat.rect) and player.grav >= 0:
                if player.rect.bottom <= plat.rect.bottom:
                    player.y = plat.rect.top - player.rect.height
                    player.grav = 0
                    player.jump_count = 0
                    player.on_ground = True
                    if plat.dir == "right":
                        player.x += 2
                    else:
                        player.x -= 2
        
        ui.interact_text_button = ui.interact_text.get_rect(topleft=(level2.door_rect.x + 10, level2.door_rect.y -30))  
        
        #UPDATING, DRAWING AND ERROR HANDLING FOR SLASH PROJECTILES
        for slash in projectiles[:]:
            slash.update()
            slash.draw(game_window)
            if slash.x > 1080 or slash.x < -100:
                projectiles.remove(slash)

            if slash.rect.colliderect(level2.circ_col_rect):
                level2.circ_state_activated = True
            elif slash.rect.colliderect(level2.rect_col_rect):
                level2.rect_state_activated = True
            elif slash.rect.colliderect(level2.per_col_rect):
                level2.per_state_activated = True

        #DOOR INTERACTION TEXT
        if player.rect.colliderect(level2.door_rect) and level2.door_state == "opened":
            game_window.blit(ui.interact_text, ui.interact_text_button)
        

        fps.tick(60)
        pygame.display.update()
    
    
    #BOSS LEVEL

    while state.game_state == "BossLevel":

        #MAPS USER INPUT TO MOVE PLAYER RIGHT OR LEFT
        user_inp = pygame.key.get_pressed()
        player.movement(user_inp[pygame.K_a], user_inp[pygame.K_d])
        
        #USER EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state.game_state = "Quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
        

                if event.key == pygame.K_j:
                    player.light_attk()
                    
                if event.key == pygame.K_k:
                    player.slash_attk()
                    if player.dir == "right":
                        proj = SlashProjectile(player.x +30, player.y -50, random.choice([assets.player_slash_r1, assets.player_slash_r2, assets.player_slash_r3, assets.player_slash_r4]), speed=8, dir="right", game_state = state.game_state)

                    elif player.dir == "left":
                        proj = SlashProjectile(player.x -105, player.y - 50, random.choice([assets.player_slash_l1, assets.player_slash_l2, assets.player_slash_l3, assets.player_slash_l4]), speed=8, dir="left", game_state = state.game_state)
                    projectiles.append(proj)      

                if event.key == pygame.K_l:
                    player.dash()
                
                if event.key == pygame.K_ESCAPE:
                        state.previous_game_state = "BossLevel"
                        state.game_state = "Settings"
        
        #CALLING FUNCTION TO FIX UI ELEMENTS
        ui.state_fix(state)
        player.update()
        
        game_window.blit(assets.boss_bg, (0,0))
        game_window.blit(assets.playerhealthbar_img, (0,0))

        #UPDATING, DRAWING AND CHECKING INTERACTIONS FOR BOSS
        if not boss.dead:
            boss.draw(game_window)
            boss.boss_states(player, playerhealthbar, bosshealthbar, punch)
        
        punch.sprite_animation(boss, playerhealthbar, player, bosshealthbar)
        punch.draw(game_window)

        #DRAWING BOSS AND PLAYER HEALTHBARS
        bosshealthbar.draw(assets.bosshealthbar_img)
        game_window.blit(assets.bosshealthbar_img, (600,5))
        playerhealthbar.draw(assets.playerhealthbar_img, state)
        
        #UPDATING, DRAWING AND ERROR HANDLING FOR SLASH PROJECTILES ALONG WITH DAMAGE DONE TO BOSS WHEN HIT
        for slash in projectiles[:]:
            slash.update()
            slash.speed = 9
            slash.draw(game_window)

            if slash.x > 1080 or slash.x < -100:
                projectiles.remove(slash)

            if slash.mask.overlap(boss.hitbox, (boss.x - slash.x, boss.y - slash.y)) and boss.state not in ("flyidle", "fly", "fly2"):
                bosshealthbar.hp -= 0.49
                projectiles.remove(slash)

        #CHECKING IF BOSS IS DEAD AND CALCULATING TIME TAKEN TO BEAT THE GAME
        if bosshealthbar.hp <=0:
            projectiles.clear()
            end_time = time.time() - state.start_time 
            mins = int(end_time // 60) 
            secs = int(end_time % 60) 
            total_time = ui.font6.render(f"Your Time Was {mins} mins {secs} secs", True, (199, 6, 38))
            end_time = time.time() - state.start_time
            state.game_state = "Win Screen"

        player.draw(game_window)
        
        fps.tick(60)
        pygame.display.update()


    #QUIT GAME

    if state.game_state == "Quit":
        state.game_running = False



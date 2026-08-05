import pygame
pygame.init()
game_window = pygame.display.set_mode((1080, 720))

###################################################################################### MAIN MENU ###############################################################################################

background = pygame.image.load("GameAssets/Menu/menu_bg.jpg").convert_alpha()
background = pygame.transform.scale(background, (1080, 720))

###################################################################################### SETTINGS ##################################################################################################

mute = pygame.image.load("GameAssets/Menu/music_muted.png").convert_alpha()
mute = pygame.transform.scale(mute,(64,64))
mute_button = mute.get_rect(topleft=(3,650))

settings_bg = pygame.image.load("GameAssets/Settings/settings_bg.jpg").convert_alpha()
settings_bg = pygame.transform.scale(settings_bg, (1080,720))

###################################################################################### LOBBY #################################################################################################

#Lobby Assets
lobby_ground = pygame.image.load("GameAssets/Lobby/lobby_ground.png").convert_alpha()
castle_img = pygame.image.load("GameAssets/Lobby/castle.png").convert_alpha()
castle = pygame.transform.scale(castle_img, (480, 270))
nightsky = pygame.image.load("GameAssets/Lobby/lobby_sky.png",).convert_alpha()
nightsky = pygame.transform.scale(nightsky, (1080,720))
sign = pygame.image.load("GameAssets/Lobby/sign.png").convert_alpha()
sign = pygame.transform.scale(sign, (64, 64))

#Player Assets
player_img = pygame.image.load("GameAssets/PlayerSprite/idle1.png").convert_alpha()
player = pygame.transform.scale(player_img, (64, 64))
player_l = pygame.transform.flip(player, True, False)


#Light Attack
player_atk1 = pygame.image.load("GameAssets/PlayerSprite/light_atk1.png").convert_alpha()
player_atk1 = pygame.transform.scale(player_atk1, (64,64))
player_atk2 = pygame.image.load("GameAssets/PlayerSprite/light_atk2.png").convert_alpha()
player_atk2 = pygame.transform.scale(player_atk2, (64,64))
player_atk3 = pygame.image.load("GameAssets/PlayerSprite/light_atk3.png").convert_alpha()
player_atk3 = pygame.transform.scale(player_atk3, (64,64))

player_atk1_l = pygame.transform.flip(player_atk1, True, False)
player_atk2_l = pygame.transform.flip(player_atk2, True, False)
player_atk3_l = pygame.transform.flip(player_atk3, True, False)

#Dash
player_dash1 = pygame.image.load("GameAssets/PlayerSprite/dash1.png").convert_alpha()
player_dash1 = pygame.transform.scale(player_dash1, (64,64))
player_dash2 = pygame.image.load("GameAssets/PlayerSprite/dash2.png").convert_alpha()
player_dash2 = pygame.transform.scale(player_dash2, (64,64))
player_dash3 = pygame.image.load("GameAssets/PlayerSprite/dash3.png").convert_alpha()
player_dash3= pygame.transform.scale(player_dash3, (64,64))

player_dash4 = pygame.image.load("GameAssets/PlayerSprite/dash4.png").convert_alpha()
player_dash4= pygame.transform.scale(player_dash4, (64,64))
player_dash5 = pygame.image.load("GameAssets/PlayerSprite/dash5.png").convert_alpha()
player_dash5= pygame.transform.scale(player_dash5, (64,64))
player_dash6 = pygame.image.load("GameAssets/PlayerSprite/dash6.png").convert_alpha()
player_dash6= pygame.transform.scale(player_dash6, (64,64))

player_dash1_l=pygame.transform.flip(player_dash1, True, False),
player_dash2_l=pygame.transform.flip(player_dash2, True, False),
player_dash3_l=pygame.transform.flip(player_dash3, True, False)

#Slash Attack
player_slash_r1 = pygame.image.load("GameAssets/PlayerSprite/slash_projectile1.png").convert_alpha()
player_slash_r1 = pygame.transform.scale(player_slash_r1, (150,150))

player_slash_r2 = pygame.image.load("GameAssets/PlayerSprite/slash_projectile2.png").convert_alpha()
player_slash_r2 = pygame.transform.scale(player_slash_r2, (150,150))

player_slash_r3 = pygame.image.load("GameAssets/PlayerSprite/slash_projectile3.png").convert_alpha()
player_slash_r3 = pygame.transform.scale(player_slash_r3, (150,150))

player_slash_r4 = pygame.image.load("GameAssets/PlayerSprite/slash_projectile4.png").convert_alpha()
player_slash_r4 = pygame.transform.scale(player_slash_r4, (150,150))

player_slash_l1 = pygame.transform.flip(player_slash_r1, True, False)
player_slash_l2 = pygame.transform.flip(player_slash_r2, True, False)
player_slash_l3 = pygame.transform.flip(player_slash_r3, True, False)
player_slash_l4 = pygame.transform.flip(player_slash_r4, True, False)

player_slash2 = pygame.image.load("GameAssets/PlayerSprite/slash_atk1.png").convert_alpha()
player_slash2 = pygame.transform.scale(player_slash2, (64,64))
player_slash3 = pygame.image.load("GameAssets/PlayerSprite/slash_atk2.png").convert_alpha()
player_slash3 = pygame.transform.scale(player_slash3, (64,64))

player_slash2_l = pygame.transform.flip(player_slash2, True, False)
player_slash3_l = pygame.transform.flip(player_slash3, True, False)

#Running
player_run_r1 = pygame.image.load("GameAssets/PlayerSprite/run1.png").convert_alpha()
player_run_r1 = pygame.transform.scale(player_run_r1, (64,64))
player_run_r2 = pygame.image.load("GameAssets/PlayerSprite/run2.png").convert_alpha()
player_run_r2 = pygame.transform.scale(player_run_r2, (64,64))
player_run_r3 = pygame.image.load("GameAssets/PlayerSprite/run3.png").convert_alpha()
player_run_r3 = pygame.transform.scale(player_run_r3, (64,64))
player_idle_l = pygame.transform.flip(player, True, False)

player_run_l1 = pygame.transform.flip(player_run_r1, True, False)
player_run_l2 = pygame.transform.flip(player_run_r2, True, False)
player_run_l3 = pygame.transform.flip(player_run_r3, True, False)

#Jumping 
player_jump_r = pygame.image.load("GameAssets/PlayerSprite/jump1.png").convert_alpha()
player_jump_r = pygame.transform.scale(player_jump_r, (64,64))
player_jump_l = pygame.transform.flip(player_jump_r, True, False)

#Healthbar
playerhealthbar_img = pygame.image.load("GameAssets/PlayerSprite/player_healthbar.png").convert_alpha()

###################################################################################### LEVEL 1 ###############################################################################################

#Level 1 Assets
level1_pillars = pygame.image.load("GameAssets/Level1/pillars.png").convert_alpha()
level1_pillars = pygame.transform.scale(level1_pillars, (1080, 720))
level1_bg = pygame.image.load("GameAssets/Level1/room.png").convert_alpha()
level1_bg = pygame.transform.scale(level1_bg, (1080, 720))
door1 = pygame.image.load("GameAssets/Level1/door_close.png").convert_alpha()
door2 = pygame.image.load("GameAssets/Level1/door_open.png").convert_alpha()

#Enemy Drops
healthpack = pygame.image.load("GameAssets/Level1/hearts.png").convert_alpha()
healthpack = pygame.transform.scale(healthpack,(30,30))

#Enemy Assets
enemy = pygame.image.load("GameAssets/EnemySprite/idle1.png").convert_alpha()
enemy = pygame.transform.scale(enemy,(100,100))

#Summon
summon1 = pygame.image.load("GameAssets/EnemySprite/summon1.png").convert_alpha()
summon1 = pygame.transform.scale(summon1,(100,100))
summon2 = pygame.image.load("GameAssets/EnemySprite/summon2.png").convert_alpha()
summon2 = pygame.transform.scale(summon2,(100,100))

#Running
enemy_run1 = pygame.image.load("GameAssets/EnemySprite/run1.png").convert_alpha()
enemy_run1 = pygame.transform.scale(enemy_run1,(100,100))
enemy_run2 = pygame.image.load("GameAssets/EnemySprite/run2.png").convert_alpha()
enemy_run2 = pygame.transform.scale(enemy_run2,(100,100))

#Attacks
enemy_atk1 = pygame.image.load("GameAssets/EnemySprite/atk1.png").convert_alpha()
enemy_atk1 = pygame.transform.scale(enemy_atk1,(100,100))
enemy_atk2 = pygame.image.load("GameAssets/EnemySprite/atk2.png").convert_alpha()
enemy_atk2 = pygame.transform.scale(enemy_atk2,(100,100))

#Enemy Death Indicator
eye1 = pygame.image.load("GameAssets/Level1/eye1.png").convert_alpha()
eye1 = pygame.transform.scale(eye1,(65.33,143.67))
eye2 = pygame.image.load("GameAssets/Level1/eye2.png").convert_alpha()
eye2 = pygame.transform.scale(eye2,(65.33,143.67))
eye3 = pygame.image.load("GameAssets/Level1/eye3.png").convert_alpha()
eye3 = pygame.transform.scale(eye3,(65.33,143.67))
eye4 = pygame.image.load("GameAssets/Level1/eye4.png").convert_alpha()
eye4 = pygame.transform.scale(eye4,(65.33,143.67))
eye5 = pygame.image.load("GameAssets/Level1/eye5.png").convert_alpha()
eye5 = pygame.transform.scale(eye5,(65.33,143.67))
eye6 = pygame.image.load("GameAssets/Level1/eye6.png").convert_alpha()
eye6 = pygame.transform.scale(eye6,(65.33,143.67))

###################################################################################### LEVEL 2 ###############################################################################################

#Level 2 Assets
level2_bg = pygame.image.load("GameAssets/Level2/level2_bg.jpg").convert_alpha()
level2_bg = pygame.transform.scale(level2_bg, (1080, 720))

#Symbols
rect_na = pygame.image.load("GameAssets/Level2/rect1.png").convert_alpha()
rect_na = pygame.transform.scale(rect_na,(42,42))
rect_a = pygame.image.load("GameAssets/Level2/rect2.png").convert_alpha()
rect_a = pygame.transform.scale(rect_a,(42,42))

circ_na = pygame.image.load("GameAssets/Level2/circle1.png").convert_alpha()
circ_na = pygame.transform.scale(circ_na,(42,42))
circ_a = pygame.image.load("GameAssets/Level2/circle2.png").convert_alpha()
circ_a = pygame.transform.scale(circ_a,(42,42))

per_na = pygame.image.load("GameAssets/Level2/per1.png").convert_alpha()
per_na = pygame.transform.scale(per_na,(42,42))
per_a = pygame.image.load("GameAssets/Level2/per2.png").convert_alpha()
per_a = pygame.transform.scale(per_a,(42,42))

#Boss Gate
boss_gate1 = pygame.image.load("GameAssets/Level2/door1.png").convert_alpha()
boss_gate1 = pygame.transform.scale(boss_gate1,(115.5,148.5))
boss_gate2 = pygame.image.load("GameAssets/Level2/door2.png").convert_alpha()
boss_gate2 = pygame.transform.scale(boss_gate2,(115.5,148.5))
boss_gate3 = pygame.image.load("GameAssets/Level2/door3.png").convert_alpha()
boss_gate3 = pygame.transform.scale(boss_gate3,(115.5,148.5))
boss_gate4 = pygame.image.load("GameAssets/Level2/door4.png").convert_alpha()
boss_gate4 = pygame.transform.scale(boss_gate4,(115.5,148.5))
boss_gate5 = pygame.image.load("GameAssets/Level2/door5.png").convert_alpha()
boss_gate5 = pygame.transform.scale(boss_gate5,(115.5,148.5))
boss_gate6 = pygame.image.load("GameAssets/Level2/door6.png").convert_alpha()
boss_gate6 = pygame.transform.scale(boss_gate6,(115.5,148.5))

#Platform
platform1 = pygame.image.load("GameAssets/Level2/platform.png").convert_alpha()
platform1 = pygame.transform.scale(platform1,(68,16))
platform2 = pygame.image.load("GameAssets/Level2/platform.png").convert_alpha()
platform2 = pygame.transform.scale(platform2,(68,16))
platform3 = pygame.image.load("GameAssets/Level2/platform.png").convert_alpha()
platform3 = pygame.transform.scale(platform3,(68,16))
platform4 = pygame.image.load("GameAssets/Level2/platform.png").convert_alpha()
platform4 = pygame.transform.scale(platform4,(68,16))

###################################################################################### BOSS LEVEL #############################################################################################

#Healthbar
bosshealthbar_img = pygame.image.load("GameAssets/BossSprite/boss_healthbar.png").convert_alpha()
animation_fix = pygame.image.load("GameAssets/BossSprite/fist_tp.png").convert_alpha()
animation_fix = pygame.transform.scale(animation_fix,(300,220))

#Boss Assets
boss_bg = pygame.image.load("GameAssets/BossLevel/boss_bg.png").convert_alpha()
boss_bg = pygame.transform.scale(boss_bg, (1080,840))

#Idle
boss_idle1 = pygame.image.load("GameAssets/BossSprite/idle1.png").convert_alpha()
boss_idle1 = pygame.transform.scale(boss_idle1,(360,198))
boss_idle1_r = pygame.transform.flip(boss_idle1, True, False)

boss_idle2 = pygame.image.load("GameAssets/BossSprite/idle2.png").convert_alpha()
boss_idle2 = pygame.transform.scale(boss_idle2,(360,198))
boss_idle2_r = pygame.transform.flip(boss_idle2, True, False)

boss_idle3 = pygame.image.load("GameAssets/BossSprite/idle3.png").convert_alpha()
boss_idle3 = pygame.transform.scale(boss_idle3,(360,198))
boss_idle3_r = pygame.transform.flip(boss_idle3, True, False)

boss_idle4 = pygame.image.load("GameAssets/BossSprite/idle4.png").convert_alpha()
boss_idle4 = pygame.transform.scale(boss_idle4,(360,198))
boss_idle4_r = pygame.transform.flip(boss_idle4, True, False)

boss_idle5 = pygame.image.load("GameAssets/BossSprite/idle5.png").convert_alpha()
boss_idle5 = pygame.transform.scale(boss_idle5,(360,198))
boss_idle5_r = pygame.transform.flip(boss_idle5, True, False)

#Light Attack

boss_light1 = pygame.image.load("GameAssets/BossSprite/light1.png").convert_alpha()
boss_light1 = pygame.transform.scale(boss_light1,(360,168))
boss_light1_r = pygame.transform.flip(boss_light1, True, False)

boss_light2 = pygame.image.load("GameAssets/BossSprite/light2.png").convert_alpha()
boss_light2 = pygame.transform.scale(boss_light2,(360,168))
boss_light2_r = pygame.transform.flip(boss_light2, True, False)

boss_light3 = pygame.image.load("GameAssets/BossSprite/light3.png").convert_alpha()
boss_light3 = pygame.transform.scale(boss_light3,(360,168))
boss_light3_r = pygame.transform.flip(boss_light3, True, False)

boss_light4 = pygame.image.load("GameAssets/BossSprite/light4.png").convert_alpha()
boss_light4 = pygame.transform.scale(boss_light4,(360,168))
boss_light4_r = pygame.transform.flip(boss_light4, True, False)

boss_light5 = pygame.image.load("GameAssets/BossSprite/light5.png").convert_alpha()
boss_light5 = pygame.transform.scale(boss_light5,(360,168))
boss_light5_r = pygame.transform.flip(boss_light5, True, False)

#Barrage Attack

boss_barrage1 = pygame.image.load("GameAssets/BossSprite/barrage1.png").convert_alpha()
boss_barrage1 = pygame.transform.scale(boss_barrage1,(360,168))
boss_barrage1_r = pygame.transform.flip(boss_barrage1, True, False)

boss_barrage2 = pygame.image.load("GameAssets/BossSprite/barrage2.png").convert_alpha()
boss_barrage2 = pygame.transform.scale(boss_barrage2,(360,168))
boss_barrage2_r = pygame.transform.flip(boss_barrage2, True, False)

boss_barrage3 = pygame.image.load("GameAssets/BossSprite/barrage3.png").convert_alpha()
boss_barrage3 = pygame.transform.scale(boss_barrage3,(360,168))
boss_barrage3_r = pygame.transform.flip(boss_barrage3, True, False)

boss_barrage4 = pygame.image.load("GameAssets/BossSprite/barrage4.png").convert_alpha()
boss_barrage4 = pygame.transform.scale(boss_barrage4,(360,168))
boss_barrage4_r = pygame.transform.flip(boss_barrage4, True, False)

boss_barrage5 = pygame.image.load("GameAssets/BossSprite/barrage5.png").convert_alpha()
boss_barrage5 = pygame.transform.scale(boss_barrage5,(360,168))
boss_barrage5_r = pygame.transform.flip(boss_barrage5, True, False)

#Flying

boss_fly1 = pygame.image.load("GameAssets/BossSprite/fly1.png").convert_alpha()
boss_fly1 = pygame.transform.scale(boss_fly1,(300,220))

boss_fly2 = pygame.image.load("GameAssets/BossSprite/fly2.png").convert_alpha()
boss_fly2 = pygame.transform.scale(boss_fly2,(300,220))
boss_fly3 = pygame.image.load("GameAssets/BossSprite/fly3.png").convert_alpha()
boss_fly3 = pygame.transform.scale(boss_fly3,(300,220))
boss_fly4 = pygame.image.load("GameAssets/BossSprite/fly4.png").convert_alpha()
boss_fly4 = pygame.transform.scale(boss_fly4,(300,220))
boss_fly5 = pygame.image.load("GameAssets/BossSprite/fly5.png").convert_alpha()
boss_fly5 = pygame.transform.scale(boss_fly5,(300,220))
boss_fly6 = pygame.image.load("GameAssets/BossSprite/fly6.png").convert_alpha()
boss_fly6 = pygame.transform.scale(boss_fly6,(300,220))

boss_fly7 = pygame.image.load("GameAssets/BossSprite/fly7.png").convert_alpha()
boss_fly7 = pygame.transform.scale(boss_fly7,(300,220))
boss_fly8 = pygame.image.load("GameAssets/BossSprite/fly8.png").convert_alpha()
boss_fly8 = pygame.transform.scale(boss_fly8,(300,220))
boss_fly9 = pygame.image.load("GameAssets/BossSprite/fly9.png").convert_alpha()
boss_fly9 = pygame.transform.scale(boss_fly9,(300,220))
boss_fly10 = pygame.image.load("GameAssets/BossSprite/fly10.png").convert_alpha()
boss_fly10 = pygame.transform.scale(boss_fly10,(300,220))

#Punch
boss_punch1 = pygame.image.load("GameAssets/BossSprite/fist1.png").convert_alpha()
boss_punch1 = pygame.transform.scale(boss_punch1,(300,320))
boss_punch2 = pygame.image.load("GameAssets/BossSprite/fist2.png").convert_alpha()
boss_punch2 = pygame.transform.scale(boss_punch2,(300,320))
boss_punch3 = pygame.image.load("GameAssets/BossSprite/fist3.png").convert_alpha()
boss_punch3 = pygame.transform.scale(boss_punch3,(300,320))

###################################################################################### WIN SCREEN ###############################################################################################

win_bg = pygame.image.load("GameAssets/WinScreen/win_bg.png").convert_alpha()
win_bg = pygame.transform.scale(win_bg, (1080,720))


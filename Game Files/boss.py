import pygame, random, math

import assets
from player import Player

#Boss Class: Handles boss movement, attacks, properties and animations.
class Boss():
    def __init__(boss, x, y, assets): #Initializes boss position, assets, states and properties.
        boss.x = x
        boss.y = y
        boss.assets = assets
    
        #State Variables
        boss.dir = "left" #Current direction boss is facing
        boss.state = "idle" #Current action performed by the boss
        boss.dead = False
        boss.special_move_activated = False #Checks if the boss uses special move
        boss.ground_y = 425
        
        #Movement Speeds
        boss.idle_speed = 1
        boss.fly_speed = 3

        #Attack Damages
        boss.light_atk_dmg = 0.05
        boss.barrage_atk_dmg = 0.18

        #Animation Variables
        boss.frame = 0
        boss.anim_speed = 0.5

        #Animation dictionary that maps boss states and directions to the list
        boss.animation_state = { "idle_left": [assets.boss_idle1, assets.boss_idle2, assets.boss_idle3, assets.boss_idle4, assets.boss_idle5],
                                 "idle_right": [assets.boss_idle1_r, assets.boss_idle2_r, assets.boss_idle3_r, assets.boss_idle4_r, assets.boss_idle5_r],
                                 
                                 "light_left": [assets.boss_light1, assets.boss_light2, assets.boss_light3, assets.boss_light4, assets.boss_light5],
                                 "light_right": [assets.boss_light1_r, assets.boss_light2_r, assets.boss_light3_r, assets.boss_light4_r, assets.boss_light5_r],
                                 
                                 "barrage_left": [assets.boss_barrage1, assets.boss_barrage2, assets.boss_barrage3, assets.boss_barrage4, assets.boss_barrage5],
                                 "barrage_right": [assets.boss_barrage1_r, assets.boss_barrage2_r, assets.boss_barrage3_r, assets.boss_barrage4_r, assets.boss_barrage5_r],
                               
                                 "flyidle_left": [assets.boss_fly1],
                                 "flyidle_right": [assets.boss_fly1],

                                 "fly_left": [assets.boss_fly2, assets.boss_fly3, assets.boss_fly4, assets.boss_fly5, assets.boss_fly6],
                                 "fly_right": [assets.boss_fly2, assets.boss_fly3, assets.boss_fly4, assets.boss_fly5, assets.boss_fly6],

                                 "fly2_left": [assets.boss_fly7, assets.boss_fly8, assets.boss_fly9, assets.boss_fly10, assets.boss_fly9],             
                                 "fly2_right": [assets.boss_fly7, assets.boss_fly8, assets.boss_fly9, assets.boss_fly10, assets.boss_fly9],

                                   }
        
        #Sets boss image, hitbox and rect for collision handling
        boss.image = boss.animation_state["idle_left"][0]
        boss.rect = boss.image.get_rect(topleft = (boss.x, boss.y))
        boss.hitbox = pygame.mask.from_surface(boss.image)

    #Handles boss animations and effects each state has on the player and boss
    def sprite_animation(boss, player, playerhealthbar, punch):

        #Determines current animation based on the boss's state and direction and updates each frame
        boss_anim = f"{boss.state}_{boss.dir}"
        anim_frames = boss.animation_state[boss_anim]
        boss.frame += boss.anim_speed

        #Loops animation when all frames in the list have been played
        if boss.frame >= len(anim_frames):
            boss.frame = 0  

            if boss.state == "fly":
                boss.anim_speed = 0.08
                boss.state = "fly2"   
        
        #Handles effects and state changes for each boss state
        if boss.state == "light":
            boss.ground_y = 455
            boss.anim_speed = 0.15
            playerhealthbar.hp -= boss.light_atk_dmg
            if not boss.rect.colliderect(player.rect):
                boss.state = "idle"
        
        elif boss.state == "fly2":
            if boss.y != 413:
                boss.y += boss.fly_speed
            if boss.y == 413:
                if punch.state == "deactivated":
                    punch.x = player.x-115
                    punch.state = "activated"

        elif boss.state == "barrage":
            boss.ground_y = 455
            boss.anim_speed = 0.3
            playerhealthbar.hp -= boss.barrage_atk_dmg
            if not boss.rect.colliderect(player.rect):
                boss.state = "idle"

        elif boss.state == "idle":
            boss.ground_y = 425
            boss.anim_speed = 0.1
            if boss.dir == "right":
                boss.x += boss.idle_speed
            else:
                boss.x -= boss.idle_speed
        
        elif boss.state == "flyidle":
            if 410 <= boss.x <= 413:
                boss.y -= boss.fly_speed
                boss.anim_speed = 0.035
                if boss.y == 11:
                    boss.special_move_activated = True
                    boss.state = "fly"
            elif boss.x > 410:
                boss.x -= boss.fly_speed
            elif boss.x < 413:
                boss.x += boss.fly_speed
            
        #Updates boss image and hitbox for collision handling
        boss.image = anim_frames[int(boss.frame)]
        boss.hitbox = pygame.mask.from_surface(boss.image)

   
    def boss_states(boss, player, playerhealthbar, bosshealthbar, punch): #Handles boss behavior/AI

        if bosshealthbar.hp <= 25 and not boss.special_move_activated:
            boss.state = "flyidle"
            
        #Determines when boss dies
        if bosshealthbar.hp <0:
            boss.dead = True

        elif boss.rect.colliderect(player.rect) and boss.state not in ("flyidle", "fly", "fly2"):
            if bosshealthbar.hp >= 75: 
             boss.state = "light"

            elif 25 <bosshealthbar.hp < 75:
             boss.state = "barrage"

            elif bosshealthbar.hp <= 25:
                boss.state = "light"
         
        elif not boss.rect.colliderect(player.rect) and boss.state not in ("flyidle", "fly", "fly2"):

            if boss.x < player.x:
             boss.dir = "right" 
            else:
                boss.dir = "left"
            
            boss.state = "idle"
        
        #Handles damage done to boss when player uses light attack on it
        if player.state == "light" and player.hitbox.overlap(boss.hitbox, (boss.x-player.x,boss.y-player.y)) and boss.state not in ("flyidle", "fly", "fly2"):
                bosshealthbar.hp -= 0.15
        
        #Ensures boss does not "float" when performing certain attacks
        if boss.y != boss.ground_y and boss.state in ("idle", "light", "barrage"):
            boss.y = boss.ground_y

        #Updates animation and position of the boss
        boss.sprite_animation(player, playerhealthbar, punch)
        boss.rect.topleft = (boss.x, boss.y) 

    
    def draw(boss, surface):#Handles rendering of the boss on the screen
        if not boss.dead:
            surface.blit(boss.image, boss.rect)

#Boss Punch Class: Handles the boss's special attack/punch attack, properties and animations.
class BossPunch():
    def __init__(punch, assets): #Initializes boss position, assets, states and properties.
        punch.x = 0
        punch.y = 300
        punch.assets = assets
        
        #Boss punch states, properties and animation variables
        punch.state = "deactivated"
        punch.frame = 0
        punch.anim_speed = 0.06
        punch.dmg = 0.5

        #Animation dictionary that maps punch states to the list
        punch.punch_set = { "activated": [assets.animation_fix,assets.boss_punch1, assets.boss_punch3, assets.boss_punch2],
                            "deactivated": [assets.animation_fix]
                          }
        
        #Sets punch image and rect for collision handling
        punch.image = punch.punch_set["deactivated"][0]
        punch.rect = punch.image.get_rect(topleft = (punch.x, punch.y))

    #Handles punch animation and collision damage to the player and boss
    def sprite_animation(punch, boss, playerhealthbar, player, bosshealthbar):
        if punch.state == "activated":
            anim_frames = punch.punch_set["activated"]
            punch.frame += punch.anim_speed
            
            #Damages player on contact
            if punch.rect.colliderect(player.rect):
                playerhealthbar.hp -= punch.dmg

            #Loops punch animation and resets punch and boss states after move is done
            if punch.frame >= len(anim_frames):
                punch.frame = 0  
                bosshealthbar.hp -= 0.1
                boss.state = "idle"
                punch.state = "deactivated"
        else:
            anim_frames = punch.punch_set["deactivated"] 
            punch.frame = 0

        #Updates boss image and hitbox for collision handling
        punch.image = anim_frames[int(punch.frame)]
        punch.rect = punch.image.get_rect(topleft=(punch.x, punch.y))

    #Handles rendering of the punch on the screen
    def draw(punch, surface):
        if punch.state == "activated":
            surface.blit(punch.image, (punch.x, punch.y))
        else:
            pass

#Boss Health Bar Class: Handles boss health bar properties and rendering.
class BossHealthBar():
    
    def __init__(healthbar, x, y, w, h, full_hp): #Initialzes health bar dimensions and hp values
        healthbar.x = x 
        healthbar.y = y
        healthbar.w = w
        healthbar.h = h
        healthbar.hp = full_hp
        healthbar.full_hp = full_hp
    def draw(healthbar, surface): #Handles rendering of the health bar on the screen
        ratio = healthbar.hp/healthbar.full_hp
        pygame.draw.rect(surface, (177, 18, 38), (healthbar.x, healthbar.y, healthbar.w, healthbar.h))
        pygame.draw.rect(surface, (110, 235, 131), (healthbar.x, healthbar.y, healthbar.w*ratio, healthbar.h))
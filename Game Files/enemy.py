import pygame, random, math

import assets
from player import Player, PlayerHealthBar

#Enemy Class: Hnandles Enemy's movement, animation, and states.
class Enemy():
    def __init__(enemy, assets): #Initializes enemy position, assets, states and properties.
        enemy.x = random.randint(0, 1070)
        enemy.y = 555
        enemy.assets = assets

        #State Variables
        enemy.dir = "left" #Current direction enemy is facing
        enemy.state = "summon" #Current action performed by the enemy
        enemy.dead = False
        enemy.count = 0
        
        #Animation Variables
        enemy.frame = 0
        enemy.anim_speed = 0.1

        #Enemy Movement and Attack Properties
        enemy.run_speed = 2
        enemy.atk_dmg = 0.05
        enemy.max_spawns = 5


        #Enemy Indicator (Eye) Properties
        enemy.eye_set = [assets.eye2, assets.eye3, assets.eye4, assets.eye5, assets.eye6] 
        enemy.eye_frame = 0 
        enemy.eye_state = assets.eye1

        #Animation dictionary that maps enemy states and directions to the list
        enemy.animation_state = { "summon_left": [assets.summon1,assets.summon2],
                                 "summon_right": [assets.summon1,assets.summon2],
                                 
                                 "idle_left": [assets.enemy],
                                 "idle_right": [pygame.transform.flip(assets.enemy, True, False)],
                                 
                                 "run_left": [assets.enemy_run1, assets.enemy_run2],
                                 "run_right": [pygame.transform.flip(assets.enemy_run1, True, False), pygame.transform.flip(assets.enemy_run2, True, False)],
                                 
                                 "attk_left": [assets.enemy_atk1, assets.enemy_atk2],
                                 "attk_right": [pygame.transform.flip(assets.enemy_atk1, True, False), pygame.transform.flip(assets.enemy_atk2, True, False)] }
        
        #Sets enemy image and rect for collision handling
        enemy.image = enemy.animation_state["summon_left"][0]
        enemy.rect = enemy.image.get_rect(topleft = (enemy.x, enemy.y))
        
    #Handles enemy animations and effects each state has on the player and enemy
    def sprite_animation(enemy, player, playerhealthbar):

         #Determines current animation based on the enemy's state and direction and updates each frame
        enemy_anim = f"{enemy.state}_{enemy.dir}"
        anim_frames = enemy.animation_state[enemy_anim]
        enemy.frame += enemy.anim_speed

        #Loops animation when all frames in the list have been played and also spawns the enemy
        if enemy.frame >= len(anim_frames):
            enemy.frame = 0        
            if enemy.state == "summon":
                enemy.state = "idle"
                enemy.anim_speed = 0.1
        
        #Handles effects of each state on the player and enemy
        elif enemy.state == "attk":
            if enemy.count < enemy.max_spawns:
                playerhealthbar.hp -= enemy.atk_dmg
                
            if not enemy.rect.colliderect(player.rect):
                enemy.state = "run"
        
        elif enemy.state == "run":
            if enemy.dir == "right":
                enemy.x += enemy.run_speed
            else:
                enemy.x -= enemy.run_speed
        
        #Updates enemy image and hitbox for collision handling
        enemy.image = anim_frames[int(enemy.frame)]
        enemy.hitbox = pygame.mask.from_surface(enemy.image)
    
    #Handles enemy behavior/AI
    def enemy_states(enemy, player, playerhealthbar,enemyhealthbar):

        if enemy.count < 5 and enemy.state == "summon":
            enemy.anim_speed = 0.02

        if not enemy.rect.colliderect(player.rect) and enemy.state in ("run", "idle"):
    
            if enemy.x < player.x:
             enemy.dir = "right"
           
            else:
                enemy.dir = "left"
            
            enemy.state = "run"

        elif enemy.rect.colliderect(player.rect) and enemy.state in ("idle", "run"):
            enemy.state = "attk"
        
        #Handles damage done to the enemy when the player uses light attack
        if player.rect.colliderect(enemy.rect) and enemy.state != "summon":
            if player.state == "light" and player.dir != enemy.dir:
                enemyhealthbar.hp -= 0.5
        
        #Updates animation and position of the enemy
        enemy.sprite_animation(player, playerhealthbar)
        enemy.rect.topleft = (enemy.x, enemy.y)
    
    #Handles the enemy eye indicator
    def enemies_indicator(enemy):
        if enemy.dead and enemy.eye_frame < 5:
            
            #Updates eye frame to show the enemy is dead and will soon respawn (or not)
            enemy.eye_state = enemy.eye_set[enemy.eye_frame]
            enemy.eye_frame = enemy.eye_frame +1 
            
            #Key Requirement for enemy respawn logic
            if enemy.count < enemy.max_spawns:
                enemy.dead = False
            
    #Handles rendering of the enemy on the screen
    def draw(enemy, surface):
        if not enemy.dead:
            surface.blit(enemy.image, enemy.rect)

#Enemy Health Bar Class: Handles enemy health bar properties and rendering along with creation of enemy drops
class EnemyHealthBar():
    def __init__(healthbar, x, y, w, h, full_hp): #Initialzes health bar dimensions and hp values
        healthbar.x = x 
        healthbar.y = y
        healthbar.w = w
        healthbar.h = h
        healthbar.hp = full_hp
        healthbar.full_hp = full_hp
        
    
    def draw(healthbar, surface, enemy, drops): #Handles rendering of the health bar on the screen and creation of healthpacks
        ratio = healthbar.hp/healthbar.full_hp
        pygame.draw.rect(surface, (177, 18, 38), (healthbar.x, healthbar.y, healthbar.w, healthbar.h))
        pygame.draw.rect(surface, (110, 235, 131), (healthbar.x, healthbar.y, healthbar.w*ratio, healthbar.h))
        
        if ratio <= 0:
            enemy.dead = True
            enemy.anim_speed = 0.02

            #Creates a health pack with a 1 in 4 chance of dropping
            drops_chance = random.randint(1,4)
            if drops_chance == 4:
                drop_healthpack = EnemyDrops(enemy.x+50, 620, assets.healthpack)
                drops.append(drop_healthpack)

            #Respawning new enemy after death
            enemy.count = enemy.count + 1
            enemy.state = "summon"
            healthbar.hp = 100
            enemy.x = random.randint(0, 1070)

#Enemy Drops Class: Handles properties and rendering of drops that drop when the enemy dies
class EnemyDrops:
    def __init__(drops, x, y, image): #Initializes drop position and image
        drops.x = x
        drops.y = y
        drops.image = image
        drops.rect = drops.image.get_rect(topleft=(drops.x, drops.y))
    
    def update(drops): #Creates a rectangle of the drop for collision handling
        drops.rect.topleft = (drops.x, drops.y)

    def draw(drops, surface): #Handles rendering of the drop on the screen
        surface.blit(drops.image, drops.rect)

                                    






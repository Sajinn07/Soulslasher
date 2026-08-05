import pygame, random, math

import assets
from game_states import States

#Player Class: Handles player properties, movement, attacks, and animations.
class Player():
    def __init__(player, x, y, assets):  #Initializes player position, assets, states and properties.
        player.x = x
        player.y = y
        player.assets = assets
        player.grav = 0 #The gravity that affects the player
        
        player.move_speed = 7 #Speed at which the player moves
        
        #Jump Variables
        player.on_ground = False
        player.jump_count = 0
        player.max_jumps = 2

        #State Variables
        player.dir = "right" #Current direction player is facing
        player.state = "idle" #Current action performed by the player

        #Animation Variables
        player.frame = 0
        player.anim_speed = 0.2

        #Dash Variables
        player.dashes = 0
        player.dash_speed = 15
        player.max_dash_frames = 3
        
        player.ground_y = 560 #The y cordinate of the ground level for the player

        #Animation dictionary that maps player states and directions to the list
        player.animation_state = { "idle_right": [assets.player],
                                   "idle_left": [assets.player_l],

                                   "run_right": [assets.player_run_r1, assets.player_run_r2, assets.player_run_r3],
                                   "run_left": [assets.player_run_l1, assets.player_run_l2, assets.player_run_l3],

                                   "jump_right": [assets.player_jump_r],
                                   "jump_left": [assets.player_jump_l],

                                   "light_right": [assets.player_atk1, assets.player_atk3, assets.player_atk2], 
                                   "light_left": [assets.player_atk1_l, assets.player_atk3_l, assets.player_atk2_l],

                                   "slash_right": [assets.player_slash2,assets.player_slash3],
                                   "slash_left": [assets.player_slash2_l,assets.player_slash3_l],

                                   "dash_right": [assets.player_dash2],
                                   "dash_left": [pygame.transform.flip(assets.player_dash2, True, False)] }
        
        #Sets player image, hitbox and rect for collision handling
        player.image = player.animation_state["idle_right"][0]
        player.rect = player.image.get_rect(topleft = (player.x, player.y))
        player.hitbox = pygame.mask.from_surface(player.image)
    
    #Handles the player movement and state changes based on user input
    def movement(player, left, right):
        if player.state in ("light", "slash", "dash"):
            return #Stops movement if the player is performing an attack or dash
        
        #Handles direction and state changes based on user input
        if right:
            player.x += player.move_speed
            player.dir = "right"
            if player.on_ground:
                player.state = "run"
            
        elif left:
            player.x -= player.move_speed
            player.dir = "left"
            if player.on_ground:
                player.state = "run"
        
        else:
            if player.on_ground:
                player.state = "idle"
    
    #Handlles the jumping mechanic of the player
    def jump(player):
        if player.jump_count < player.max_jumps: #Only allows the player to jump a certain number of times
            player.grav = -10 #Applies gravity to player when in air
            player.jump_count += 1
            player.on_ground = False
            player.state = "jump"
    
    #Handles change in state for attacks and dash

    def light_attk(player):
        if player.state not in ("light", "slash", "dash"):
            player.state = "light"
            player.frame = 0
    
    def slash_attk(player):
        if player.state not in ("slash", "dash"):
            player.state = "slash"
            player.frame = 0

    def dash(player):
        if player.state != "dash":
            player.state = "dash"
            player.dashes = 0
            player.frame = 0
    
    #Handles player animations and dash properties
    def sprite_animation(player):

        #Determines current animation based on the player's state and direction and updates each frame
        user_inp = f"{player.state}_{player.dir}"
        anim_frames = player.animation_state[user_inp]
        player.frame += player.anim_speed

        #Loops animation when all frames in the list have been played
        if player.frame >= len(anim_frames):
            player.frame = 0

            if player.state in ("light", "slash"):
                player.state = "idle"
            
            #Handles the dash mechanic and completion of the dash animation
            if player.state in ("dash"):
                player.dashes += 1
                if player.dashes >= player.max_dash_frames:
                    player.state = "idle"
        
        #Updates player image and hitbox for collision handling
        player.image = anim_frames[int(player.frame)]
        player.hitbox = pygame.mask.from_surface(player.image)
    
    #Handles player gravity, movement, and state changes each frame`
    def update(player):
        player.grav += 0.67
        player.y += player.grav #Applies gravity to player each frame when in the air

        #Handles gravity not affecting player when in the ground and resets state
        if player.y >= player.ground_y:
            player.y = player.ground_y
            player.grav = 0
            player.jump_count = 0
            player.on_ground = True
            if player.state in ("jump"):
                player.state = "idle"
        
        #Handles player dash movement based on direction
        if player.state in ("dash"):
            if player.dir == "right":
                player.x += player.dash_speed
            else:
                player.x -= player.dash_speed
        
        #Prevents player from moving off screen (Error Handling)
        if player.x>1025:
            player.x = 1025
        if player.x<-10:
            player.x = -10
        
        #Updates animation and position of the player
        player.sprite_animation()
        player.rect.topleft = (player.x, player.y)
    
    #Handles rendering of the player on the screen
    def draw(player, surface):
        surface.blit(player.image, player.rect)

#Slash Projectile Class: Handles properties, movement, and rendering of the slash projectile created by the player when performing a slash attack
class SlashProjectile():
    def __init__(slash, x, y, image, speed, dir, game_state = None): #Initlizes projectile properties and hitbox for collision handling
        slash.x = x
        slash.y = y
        slash.image = image
        slash.speed = speed #Speed at which the projectile moves
        slash.dir = dir #Direction of the projectile based on the direction of player
        slash.game_state = game_state #Level in which the projectile is used

        #Sets projectile rect and hitbox for collision handling
        slash.rect = slash.image.get_rect(topleft=(slash.x, slash.y))
        slash.mask = pygame.mask.from_surface(slash.image)

    def update(slash): #Handles movement of the projectile and error handling of the projectiles
        
        #Move projectile based on direction
        if slash.dir == "right":
            slash.x += slash.speed
        elif slash.dir == "left":
            slash.x -= slash.speed
        slash.rect.topleft = (slash.x, slash.y)

        #Prevents the projectile from falling off the screen (Error Handling)
        if slash.game_state == "Lobby" or slash.game_state == "BossLevel":
            if slash.y >= 470:
               slash.y = 470
        elif slash.game_state == "Level1":
            if slash.y >= 505:
                slash.y = 505
        elif slash.game_state == "Level2":
            if slash.y >= 500:
                slash.y = 500
        
    #Handles rendering of the projectile on the screen
    def draw(slash, surface):
        surface.blit(slash.image, slash.rect)


#Player Health Bar Class: Handles player health bar properties and rendering.
class PlayerHealthBar():
    def __init__(playerhealthbar, x, y, w, h, full_hp): #Initialzes health bar dimensions and hp values
        playerhealthbar.x = x 
        playerhealthbar.y = y
        playerhealthbar.w = w
        playerhealthbar.h = h
        playerhealthbar.hp = full_hp
        playerhealthbar.full_hp = full_hp
    
    #Handles rendering of the health bar on the screen and checks for player death
    def draw(playerhealthbar, surface, state): 
        ratio = playerhealthbar.hp/playerhealthbar.full_hp

        #Sends user to death screen if player dies (hp is 0 or less)
        if playerhealthbar.hp <= 0:
            state.game_state = "Death Screen"

        pygame.draw.rect(surface, (177, 18, 38), (playerhealthbar.x, playerhealthbar.y, playerhealthbar.w, playerhealthbar.h))
        pygame.draw.rect(surface, (110, 235, 131), (playerhealthbar.x, playerhealthbar.y, playerhealthbar.w*ratio, playerhealthbar.h))
    
    #Handles healing of the player when interacting with a healthpack
    def heal(playerhealthbar, packsize):
        playerhealthbar.hp += packsize
        if playerhealthbar.hp > playerhealthbar.full_hp:
            playerhealthbar.hp = playerhealthbar.full_hp
    
    




                                    






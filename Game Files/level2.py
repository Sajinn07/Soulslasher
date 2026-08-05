import pygame, random, math

import assets

#Platforms Class: Handles movement and rendering of moving platforms in level 2
class Platforms:
    def __init__(platform, x, y, image, speed, dir): #Initializes platform positon, image and properties
        platform.x = x
        platform.y = y
        platform.image = image
        platform.speed = speed #Speed at which the platform moves
        platform.dir = dir #Direction of platform movement
        platform.rect = platform.image.get_rect(topleft=(platform.x, platform.y))

    def update(platform): #Updates platform position based on speed and direction
        if platform.speed > 0:
            if platform.dir == "right":
              platform.x += platform.speed
            elif platform.dir == "left":
               platform.x -= platform.speed

        #Reverses direction if platform reaches the edge of its movement range
        if platform.x >= 1020:
            platform.dir = "left"
        if platform.x <= 0:
            platform.dir = "right"
        platform.rect.topleft = (platform.x, platform.y)

    #Handles rendering of the platform on the screen
    def draw(platform, surface):
        surface.blit(platform.image, platform.rect)
    
class Level2():
    def __init__(level2): #Initializes level 2 properties and assets
        level2.circ_frame = 0
        level2.rect_frame = 0  
        level2.per_frame = 0

        level2.door_frame = 0
        level2.anim_speed = 0.1
        
        #Checks if the symbols have been activated by the player
        level2.circ_state_activated = False
        level2.rect_state_activated = False
        level2.per_state_activated = False
        level2.door_state = "closed"

        #Stores the different states of the symbols and door in a list for aniamtions
        level2.object_state = { "circle": [assets.circ_na, assets.circ_a],
                                 "rectangle": [assets.rect_na, assets.rect_a],
                                 "percentage": [assets.per_na, assets.per_a],

                                  "door": [assets.boss_gate1, assets.boss_gate2,assets.boss_gate3,assets.boss_gate4,assets.boss_gate5,assets.boss_gate6] }
        
        #Assigns the initial images for the symbols and door
        level2.circ_col = assets.circ_a
        level2.rect_col = assets.rect_a
        level2.per_col = assets.per_a

        level2.circ_image = level2.object_state["circle"][0]
        level2.rect_image = level2.object_state["rectangle"][0]
        level2.per_image = level2.object_state["percentage"][0]

        level2.door_image = level2.object_state["door"][0]
        
        #Defines Symbol rectangles for collision detection
        level2.circ_col_rect = level2.circ_image.get_rect(topleft=(955, 450))
        level2.rect_col_rect = level2.rect_image.get_rect(topleft=(82, 320))
        level2.per_col_rect = level2.per_image.get_rect(topleft=(955, 190))

        level2.circ_rect = level2.circ_image.get_rect(topleft=(524, 665))
        level2.rect_rect = level2.rect_image.get_rect(topleft=(440, 665))
        level2.per_rect = level2.per_image.get_rect(topleft=(482, 665))

        level2.door_rect = level2.door_image.get_rect(topleft=(670, 450))

    def update(level2): #Handles logic for symbol activation and opening door
        
        #Opening door animation
        if level2.door_state == "open":
            anim_frames = level2.object_state["door"]
            level2.door_frame += level2.anim_speed
            
            if level2.door_frame >= len(anim_frames):
                level2.door_state = "opened"
                level2.door_frame = 5
                
            level2.door_image = anim_frames[int(level2.door_frame)]

        #Indicates activation of symbol
        if level2.circ_state_activated:
            level2.circ_image = level2.object_state["circle"][1] 

        if level2.rect_state_activated:
            level2.rect_image = level2.object_state["rectangle"][1]       

        if level2.per_state_activated:
            level2.per_image = level2.object_state["percentage"][1]
        
        if level2.rect_state_activated and level2.per_state_activated and level2.circ_state_activated and level2.door_state == "closed":
            level2.door_state = "open"
        
        
        #Updates all rectangles for collision detection
        level2.circ_rect = level2.circ_image.get_rect(topleft=(524, 665))
        level2.rect_rect = level2.rect_image.get_rect(topleft=(440, 665))
        level2.per_rect = level2.per_image.get_rect(topleft=(482, 665))
        level2.door_rect = level2.door_image.get_rect(topleft=(670, 450))

    #Handles rendering of symbols and door on the screen
    def draw(level2, surface):
        surface.blit(level2.circ_col, level2.circ_col_rect)
        surface.blit(level2.rect_col, level2.rect_col_rect)
        surface.blit(level2.per_col, level2.per_col_rect)

        surface.blit(level2.circ_image, level2.circ_rect)
        surface.blit(level2.rect_image, level2.rect_rect)
        surface.blit(level2.per_image, level2.per_rect)

        surface.blit(level2.door_image, level2.door_rect)
        
    










import pygame, random, math
import assets

#States Class: Stores all the states of the game and is used to change the states of the game when needed
class States():
    def __init__(state):
        state.game_running = True
        state.in_level = True
        state.save_created = False
        state.music_state = "Unmuted"
        state.game_state = "Menu"
        state.previous_game_state = None

        state.start_time = None
        state.end_time =  None
        state.total_time = None

    

        

    
    
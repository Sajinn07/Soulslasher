import pygame, random, math

import assets
from game_states import States

#UI Class: Stores all User Interface elements, positions and error handling
class UI():
    def __init__(ui):

        #Fonts
        ui.font = pygame.font.SysFont("arialblack", 40)
        ui.font2 = pygame.font.SysFont("jokerman", 100)
        ui.font3 = pygame.font.SysFont("agencyfb", 20)
        ui.font4 = pygame.font.SysFont("arialrounded",30)
        ui.font5 = pygame.font.SysFont("castellar", 145)
        ui.font6 = pygame.font.SysFont("arialblack", 20)
        ui.font7 = pygame.font.SysFont("arialnova", 20)
        ui.font8 = pygame.font.SysFont("arialrounded",20)
        ui.font9 = pygame.font.SysFont("arialrounded", 15)
        
        #Buttons and texts
        ui.continue_text = ui.font.render("CONTINUE", True, (163, 36, 60))
        ui.continue_button = ui.continue_text.get_rect(topleft=(420, 320))
        
        ui.play_text = ui.font.render("PLAY", True, (163, 36, 60))
        ui.play_button = ui.play_text.get_rect(topleft=(470, 320))

        ui.options_text = ui.font.render("OPTIONS", True, (163, 36, 60))
        ui.options_button = ui.options_text.get_rect(topleft=(430, 390))

        ui.quit_text = ui.font.render("QUIT", True, (163, 36, 60))
        ui.quit_button = ui.quit_text.get_rect(topleft=(470, 460))

        ui.game_name_text = ui.font2.render("SpeedSlasher", True,(10, 15, 31))
        ui.game_name_rect = ui.game_name_text.get_rect(center=(550, 200))

        ui.controls_text = ui.font4.render("CONTROLS", True, (10, 15, 31))
        ui.controls_button = ui.controls_text.get_rect(topleft=(460, 320))

        ui.mainmenu_text = ui.font4.render("RETURN TO MAIN MENU", True, (10, 15, 31))
        ui.mainmenu_button = ui.mainmenu_text.get_rect(topleft=(365, 390))

        ui.backtosettings_text = ui.font4.render("BACK TO SETTINGS", True, (10, 15, 31))
        ui.backtosettings_button = ui.backtosettings_text.get_rect(topleft=(400, 500))

        ui.settings_text = ui.font.render("SETTINGS", True, (10, 15, 31))
        ui.settings_rect = ui.settings_text.get_rect(topleft=(430, 70))

        ui.backtogame_text = ui.font4.render("BACK TO GAME", True, (10, 15, 31))
        ui.backtogame_button = ui.backtogame_text.get_rect(topleft=(435, 250))

        ui.tips_text = ui.font9.render("TIP: Click 'ESC' To Check Controls", True, (255, 204, 0))
        ui.tips_text_rect = ui.tips_text.get_rect(topleft=(500, 55))

        ui.tips2_text = ui.font9.render("TIP: Use Slash Attack to Activate Symbols", True, (255, 204, 0))
        ui.tips2_text_rect = ui.tips2_text.get_rect(topleft=(500, 55))

        ui.moves_text = ui.font4.render("MOVES", True, (10, 15, 31))
        ui.moves_text_rect = ui.moves_text.get_rect(topleft=(300, 50))

        ui.right_text = ui.font8.render("RIGHT", True, (10, 15, 31))
        ui.right_text_rect = ui.right_text.get_rect(topleft=(320, 120))

        ui.left_text = ui.font8.render("LEFT", True, (10, 15, 31))
        ui.left_text_rect = ui.left_text.get_rect(topleft=(325, 180))

        ui.jump_text = ui.font8.render("JUMP", True, (10, 15, 31))
        ui.jump_text_rect = ui.jump_text.get_rect(topleft=(320, 240))

        ui.dash_text = ui.font8.render("DASH", True, (10, 15, 31))
        ui.dash_text_rect = ui.dash_text.get_rect(topleft=(320, 300))

        ui.light_text = ui.font8.render("LIGHT ATTACK", True, (10, 15, 31))
        ui.light_text_rect = ui.light_text.get_rect(topleft=(280, 360))

        ui.slash_text = ui.font8.render("SLASH ATTACK", True, (10, 15, 31))
        ui.slash_text_rect = ui.slash_text.get_rect(topleft=(280, 420))

        ui.keybinds_text = ui.font4.render("KEYBINDS", True, (10, 15, 31))
        ui.keybinds_text_rect = ui.keybinds_text.get_rect(topleft=(600, 50))

        ui.d_text = ui.font8.render("D", True, (10, 15, 31))
        ui.d_text_rect = ui.d_text.get_rect(topleft=(670, 120))

        ui.a_text = ui.font8.render("A", True, (10, 15, 31))
        ui.a_text_rect = ui.a_text.get_rect(topleft=(670, 180))

        ui.space_text = ui.font8.render("SPACEBAR", True, (10, 15, 31))
        ui.space_text_rect = ui.space_text.get_rect(topleft=(630, 240))

        ui.l_text = ui.font8.render("L", True, (10, 15, 31))
        ui.l_text_rect = ui.l_text.get_rect(topleft=(670, 300))

        ui.j_text = ui.font8.render("J", True, (10, 15, 31))
        ui.j_text_rect = ui.j_text.get_rect(topleft=(670, 360))

        ui.k_text = ui.font8.render("K", True, (10, 15, 31))
        ui.k_text_rect = ui.k_text.get_rect(topleft=(670, 420))

        ui.death_text = ui.font5.render("YOU DIED", True,(139, 0, 0))
        ui.death_rect = ui.death_text.get_rect(center=(550, 330))

        ui.win_text = ui.font5.render("YOU WON", True,(17, 207, 80))
        ui.win_rect = ui.win_text.get_rect(center=(550, 330))

        ui.interact_text = ui.font3.render("Press 'E' to Enter", True,(255, 255, 255))
        ui.interact_text_button = ui.interact_text.get_rect(topleft=(825,530))  

        ui.slash_locked_text = ui.font7.render("Slash Attack Locked!", True,(199, 6, 38))
        ui.slash_locked_rect = ui.slash_locked_text.get_rect(center=(540, 680))

        ui.slash_unlocked_text = ui.font7.render("Slash Attack Unlocked! Press 'K' To Use", True,(17, 207, 80))
        ui.slash_unlocked_rect = ui.slash_unlocked_text.get_rect(center=(540, 680))
    

    def state_fix(ui, state): #Handles the error handling and position fixing of UI elements when switching between game states
        if state.game_state == "Level2":
            ui.interact_text_button = ui.interact_text.get_rect(topleft=(5,0))
        else:
             ui.interact_text_button = ui.interact_text.get_rect(topleft=(825,530))  
        
        #Keep track of whether the player is playing the game or not (in a level/lobby or not)
        if state.previous_game_state == "Menu":
            state.in_level = False
        else:
            state.in_level = True
        
        #Change the color of the buttons when hovered over and fix their positions if necessary
        if state.game_state == "Menu":
            mouse_pos = pygame.mouse.get_pos()
            if ui.play_button.collidepoint(mouse_pos):
                 ui.play_text = ui.font.render("PLAY", True, (181, 71, 83))
            elif ui.continue_button.collidepoint(mouse_pos):
                 ui.continue_text = ui.font.render("CONTINUE", True, (181, 71, 83))
            elif ui.quit_button.collidepoint(mouse_pos):
                ui.quit_text = ui.font.render("QUIT", True, (181, 71, 83))
            elif ui.options_button.collidepoint(mouse_pos):
                 ui.options_text = ui.font.render("OPTIONS", True, (181, 71, 83))
            else:
                 ui.quit_text = ui.font.render("QUIT", True, (163, 36, 60))
                 ui.options_text = ui.font.render("OPTIONS", True, (163, 36, 60))
                 ui.play_text = ui.font.render("PLAY", True, (163, 36, 60))
                 ui.continue_text = ui.font.render("CONTINUE", True, (163, 36, 60))
        
        elif state.game_state == "Settings":
            mouse_pos = pygame.mouse.get_pos()
            if ui.controls_button.collidepoint(mouse_pos):
                ui.controls_text = ui.font4.render("CONTROLS", True, (120, 150, 230))
            elif ui.mainmenu_button.collidepoint(mouse_pos):
                ui.mainmenu_text = ui.font4.render("RETURN TO MAIN MENU", True, (120, 150, 230))
            elif ui.backtogame_button.collidepoint(mouse_pos) and state.in_level:
                ui.backtogame_text = ui.font4.render("BACK TO GAME", True, (120, 150, 230))  
            else:
                ui.mainmenu_text = ui.font4.render("RETURN TO MAIN MENU", True, (10, 15, 31))
                ui.controls_text = ui.font4.render("CONTROLS", True, (10, 15, 31))
                ui.backtogame_text = ui.font4.render("BACK TO GAME", True, (10, 15, 31))
        
        elif state.game_state == "Controls":
            mouse_pos = pygame.mouse.get_pos()
            if ui.backtosettings_button.collidepoint(mouse_pos):
                ui.backtosettings_text = ui.font4.render("BACK TO SETTINGS", True, (120, 150, 230))  
            else:
                ui.backtosettings_text = ui.font4.render("BACK TO SETTINGS", True, (10, 15, 31))
        
        elif state.game_state == "Death Screen":
            mouse_pos = pygame.mouse.get_pos()
            if ui.controls_button.collidepoint(mouse_pos):
                ui.controls_text = ui.font4.render("CONTROLS", True, (120, 150, 230))

            elif ui.mainmenu_button.collidepoint(mouse_pos):
                ui.mainmenu_text = ui.font4.render("RETURN TO MAIN MENU", True, (120, 150, 230))
            else:
                ui.mainmenu_text = ui.font4.render("RETURN TO MAIN MENU", True, (10, 15, 31))

            if state.game_state != "Menu":
                ui.mainmenu_button = ui.mainmenu_text.get_rect(topleft=(360,500))
        
        elif state.game_state == "Win Screen":
            mouse_pos = pygame.mouse.get_pos()
            if ui.controls_button.collidepoint(mouse_pos):
                ui.controls_text = ui.font4.render("CONTROLS", True, (120, 150, 230))


            elif ui.mainmenu_button.collidepoint(mouse_pos):
                ui.mainmenu_text = ui.font4.render("RETURN TO MAIN MENU", True, (120, 150, 230))
            else:
                ui.mainmenu_text = ui.font4.render("RETURN TO MAIN MENU", True, (10, 15, 31))
            
            if state.game_state != "Menu":
                ui.mainmenu_button = ui.mainmenu_text.get_rect(topleft=(360,500))




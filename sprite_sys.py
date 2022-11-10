# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:52:21 2022

@author: Zachary Mark
"""

import pygame

class Sprites():
    def __init__(self):
        
        self.pause=pygame.image.load("Sprites/Pause Logo.png").convert_alpha()
        #character
        player_sheet=pygame.image.load("Sprites/Character_Sheet.png").convert_alpha()
        
        
        self.character_sheet={"Right"   : [player_sheet.subsurface(pygame.Rect(0,0,17,21)),
                                           player_sheet.subsurface(pygame.Rect(19,0,17,21)),
                                           player_sheet.subsurface(pygame.Rect(0,0,17,21)),
                                           player_sheet.subsurface(pygame.Rect(38,0,17,21))],
                              "Left"    : [player_sheet.subsurface(pygame.Rect(0,23,17,21)),
                                           player_sheet.subsurface(pygame.Rect(19,23,17,21)),
                                           player_sheet.subsurface(pygame.Rect(0,23,17,21)),
                                           player_sheet.subsurface(pygame.Rect(38,23,17,21))],
                              
                              "Right Arm" : player_sheet.subsurface(pygame.Rect(57,0,14,10)),
                              
                              "Left Arm" : player_sheet.subsurface(pygame.Rect(57,11,14,10))
                              }
        
        #Zombie
        zombie_sheet=pygame.image.load("Sprites/Zombie_Sheet.png").convert_alpha()
        
        
        self.zombie_sheet={"Right"   : [zombie_sheet.subsurface(pygame.Rect(0,0,14,24)),
                                           zombie_sheet.subsurface(pygame.Rect(15,0,14,24)),
                                           zombie_sheet.subsurface(pygame.Rect(0,0,14,24)),
                                           zombie_sheet.subsurface(pygame.Rect(30,0,14,24))],
                           "Left"    : [zombie_sheet.subsurface(pygame.Rect(0,26,14,24)),
                                           zombie_sheet.subsurface(pygame.Rect(15,26,14,24)),
                                           zombie_sheet.subsurface(pygame.Rect(0,26,14,24)),
                                           zombie_sheet.subsurface(pygame.Rect(30,26,14,24))],
                           
                           "Right Belly"     : zombie_sheet.subsurface(pygame.Rect(71,0,25,24)),
                           "Right Back"     : zombie_sheet.subsurface(pygame.Rect(45,0,25,24)),
                          "Left Belly"     : zombie_sheet.subsurface(pygame.Rect(71,26,25,24)),
                          "Left Back"     : zombie_sheet.subsurface(pygame.Rect(45,26,25,24))
                                  
                              }
        
        self.zambini_sheet={"Right"   :   [zombie_sheet.subsurface(pygame.Rect(0,52,14,19)),
                                           zombie_sheet.subsurface(pygame.Rect(15,52,14,19)),
                                           zombie_sheet.subsurface(pygame.Rect(0,52,14,19)),
                                           zombie_sheet.subsurface(pygame.Rect(30,52,14,19))],
                            
                           "Left"    : [zombie_sheet.subsurface(pygame.Rect(0,72,14,19)),
                                           zombie_sheet.subsurface(pygame.Rect(15,72,14,19)),
                                           zombie_sheet.subsurface(pygame.Rect(0,72,14,19)),
                                           zombie_sheet.subsurface(pygame.Rect(30,72,14,19))],
                           
                           "Right Belly"     : zombie_sheet.subsurface(pygame.Rect(45,52,19,19)),
                           "Right Back"     : zombie_sheet.subsurface(pygame.Rect(65,52,19,19)),
                          "Left Belly"     : zombie_sheet.subsurface(pygame.Rect(45,72,19,19)),
                          "Left Back"     : zombie_sheet.subsurface(pygame.Rect(65,72,19,19))
                                  
                              }
                
                
        icon_sheet=pygame.image.load("Sprites/In_Game_Icons.png")
        self.icons={"Enemy_Alert"   : icon_sheet.subsurface(0,0,17,29)}
        
        power_up_sheet=pygame.image.load("Sprites/power_up_sprites.png")
        self.power_up={'XP_Magnet' : power_up_sheet}
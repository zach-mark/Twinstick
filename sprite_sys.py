# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:52:21 2022

@author: Zachary Mark
"""

import pygame

class Sprites():
    def __init__(self):
        
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
        player_sheet=pygame.image.load("Sprites/Zombie_Sheet.png").convert_alpha()
        
        
        self.zombie_sheet={"Right"   : [player_sheet.subsurface(pygame.Rect(0,0,14,24)),
                                           player_sheet.subsurface(pygame.Rect(15,0,14,24)),
                                           player_sheet.subsurface(pygame.Rect(0,0,14,24)),
                                           player_sheet.subsurface(pygame.Rect(30,0,14,24))],
                           "Left"    : [player_sheet.subsurface(pygame.Rect(0,26,14,24)),
                                           player_sheet.subsurface(pygame.Rect(15,26,14,24)),
                                           player_sheet.subsurface(pygame.Rect(0,26,14,24)),
                                           player_sheet.subsurface(pygame.Rect(30,26,14,24))],
                           
                           "Right Belly"     : player_sheet.subsurface(pygame.Rect(71,0,25,24)),
                           "Right Back"     : player_sheet.subsurface(pygame.Rect(45,0,25,24)),
                          "Left Belly"     : player_sheet.subsurface(pygame.Rect(71,26,25,24)),
                          "Left Back"     : player_sheet.subsurface(pygame.Rect(45,26,25,24))
                                  
                              }
        
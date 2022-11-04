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
        
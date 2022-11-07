# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 20:39:25 2022

@author: Zachary Mark
"""

import pygame

class Block():
    def __init__(self, xy):
        self.x=xy[0]
        self.y=xy[1]
        
        self.width=32
        self.height=32
        
        self.my_rect=pygame.Rect(self.x,self.y,self.width,self.height)
        
    
    def logic(self):
        pass
    
    def draw(self, DISPLAY):
        
        pygame.draw.rect(DISPLAY, (0,0,0), self.my_rect)
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:02:05 2022

@author: Zachary Mark
"""
import pygame

#antidrift
antidrift_setting=0.05

class Player():
    def __init__(self):
        #player stats
        self.speed=10
        
        self.x=30
        self.y=30
        
    def user_inputs(self, axis_a,axis_b):
        """
        Parameters
        ----------
        axis_a : Touple
            Movement axis inputs.
        axis_b : Touple
            Firing axis inputs.

        Returns
        -------
        None.

        """
        
        if abs(axis_a[0])>antidrift_setting:
            self.x+=axis_a[0]*self.speed
        if abs(axis_a[1])>antidrift_setting:
            self.y+=axis_a[1]*self.speed
        
        
    
    def logic(self):
        
        pass
    
    def draw(self, DISPLAY):
        
        pygame.draw.rect(DISPLAY, (255,255,255), [self.x,self.y,30,30])
        
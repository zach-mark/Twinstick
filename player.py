# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:02:05 2022

@author: Zachary Mark
"""
import pygame

#antidrift
moving_antidrift_setting=0.25
shooting_sensitivity=0.1

class Player():
    def __init__(self, master):
        #player stats
        self.speed=10
        
        self.x=30
        self.y=30
        
        
        #game engine setup
        self.master=master
        
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
        
        #MOVEMENT INPUT
        if abs(axis_a[0])>moving_antidrift_setting:
            self.x+=axis_a[0]*self.speed
        if abs(axis_a[1])>moving_antidrift_setting:
            self.y+=axis_a[1]*self.speed
        
        #SHOOTING INPUT
        trying_to_shoot=False
        
        
        if abs(axis_b[0])>shooting_sensitivity:
            shoot_dir_x=axis_b[0]
            trying_to_shoot=True
        else:
            shoot_dir_x=0
        if abs(axis_b[1])>shooting_sensitivity:
            self.y+=axis_a[1]*self.speed
            shoot_dir_y=axis_b[1]
            trying_to_shoot=True
        else:
            shoot_dir_y=0
            
        if trying_to_shoot==True:
            self.master.BULLETS.append(
                Bullet((self.x+15,self.y+15),
                       (shoot_dir_x,shoot_dir_y)))
        
    
    def logic(self):
        
        pass
    
    def draw(self, DISPLAY):
        
        pygame.draw.rect(DISPLAY, (255,255,255), [self.x,self.y,30,30])


class Bullet():
    def __init__(self, xy, angle):
        #bullet_speed
        self.speed=20
        self.life=10
        
        self.x=xy[0]
        self.y=xy[1]
        
        self.angle=angle
        
        
    def logic(self):
        self.x+=self.angle[0]*self.speed
        self.y+=self.angle[1]*self.speed
    
    def draw(self, DISPLAY):
        pygame.draw.rect(DISPLAY, (255,0,0), [self.x,self.y,3,3])
        
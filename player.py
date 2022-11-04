# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:02:05 2022

@author: Zachary Mark
"""
import pygame

from math import sqrt, pi, sin

import numpy as np

#antidrift
moving_antidrift_setting=0.25
shooting_sensitivity=0.1


class Player():
    def __init__(self, master):
        #player stats
        self.speed=5
        
        self.x=30
        self.y=30
        
        self.shot_cooldown=20
        self.cooldown_timer=0
        
        self.bullet_mode="Spread4"
        #game engine setup
        self.master=master
        self.can_shoot=False
        
        #animation_setup
        self.facing="Right"
        self.frame=0
        self.frame_timing=15
        self.arm_distance=15
        
        self.gun_angle=0
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
            trying_to_shoot=True
        if abs(axis_b[1])>shooting_sensitivity:
            trying_to_shoot=True
            
        if trying_to_shoot==True and self.can_shoot==True:
            shoot_dir_x=axis_b[0]
            shoot_dir_y=axis_b[1]
            
            self.can_shoot=False
            self.cooldown_timer=self.shot_cooldown
            
            
            entity_1= (0,0)
            entity_2= (shoot_dir_x,shoot_dir_y)
            
            
            x_dis=abs(entity_1[0]-entity_2[0])
            y_dis=abs(entity_1[1]-entity_2[1])
                            
            distance=sqrt(x_dis**2+y_dis**2)
        
            x_vect=entity_2[0]-entity_1[0]
            y_vect=entity_2[1]-entity_1[1]
            unit_vector=(x_vect/distance, y_vect/distance)
            
            p1=(0,0)
            p2=unit_vector
            
            #find the angle
            ang1 = np.arctan2(*p1[::-1])
            ang2 = np.arctan2(*p2[::-1])
            angle_shot=np.rad2deg((ang1 - ang2) % (2 * np.pi))
            
            self.gun_angle=angle_shot
            #ANGLE SHOT should be used for all calculating of special bullets
            
            if self.bullet_mode=="Normal":
                self.master.BULLETS.append(
                    Bullet((self.x,self.y),
                           angle_shot))
            
            elif self.bullet_mode=="Spread2":
                
                self.master.BULLETS.append(
                    Bullet((self.x,self.y),
                           angle_shot-5))
                self.master.BULLETS.append(
                    Bullet((self.x,self.y),
                           angle_shot+5))
            
            elif self.bullet_mode=="Spread4":
                
                self.master.BULLETS.append(
                    Bullet((self.x,self.y),
                           angle_shot-5))
                self.master.BULLETS.append(
                    Bullet((self.x,self.y),
                           angle_shot+5))
                self.master.BULLETS.append(
                    Bullet((self.x,self.y),
                           angle_shot-2.5))
                self.master.BULLETS.append(
                    Bullet((self.x,self.y),
                           angle_shot+2.5))
                
            
        
    
    def logic(self):
        
        if self.cooldown_timer>0:
            self.cooldown_timer-=1
        else:
            self.can_shoot=True
    
    def draw(self, DISPLAY):
        
        if 90>=self.gun_angle>=0 or 270<self.gun_angle<=360:
            arm_rotate=pygame.transform.rotate(self.master.sprites.character_sheet["Right Arm"], self.gun_angle)
            self.facing="Right"
        else:
            arm_rotate=pygame.transform.rotate(self.master.sprites.character_sheet["Left Arm"], self.gun_angle-180)
            self.facing="Left"
        
        theta=(self.gun_angle/180)*pi
    
        if 270>=self.gun_angle>=90:
            val=-1
        else:
            val=1
        hypotenuse=self.arm_distance
        
        y=hypotenuse*sin(theta)
        
        
        x=sqrt(hypotenuse**2 - y**2)*val
        
        
        
        DISPLAY.blit( self.master.sprites.character_sheet[self.facing][0], (self.x,self.y))
        DISPLAY.blit(arm_rotate, (self.x+x,self.y-y))


class Bullet():
    def __init__(self, xy, angle):
        #bullet_speed
        self.speed=10
        self.life=45
        
        self.x=xy[0]
        self.y=xy[1]
        
        
    
        theta=(angle/180)*pi
        
        if 270>=angle>=90:
            val=-1
        else:
            val=1
        hypotenuse=1
        
        y=hypotenuse*sin(theta)
        
        
        x=sqrt(hypotenuse**2 - y**2)*val
                
        self.vector=(x,-y)
        
        
        
    def logic(self):
        self.life-=1
        
        self.x+=self.vector[0]*self.speed
        self.y+=self.vector[1]*self.speed
    
    def draw(self, DISPLAY):
        
        pygame.draw.circle(DISPLAY, (255,255,255), [self.x,self.y], 3)
        
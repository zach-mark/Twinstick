# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:02:05 2022

@author: Zachary Mark
"""
import pygame, random

import particles

from math import sqrt, pi, sin, cos, radians

import numpy as np

#antidrift
moving_antidrift_setting=0.25
shooting_sensitivity=0.1


class Player():
    def __init__(self, master):
        #player stats
        self.speed=5
        
        self.absorb_range=100
        self.x=30
        self.y=30
        
        self.shot_cooldown=5
        self.cooldown_timer=0
        
        self.bullet_mode="Normal"
        
        self.bullet_speed=12
        self.bullet_life=80
        
        #game engine setup
        self.master=master
        self.can_shoot=False
        
        
        #animation_setup
        self.facing="Right"
        self.move_face="Right"
        self.moving=False
        self.frame=0
        self.frame_timing=5
        self.frame_tick=0
        self.arm_distance=15
        self.gun_out=False
        
        self.gun_angle=0
        
        #self_power_up_effects
        self.active_effects={}
        self.magnet_exp_on=False
        self.magnet_exp_timer=0
        
        self.exp=0
    def exp_up(self, exp):
        self.exp+=exp
        
        
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
        self.moving=False
        
        #MOVEMENT INPUT
        if abs(axis_a[0])>moving_antidrift_setting:
                        
            self.x+=axis_a[0]*self.speed
            if axis_a[0]>0:
                self.move_face="Right"
            else:
                self.move_face="Left"
            
            self.moving=True
                
        if abs(axis_a[1])>moving_antidrift_setting:
            self.y+=axis_a[1]*self.speed
            
            self.moving=True
        
        #SHOOTING INPUT
        trying_to_shoot=False
        
        if abs(axis_b[0])>shooting_sensitivity:
            trying_to_shoot=True
        if abs(axis_b[1])>shooting_sensitivity:
            trying_to_shoot=True
        if trying_to_shoot==True:
            self.gun_out=True
            
            
        
            
            
            shoot_dir_x=axis_b[0]
            shoot_dir_y=axis_b[1]
            
            
            
            
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
            if self.can_shoot==True:
                self.can_shoot=False
                self.cooldown_timer=self.shot_cooldown
                if self.bullet_mode=="Normal":
                    self.master.BULLETS.append(Bullet(self.master, (self.x,self.y),angle_shot,self.bullet_speed, self.bullet_life, 5))
        else:
            self.gun_out=False
                
            
        
    
    def logic(self):
        
        if self.cooldown_timer>0:
            self.cooldown_timer-=1
        else:
            self.can_shoot=True
        
        if self.moving==True:
            self.frame_tick+=1
            if self.frame_tick>=self.frame_timing:
                self.frame_tick=0
                self.frame+=1
                if self.frame>3:
                    self.frame=0   
        else:
            self.frame=0   
            
        self.power_up_effects()
                    
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
        
        if self.gun_out==False:
            self.facing=self.move_face
        DISPLAY.blit( self.master.sprites.character_sheet[self.facing][self.frame], (self.x,self.y))
        if self.gun_out==True:
            DISPLAY.blit(arm_rotate, (self.x+x,self.y-y))
        
            
            
        
        if self.master.DEBUG_MODE==True:
            #draw absorb range
            pygame.draw.circle(DISPLAY, (0,255,120), [self.x,self.y], self.absorb_range, 1)
            
            #draw attack range
            pygame.draw.circle(DISPLAY, (0,0,0), [self.x,self.y], self.bullet_speed*self.bullet_life, 1)
            
            #draw aim line        
            theta_rad = pi/2 - radians(self.gun_angle+90)
            x_targ= self.x + self.bullet_speed*self.bullet_life * cos(theta_rad)
            y_targ= self.y + self.bullet_speed*self.bullet_life * sin(theta_rad)
    
            pygame.draw.line(DISPLAY, (255,0,0),(self.x,self.y),(x_targ,y_targ),1)
            
    
    def power_up_effects(self):
        if self.magnet_exp_on==True:
            self.magnet_exp_timer-=1
            
            if self.magnet_exp_timer<1:
                self.magnet_exp_timer=0
                self.magnet_exp_on=False
    def exp_magnet(self):
        self.magnet_exp_on=True
        self.magnet_exp_timer=5
        
        


class Bullet():
    def __init__(self, master, xy, angle, speed, life, penetration=0):
        
        self.master=master
        #bullet_speed
        self.speed=speed
        self.life=life+1
        
        self.x=xy[0]
        self.y=xy[1]
        
        self.damage=5
        self.penetration=penetration
        
        self.hit_box=[-3,-3,6,6]
        self.my_rect=pygame.Rect(self.x+self.hit_box[0], self.y+self.hit_box[1],
                                 self.hit_box[2], self.hit_box[3]) 
        
        
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
        
        self.my_rect=pygame.Rect(self.x+self.hit_box[0], self.y+self.hit_box[1],
                                 self.hit_box[2], self.hit_box[3]) 
        self.check_object_collides()
        
    def check_object_collides(self):
        
        
        collides=self.my_rect.collidelist(self.master.obstacle_rects)
        if collides!=-1:
            self.life=0
    
    def draw(self, DISPLAY):
        
        pygame.draw.circle(DISPLAY, (20,20,20), [self.x,self.y], 3)

class XP_ORB():
    def __init__(self, master, xy, exp):
        self.master=master
        self.speed=random.randint(3, 5)
        
        self.x=xy[0]
        self.y=xy[1]
        
        self.exp=exp
        self.color= [0,
                     random.randint(180, 255),
                     random.randint(25, 120)]
        self.phase=0
        self.worble=[random.randint(0,9),0.1]
        
        self.phase_ticks=15
        self.life=1
        
        self.vector= (random.random()*2-1,random.random()*2-1)
        
        
    def logic(self):
        
        if self.phase==0:
            self.phase_ticks-=1
            if self.phase_ticks<1:
                self.phase=1
                self.speed=0
            self.x+=self.vector[0]*self.speed
            self.y+=self.vector[1]*self.speed
            
            self.speed*=0.85
            
        else:
            self.target=(self.master.PLAYER.x,self.master.PLAYER.y)
                
            target_vector=(0,0)
            
            x_dif= self.target[0]-self.x
            y_dif= self.target[1]-self.y
            
            total_dif=abs(x_dif)+abs(y_dif)
            
            distance=sqrt(abs(x_dif)**2+abs(y_dif)**2)
            
            if distance<=self.master.PLAYER.absorb_range:
                self.speed=4
                self.phase=2
            elif self.master.PLAYER.magnet_exp_on==True:
                self.speed=4
                self.phase=2
                
            else:
                if self.phase==1:
                    self.speed=0
                    self.worble[0]+=self.worble[1]
                    self.y+=self.worble[1]
                    self.color[2]+=self.worble[1]*10
                    if self.color[2]<0:
                        self.color[2]=0
                    if self.worble[0]>10:
                        self.worble[1]=-0.1
                    elif self.worble[0]<1:
                        self.worble[1]=0.1
                        
            
            x_proportion=x_dif/total_dif
            y_proportion=y_dif/total_dif
            
            target_vector= (x_proportion, y_proportion)
            
            if total_dif<3:
                self.master.PLAYER.exp_up(self.exp)
                self.life=0
                
            #move orb
            self.x+=target_vector[0]*self.speed
            self.y+=target_vector[1]*self.speed
            
    
        
    
    def draw(self, DISPLAY):
        pygame.draw.circle(DISPLAY,(0,0,0), [self.x,self.y], 4)
        pygame.draw.circle(DISPLAY, self.color, [self.x,self.y], 2)
        

"""
Power Ups
"""

class Magnet_Power_Up():
    def __init__(self, master, xy):
        self.master=master
        self.sprite=self.master.sprites.power_up['XP_Magnet']
        
        
        self.x=xy[0]
        self.y=xy[1]
        
        self.phase=1
        self.worble=[random.randint(0,9),0.1]
        
        self.phase_ticks=15
        self.life=1
        
        self.vector= (random.random()*2-1,random.random()*2-1)
        
        
    def logic(self):
        
    
        self.target=(self.master.PLAYER.x,self.master.PLAYER.y)
            
        target_vector=(0,0)
        
        x_dif= self.target[0]-self.x
        y_dif= self.target[1]-self.y
        
        total_dif=abs(x_dif)+abs(y_dif)
        
        distance=sqrt(abs(x_dif)**2+abs(y_dif)**2)
        
        if distance<=self.master.PLAYER.absorb_range:
            self.speed=6
            self.phase=2
        else:
            if self.phase==1:
                self.speed=0
                self.worble[0]+=self.worble[1]
                self.y+=self.worble[1]
                if self.worble[0]>10:
                    self.worble[1]=-0.1
                elif self.worble[0]<1:
                    self.worble[1]=0.1
                    
        
        x_proportion=x_dif/total_dif
        y_proportion=y_dif/total_dif
        
        target_vector= (x_proportion, y_proportion)
        
        if total_dif<3:
            self.master.PLAYER.exp_magnet()
            self.life=0
            
        #move orb
        self.x+=target_vector[0]*self.speed
        self.y+=target_vector[1]*self.speed
            
    
        
    
    def draw(self, DISPLAY):
        
        DISPLAY.blit(self.sprite, (self.x,self.y))
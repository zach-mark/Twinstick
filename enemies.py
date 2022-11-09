# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 11:01:00 2022

@author: Zachary Mark
"""
import pygame, particles, random, player

from math import sqrt


POST_HIT_SAFETY_TIME=5

def check_bullet_collides(enemy, master):
    damage=0
    enemy.my_rect=pygame.Rect(enemy.x+enemy.hit_box[0], enemy.y+enemy.hit_box[1],
                                 enemy.hit_box[2], enemy.hit_box[3]) 
        
    collides=enemy.my_rect.collidelist(master.bullet_rects)
    if collides!=-1:
        bullet=master.bullet_dict[collides]
        damage= bullet.damage
        if bullet.penetration<1:
            bullet.life=0
        else:
            bullet.penetration-=1
        enemy.post_hit_safe=True
        enemy.post_hit_tickdown=POST_HIT_SAFETY_TIME
    return damage

class Zombie():
    def __init__(self, master, xy, zombie_type=0):
        
        if zombie_type==0:
            self.hp=10
            self.speed=0.5
            self.sprite=master.sprites.zombie_sheet
            self.hit_box=[0,0,13,24]
            self.frame_timing=15
            
        else:
            self.hp=5
            self.speed=3
            self.sprite=master.sprites.zambini_sheet
            self.hit_box=[0,0,14,19]
            self.frame_timing=5
        
        
        self.master=master
        
        self.x=xy[0]
        self.y=xy[1]
        
        self.alive=True
        self.post_hit_safe=False
        self.post_hit_tickdown=0
        
        
        self.exp_value=5
        
        self.player_aware=False
        self.aimless_target=(random.randint(0, self.master.level_dim[0]),
                             random.randint(0, self.master.level_dim[1]))
        self.player_awareness_distance=200
        #engine setup
        self.del_self=False
        self.death_counter=60+random.randint(0,1200)
        self.hit_box=[0,0,13,24]
        self.my_rect=pygame.Rect(self.x+self.hit_box[0], self.y+self.hit_box[1],
                                 self.hit_box[2], self.hit_box[3]) 
        #animation_setup
        self.facing="Right"
        self.frame=0
        self.frame_tick=0
    
    def logic(self):
        
        if self.alive==True:
            
            if self.post_hit_safe==False:
                damage=check_bullet_collides(self, self.master)
                if damage!=0:
                    self.hp-=damage
                    for i in range(0, 5+random.randint(0, 4)):
                        self.master.PARTICLES.append(particles.Blood((self.x,self.y)))
            else:
                
                self.post_hit_tickdown-=1
                if self.post_hit_tickdown<1:
                    self.post_hit_safe=False
                
                
            #find zombie target and vector
            self.target=(self.master.PLAYER.x,self.master.PLAYER.y)
            
            target_vector=(0,0)
            
            x_dif= self.target[0]-self.x
            y_dif= self.target[1]-self.y
            
            total_dif=abs(x_dif)+abs(y_dif)
            
            x_proportion=x_dif/total_dif
            y_proportion=y_dif/total_dif
            
            target_vector= (x_proportion, y_proportion)
            
            #distance_from target
            distance=sqrt(abs(x_dif)**2+abs(y_dif)**2)
            
            if self.player_aware==False:
                if distance< self.player_awareness_distance:
                    self.player_aware=True
                else:
                    
                    self.target=self.aimless_target
                
                    target_vector=(0,0)
                    
                    x_dif= self.target[0]-self.x
                    y_dif= self.target[1]-self.y
                    
                    total_dif=abs(x_dif)+abs(y_dif)
                    
                    x_proportion=x_dif/total_dif
                    y_proportion=y_dif/total_dif
                    
                    target_vector= (x_proportion, y_proportion)
                    
                    #update zombie facing
                    if x_proportion>0:
                        self.facing="Right"
                    else:
                        self.facing="Left"
                    
                    #move zombie
                    self.x+=target_vector[0]*self.speed
                    self.y+=target_vector[1]*self.speed
                    #distance_from target
                    distance=sqrt(abs(x_dif)**2+abs(y_dif)**2)
                    
                    if distance<10:
                        self.aimless_target = (random.randint(0, self.master.level_dim[0]),
                                                          random.randint(0, self.master.level_dim[1]))
            else:
            
            
                #update zombie facing
                if x_proportion>0:
                    self.facing="Right"
                else:
                    self.facing="Left"
                
                #move zombie
                self.x+=target_vector[0]*self.speed
                self.y+=target_vector[1]*self.speed
                
                
            #check for life
            if self.hp<0:
                j=0
                while j<self.exp_value:
                    self.master.PARTICLES.append(player.XP_ORB(self.master, (self.x,self.y), 1))
                    j+=1
                for i in range(0,20):
                    self.master.PARTICLES.append(particles.Exp_Gain((self.x,self.y)))
                    
                self.alive=False
                self.player_aware=True
                for i in range(20):
                    self.master.PARTICLES.append(particles.Blood((self.x,self.y)))
                death_pos=random.randint(0,1)
                
                if death_pos==1:
                    self.facing=self.facing+" Belly"
                else:
                    self.facing=self.facing+" Back"
            #animation ticks
            
            self.frame_tick+=1
            if self.frame_tick>=self.frame_timing:
                
                self.frame_tick=0
                self.frame+=1
                if self.frame>3:
                    self.frame=0
        else:
            self.death_counter-=1
            
            if self.death_counter<1:
                self.del_self=True
        
        
        
        
    
    def draw(self, DISPLAY):
        
        if self.alive==True:
            DISPLAY.blit( self.sprite[self.facing][self.frame], (self.x,self.y))
        else:
            
            DISPLAY.blit( self.sprite[self.facing], (self.x,self.y))
        if self.master.DEBUG_MODE==True:
            if self.player_aware==False:
                pygame.draw.circle(DISPLAY, (0,0,255), [self.x,self.y], self.player_awareness_distance, 1)
            
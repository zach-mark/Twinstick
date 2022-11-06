# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:00:26 2022

@author: Zach Mark

TWINSTICK
"""

import pygame, sys, random

import player, sprite_sys, enemies

pygame.init()

# Setup the screen
SCREEN_SIZE=[800,600]
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
#SCREEN = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)

pygame.display.set_caption("Twinstick")

# Setup the joysticks
pygame.joystick.init()
joy_count=pygame.joystick.get_count()
JOYSTICK=[]
for i in range(joy_count):
    JOYSTICK.append(pygame.joystick.Joystick(i))
    JOYSTICK[i].init()

AXIS_A=(0,0)
AXIS_B=(0,0)

# Setup clock
CLOCK = pygame.time.Clock()
FPS= 60

#Game Instances
class GAME():
    def __init__(self):
        self.paused=False
        
        self.sprites=sprite_sys.Sprites()
        self.ENEMIES=[]
        self.BULLETS=[]
        self.PLAYER=player.Player(self)
        
        self.enemy_rects=[]
        self.bullet_rects=[]
        self.bullet_dict={}
        self.obstacle_rects=[]
        
        self.PARTICLES=[]
    def pause(self):
        
        if self.paused==True:
            self.paused=False
        else:
            self.paused=True
        
    def pause_logic(self):
        pass
    
    def pause_render(self):
         
        SCREEN.blit(self.sprites.pause,(0,0))
    
    def update_collisions(self):
        #enemies
        
        self.enemy_rects=[]
        for enemy in self.ENEMIES:
            if enemy.alive==True:
                rect=pygame.Rect(enemy.x+enemy.hit_box[0], enemy.y+enemy.hit_box[1],
                                 enemy.hit_box[2], enemy.hit_box[3])
                self.enemy_rects.append(rect)
        
        #bullets
        self.bullet_rects=[]
        self.bullet_dict={}
        for bullet in self.BULLETS:
            rect=pygame.Rect(bullet.x+bullet.hit_box[0], bullet.y+bullet.hit_box[1],
                             bullet.hit_box[2], bullet.hit_box[3])
            self.bullet_rects.append(rect)
            bullet_index=len(self.bullet_rects)-1
            self.bullet_dict[bullet_index]=bullet
        
        



def main():
    
    user_input()
    
    if game.paused==False:
        logic()
    else:
        game.pause_logic()
        
    rendering()
    CLOCK.tick(FPS)
    
    pygame.display.set_caption("Twinstick: "+str(round(CLOCK.get_fps(),0)))
    
def user_input():
    global AXIS_A, AXIS_B
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close.
            session_kill()
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button==7:
                game.pause()
                print("Pause")
        elif event.type == pygame.JOYBUTTONUP:
            pass
    
    
    #joystick code
    for joystick in JOYSTICK:
        
        
        #Axis 0 and 1- left stick
        axis_0=joystick.get_axis(0)
        axis_1=joystick.get_axis(1)
        
        #Axis 2 and 3- right stick
        axis_2=joystick.get_axis(2)
        axis_3=joystick.get_axis(3)
        
        AXIS_A=(axis_0,axis_1)
        AXIS_B=(axis_2,axis_3)
            
        
        
            
    if game.paused==False:
        game.PLAYER.user_inputs(AXIS_A, AXIS_B)
        
    


def logic():
    
    game.PLAYER.logic()
    
    game.update_collisions()
    
    for bullet in game.BULLETS:
        bullet.logic()
        
    i=len(game.BULLETS)-1
    while i>=0:
        if game.BULLETS[i].life<1:
            del game.BULLETS[i]
        i-=1
        
    
    for enemy in game.ENEMIES:
        enemy.logic()
        
    i=len(game.ENEMIES)-1
    while i>=0:
        if game.ENEMIES[i].del_self==True:
            del game.ENEMIES[i]
        i-=1
        
    for particles in game.PARTICLES:
        particles.logic()
    i=len(game.PARTICLES)-1
    while i>=0:
        if game.PARTICLES[i].life<1:
            del game.PARTICLES[i]
        i-=1
        
        
        
    
    new_spawn=random.randint(0, 600)
    if new_spawn==1:
        game.ENEMIES.append(enemies.Zombie(game,(random.randint(0, SCREEN_SIZE[0]),
                                                 random.randint(0, SCREEN_SIZE[1]))))
    
    

def rendering():
    SCREEN.fill((200,191,231))
    
    for particle in game.PARTICLES:
        particle.draw(SCREEN)
        
    for bullet in game.BULLETS:
        bullet.draw(SCREEN)
    for enemy in game.ENEMIES:
        enemy.draw(SCREEN)
        
    game.PLAYER.draw(SCREEN)
    
    
    if game.paused==True:
        game.pause_render()
    
    pygame.display.update()


def session_kill():
    pygame.quit()
    sys.exit()


game=GAME()

game.ENEMIES.append(enemies.Zombie(game,(400,200)))
while True:
    main()
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:00:26 2022

@author: Zach Mark

TWINSTICK
"""

import pygame, sys

import player

pygame.init()

# Setup the screen
SCREEN_SIZE=[500,400]
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

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
        self.ENEMIES=[]
        self.BULLETS=[]
        self.PLAYER=player.Player(self)



def main():
    
    user_input()
    logic()
    rendering()
    CLOCK.tick(FPS)
    
def user_input():
    global AXIS_A, AXIS_B
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close.
            session_kill()
    
    
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
            
        
        
            
    
    game.PLAYER.user_inputs(AXIS_A, AXIS_B)
        
    


def logic():
    for bullet in game.BULLETS:
        bullet.logic()

def rendering():
    SCREEN.fill((200,191,231))
    
    
    for bullet in game.BULLETS:
        bullet.draw(SCREEN)
        
    game.PLAYER.draw(SCREEN)
    
    pygame.display.update()


def session_kill():
    pygame.quit()
    sys.exit()


game=GAME()

while True:
    main()
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:00:26 2022

@author: Zach Mark

TWINSTICK
"""

import pygame, sys

pygame.init()

# Setup the screen
SCREEN_SIZE=[500,400]
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Twinstick")

def main():
    
    user_input()
    logic()
    rendering()
    
    
def user_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close.
            session_kill()

def logic():
    pass

def rendering():
    SCREEN.fill((200,191,231))
    
    
    pygame.display.update()


def session_kill():
    pygame.quit()
    sys.exit()



while True:
    main()
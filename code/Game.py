#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window=pygame.display.set_mode(
        size=(800, 500)
        )

    def run(self, ):
        #main.py
        #print('Setup Start')
        #print('Setup End')
        #print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # Check for all events
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #       print('Finalizando...')
            #       pygame.quit()  # close window
            #       quit() #end pygame






#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window=pygame.display.set_mode(
        size=(WIN_WIDTH, WIN_HEIGHT)     #altera o tamanho da janela/background
        )

    def run(self, ):
        #main.py
        #print('Setup Start')
        #print('Setup End')
        #print('Loop Start')
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                player_score = [0]  #score do Player
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run()
                #if level_return:
                   #level = Level(self.window, 'Level2', menu_return)
                   #level_return = level.run(player_score)
                   #if level_return:
                     # level = Level(self.window, 'Level3', menu_return)
                     # level_return = level.run(player_score)

            elif menu_return == MENU_OPTION[1]:
                score.show()

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()   #close window
                quit()   #end pygame
            else:
                pass






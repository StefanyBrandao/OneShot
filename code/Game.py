#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window=pygame.display.set_mode(
        size=(WIN_WIDTH, WIN_HEIGHT)   #altera o tamanho da janela/background#
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







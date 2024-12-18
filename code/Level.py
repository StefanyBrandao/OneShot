#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from code.Const import COLOR_PINK, WIN_HEIGHT

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from pygame import Surface, Rect
from pygame.font import Font


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('lvl11'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 15000  #15 segundos

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(90)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level_text(40, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_PINK, (20, 15))
            self.level_text(40, f'fps: {clock.get_fps():.0f}', COLOR_PINK, (20, WIN_HEIGHT - 60))
            self.level_text(40, f'entidades: {len(self.entity_list)}', COLOR_PINK, (10, WIN_HEIGHT - 50))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Vladimir Script", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)



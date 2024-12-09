#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from code.Const import COLOR_PINK, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COLOR_BLUE, COLOR_PURPLE, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL

from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from pygame import Surface, Rect
from pygame.font import Font
from code.Player import Player



class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = TIMEOUT_LEVEL
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, ):
        pygame.mixer_music.load(f'./asset/LVL1SOUND.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(90)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(30, f'Player1 - Health: {ent.health} *** Score: {ent.score}', COLOR_PURPLE, (10,10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player':
                                player_score[0] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False


            #TEXTO NA TELA
            self.level_text(30, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_PINK, (10, 50))
            self.level_text(30, f'fps: {clock.get_fps():.0f}', COLOR_PINK, (20, WIN_HEIGHT - 150))
            self.level_text(30, f'entidades: {len(self.entity_list)}', COLOR_PINK, (20, WIN_HEIGHT - 100))
            pygame.display.flip()

            #COLISÕES ENTRE PLAYER E INIMIGO
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

        #pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Vladimir Script", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)



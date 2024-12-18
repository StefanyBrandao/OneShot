#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  #position x e position y
        self.speed = 0

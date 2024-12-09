import pygame
from pygame import Surface


class Score:

   def __init__(self, window: Surface):
       self.window = window
       self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
       self.rect = self.surf.get_rect(left=0, top=0)
       pass

   def save(self):
       pass

   def show(self):
       pygame.mixer_music.load('./asset/Score.mp3')
       pygame.mixer_music.play(-1)
       self.window.blit(source=self.surf, dest=self.rect)
       while True:
           pygame.display.flip()
           pass
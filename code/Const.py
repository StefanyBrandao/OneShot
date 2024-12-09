#ALTERA O TAMANHO DA IMAGEM
import pygame

WIN_WIDTH = 900
WIN_HEIGHT = 870

#ALTERA A COR DA FONTE
COLOR_PURPLE = 154, 44, 254
COLOR_BLUE = 77, 134, 191
COLOR_PINK = 163, 105, 147

#ESCRITA DO MENU
MENU_OPTION = (
    'NEW GAME ONE PLAYER',
    'SCORE',
    'LEAVE'
)

#ALTERA A VELOCIDADE DO BACKGROUND
ENTITY_SPEED = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level1BG5': 0,
    'Level1BG6': 0,
    'Player1': 6,
    'Player1Shot': 6,
    'Enemy1': 6,
    'Enemy1Shot': 6,
    'Enemy2': 6,
    'Enemy2Shot': 6,
}


#TIRO
PLAYER_KEY_UP = {'Player1': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_LCTRL}


#VIDA
ENTITY_HEALTH = {
    'Level1BG0': 999,
    'Level1BG1': 999,
    'Level1BG2': 999,
    'Level1BG3': 999,
    'Level1BG4': 999,
    'Level1BG5': 999,
    'Level1BG6': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Enemy1': 10,
    'Enemy1Shot': 1,
    'Enemy2': 10,
    'Enemy2Shot': 1,
}
ENTITY_DAMAGE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level1BG5': 0,
    'Level1BG6': 0,
    'Player1': 5,
    'Player1Shot': 5,
    'Enemy1': 5,
    'Enemy1Shot': 5,
    'Enemy2': 5,
    'Enemy2Shot': 5,
}


ENTITY_SHOT_DELAY = {
    'Player1': 500,
    'Enemy1': 400,
    'Enemy2': 300,
}

#EVENTS
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

SPAWN_TIME = 2000

TIMEOUT_STEP = 200 #MILISSEGUNDOS
TIMEOUT_LEVEL = 45000 #MILISSEGUNDOS



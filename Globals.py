import pygame
from PlayerTop import playerTop
from PlayerBottom import playerBottom
from BlocksTop import blocksTop 
from Window import Window


clock = pygame.time.Clock()
window = Window()
playerTop = playerTop()
playerBottom = playerBottom()
blocksTop = blocksTop()
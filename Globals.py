import pygame
from Player import Player

from Blocks import Blocks 
from Window import Window


clock = pygame.time.Clock()
window = Window()
player = Player(200, 200)
player2 = Player(200, 230)	
blocks = Blocks()
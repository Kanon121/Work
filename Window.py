import pygame
class Window:
    def CreateWindow(self, height, width):
        self.size = width, height 
        self.screen = pygame.display.set_mode(self.size)
    def RenderWindow(self, color):
        if color == "black":
            color = 0,0,0
        if color == "red":
            color = 225,0,0
        if color == "white":
        	color = 255,255,255
        if color == "blue":
        	color = 0,0,255
        if color == "green":
        	color = 0, 255, 0
        self.screen.fill(color)
        
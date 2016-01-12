###
Made by Kanon 
Challenge on /r/pygame
https://www.reddit.com/r/pygame/comments/40mdi8/challenge_color_picker/
###


import sys
import pygame
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("monospace", 20)
black = 0,0,0
running = True 
all_rects = []

NAME_TO_RGBA = pygame.color.THECOLORS
RGBA_TO_NAME = {}
for name, rgb in NAME_TO_RGBA.items():
    if rgb in RGBA_TO_NAME:
        RGBA_TO_NAME[rgb].append(name)
    else:
        RGBA_TO_NAME[rgb] = [name]
        

def DrawWindow():
    pygame.display.flip()
    screen.fill(black)
 

class Rect():
    def __init__(self,name, color, x, y):
        self.rect = pygame.Rect(10,10,10,10)
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.color = color
        all_rects.append(self)
    def Draw(self):
        pygame.draw.rect(screen, (self.color), self.rect)


class ColorPicker():
    def __init__(self):
        self.colors = NAME_TO_RGBA
        self.gridX = 25
        self.MakeGrid()
    def MakeGrid(self):
        x, y = 75, 100
        i = 0
        for name, rgba in self.colors.iteritems():
            rect = Rect(name, rgba, x, y)
            x += 10
            i += 1
            if i == 25:
                i = 0
                y += 10
                x = 75
            
            
            
ColorPicker() 
name_label = font.render("", 1, (255,255,255))
color_label = font.render("", 1, (255,255,255))
while running:
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                pos = pygame.mouse.get_pos()
                for rect in all_rects:
                    if rect.rect.collidepoint(pos):
                        name_label = font.render(rect.name, 1, (255,255,255))
                        color_label = font.render(str(rect.color), 1, (255,255,255))
    screen.blit(name_label, (100, 20))
    screen.blit(color_label, (100, 40))      
    for rect in all_rects:
        rect.Draw()
    DrawWindow()

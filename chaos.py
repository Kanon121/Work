import random
import pygame

all_dots = []
placed = []
pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0, 0, 0)
yellow = (255,255,0)
clock = pygame.time.Clock()

def DrawWindow():
    screen.fill(black)
	
class Main(): 
	def __init__(self, x, y, color, id=10):
		self.rect = pygame.Rect(2, 2, 2, 2)
		self.rect.x = int(x)
		self.rect.y = int(y) 
		self.id = dots
		self.color = color
		if self.id <= 3:
			all_dots.append(self)
		

tdistance = 0.5
dots = 3
while dots > 0:
	print("{} dots left to place.").format(dots)
	x = raw_input("Dot x: ")
	y = raw_input("Dot y: ")
	Main(x, y, red, dots)
	dots -= 1

startx = int(raw_input("Start x: "))
starty = int(raw_input("Start y: "))
Main(startx, starty, blue, 0)
simulating = True
lastpos = [startx, starty]
place = 5000
while simulating:
	choice = random.randint(0, 30)
	chosen = None
	if choice >= 0 and choice <= 10:
		choice = 1
	if choice > 10 and choice <= 20:
		choice = 2
	if choice > 20 and choice <= 30:
		choice = 3
	for dot in all_dots:
		if dot.id == choice:
			chosen = dot
			
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			simulating = False

	if place > 0:
		x = ((chosen.rect.x + int(lastpos[0]))/ 2)
		y = ((chosen.rect.y + int(lastpos[1]))/ 2)
		Main(x, y, white)
		place -= 1

	lastpos[0] = x
	lastpos[1] = y
	

	for dot in all_dots:
		pygame.draw.rect(screen, (dot.color), dot.rect)
	for dot in placed:
		pygame.draw.rect(screen, (dot.color), dot.rect)
		
	pygame.display.flip()
	DrawWindow()
import pygame 
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
black = 0,0,0
clock = pygame.time.Clock()

def DrawWindow():
	screen.fill(black)


holdingM1 = False

def MakeRect(sx, sy, ex, ey):
	x = sx
	y = sy
	l = ex - sx
	w = ey - sy
	RectMaker(x, y, l, w)
	
	
rects = []


class RectMaker():
	def __init__(self, sx, sy, l ,w):
		self.rect = pygame.Rect(sx, sy, l, w)

		rects.append(self)
	def Draw(self):
		pygame.draw.rect(screen, (100,100,100), self.rect)
	

startX, startY,endX, endY = 0, 0, 0, 0
holding = False
playing = True
while playing:
	clock.tick(30)
	key = pygame.key.get_pressed()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			playing = False

		if not holding:
			if e.type == pygame.MOUSEBUTTONDOWN:
				startX, startY = pygame.mouse.get_pos()
				holding = True
				
				
		if e.type == pygame.MOUSEBUTTONUP:
			if e.button == 1:
				holding = False
				endX, endY = pygame.mouse.get_pos()
				MakeRect(startX, startY, endX, endY)
				
				
		if key[pygame.K_x]:
			del rects[-1]
	
	
	for r in rects:
		r.Draw()
		
	pygame.display.flip()
	DrawWindow()

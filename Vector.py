import pygame
import math 
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
black = 0,0,0
clock = pygame.time.Clock()

def DrawWindow():
	screen.fill(black)

bullets = []
class Bullet():
	def __init__(self, x, y):
		self.rect = pygame.Rect(10, 10, 10, 10)
		self.rect.x = 150
		self.rect.y = 150
		self.startX = 150
		self.startY = 150
		self.posX = 150
		self.posY = 150
		self.speed = 2
		self.destX = x
		self.destY = y
		bullets.append(self)

	def Shoot(self):

		diff = (self.startX - self.destX, self.startY - self.destY)
		distance = math.sqrt(diff[0]**2 + diff[1]**2)
		diff_norm = (self.speed * (diff[0] / distance), self.speed * (diff[1] / distance))
		self.posX -= diff_norm[0]
		self.posY -= diff_norm[1]
		self.rect.x = int(self.posX)
		self.rect.y = int(self.posY)
		
	def Draw(self):
		for b in bullets:
			pygame.draw.rect(screen, (100,100,100), b.rect)
	
		
		
playing = True
while playing:
	clock.tick(30)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			playing = False
		if e.type == pygame.MOUSEBUTTONDOWN:
			if e.button == 1:
				print "click"
				x, y = pygame.mouse.get_pos()
				b = Bullet(x,y)
		
	for b in bullets:
		b.Shoot()
		b.Draw()
	pygame.display.flip()
	DrawWindow()

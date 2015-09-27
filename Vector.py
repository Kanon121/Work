import pygame
import math 
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
black = 0,0,0
clock = pygame.time.Clock()

def DrawWindow():
	screen.fill(black)

	
class Guy():
	def __init__(self):
		self.rect = pygame.Rect(20,20,20,20)
		self.rect.x = 150
		self.rect.y = 150
		
	def Move(self, e):
		if e == "up":
			self.rect.y -= 5
		if e == "down":
			self.rect.y += 5
		if e == "right":
			self.rect.x += 5
		if e == "left":
			self.rect.x -= 5
	def Update(self):
		pygame.draw.rect(screen, (0,100,0), self.rect)
		
guy = Guy()
	
	
bullets = []
class Bullet():
	def __init__(self, x, y):
		self.rect = pygame.Rect(2, 2, 2, 2)
		self.rect.x = guy.rect.x + 10
		self.rect.y = guy.rect.y + 10
		self.startX = guy.rect.x + 10
		self.startY = guy.rect.y + 10
		self.posX = guy.rect.x + 10
		self.posY = guy.rect.y + 10
		self.speed = 15
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
	key = pygame.key.get_pressed()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			playing = False

		if e.type == pygame.MOUSEBUTTONDOWN:
			if e.button == 1:
				x, y = pygame.mouse.get_pos()
				b = Bullet(x,y)
	if key[pygame.K_w]:
		guy.Move("up")
	if key[pygame.K_a]:
		guy.Move("left")
	if key[pygame.K_s]:
		guy.Move("down")
	if key[pygame.K_d]:
		guy.Move("right")
	guy.Update()
	for b in bullets:
		b.Shoot()
		b.Draw()
	pygame.display.flip()
	DrawWindow()

import pygame
clock = pygame.time.Clock()
class Player():
	def __init__(self):
		self.playing = True
		self.player = pygame.Rect(200, 200, 10, 10)
		self.ascending = False
		self.descending = False
		self.baseJumpHeight = 15
		
		self.jumpHeight = self.baseJumpHeight
		self.jumpSpeed = 0
		self.fallSpeed = 0
		
	def Update(self):
		for e in pygame.event.get(): 
			if e.type == pygame.QUIT:
				self.playing = False
			if e.type == pygame.KEYDOWN:
				if not self.descending:
					if e.key == pygame.K_UP:
						self.PlayerAscend()
						
	def Collide(self, floor, block):
		if self.player.colliderect(floor):
			self.player.bottom = floor.top
			self.descending = False
			self.ascending = False
		for blocks in block:
			if self.player.colliderect(blocks):
				self.playing = False

	def Render(self, screen):
		pygame.draw.rect(screen, (255,0,0), self.player)
		pygame.display.flip()

	def PlayerAscend(self):
		self.ascending = True

	def PlayerJump(self, ascending, jumpHeight):
		
		if jumpHeight != 0:
			if ascending == True:
				self.jumpSpeed += 0.4
				self.player.y -= 1 + self.jumpSpeed
				self.jumpHeight -= 1
				
		else:
			self.ascending = False
			self.descending = True
			self.jumpHeight = self.baseJumpHeight
			self.jumpSpeed = 0
	
	def Gravity(self):
		if self.descending:
			self.fallSpeed += 0.4
			self.player.y += 1 + self.fallSpeed
		else: 
			self.descending = False
			self.fallSpeed = 0
		
		
		
		
    
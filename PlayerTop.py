import pygame
clock = pygame.time.Clock()
import time
class playerTop():
	def __init__(self):
		self.playing = True
		self.playerTop = pygame.Rect(200, 200, 10, 10)
		self.ascending = False
		self.descending = False
		self.baseJumpHeight = 20
		self.points = 0
		self.jumpHeight = self.baseJumpHeight
		self.jumpSpeed = 1
		self.fallSpeed = 1
		
	def Update(self):
		for e in pygame.event.get(): 
			if e.type == pygame.QUIT:
				self.playing = False
			if e.type == pygame.KEYDOWN:
				if not self.descending and not self.ascending:
					if e.key == pygame.K_UP:
						self.playerTopAscend()
						sound = pygame.mixer.Sound("jump.wav")
						sound.play()
					#if e.key == pygame.K_DOWN:
					#	playerBottom.playerBottomAscend()
					#	sound = pygame.mixer.Sound("jump.wav")
					#	sound.play()
	def Collide(self, floor, block):
		if self.playerTop.colliderect(floor):
			self.playerTop.bottom = floor.top
			self.descending = False
			self.ascending = False
		for blocks in block:
			if self.playerTop.colliderect(blocks):
				sound = pygame.mixer.Sound("scream.wav")
				sound.play()
				time.sleep(sound.get_length())
				self.playing = False

	def Render(self, screen):
		pygame.draw.rect(screen, (255,0,0), self.playerTop)
		

	def playerTopAscend(self):
		self.ascending = True

	def playerTopJump(self, ascending, jumpHeight):

		if jumpHeight != 0:
			if ascending == True:

				self.jumpSpeed += 0.2
				self.playerTop.y -= 1 + self.jumpSpeed
				self.jumpHeight -= 1
				
		else:
			self.ascending = False
			self.descending = True
			self.jumpHeight = self.baseJumpHeight
			self.jumpSpeed = 0
	
	def Gravity(self):
		if self.descending:
			self.fallSpeed += 0.2
			self.playerTop.y += 1 + self.fallSpeed
		else: 
			self.descending = False
			self.fallSpeed = 0
		
		
		
		
    
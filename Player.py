import pygame
clock = pygame.time.Clock()
import time
class Player():
	def __init__(self):
		self.playing = True
		self.player = pygame.Rect(200, 200, 10, 10)
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
						self.PlayerAscend()
						sound = pygame.mixer.Sound("jump.wav")
						sound.play()
						
	def Collide(self, floor, block):
		if self.player.colliderect(floor):
			self.player.bottom = floor.top
			self.descending = False
			self.ascending = False
		for blocks in block:
			if self.player.colliderect(blocks):
				sound = pygame.mixer.Sound("scream.wav")
				sound.play()
				time.sleep(sound.get_length())
				self.playing = False

	def Render(self, screen):
		pygame.draw.rect(screen, (255,0,0), self.player)
		pygame.display.flip()

	def PlayerAscend(self):
		self.ascending = True

	def PlayerJump(self, ascending, jumpHeight):

		if jumpHeight != 0:
			if ascending == True:

				self.jumpSpeed += 0.2
				self.player.y -= 1 + self.jumpSpeed
				self.jumpHeight -= 1
				
		else:
			self.ascending = False
			self.descending = True
			self.jumpHeight = self.baseJumpHeight
			self.jumpSpeed = 0
	
	def Gravity(self):
		if self.descending:
			self.fallSpeed += 0.2
			self.player.y += 1 + self.fallSpeed
		else: 
			self.descending = False
			self.fallSpeed = 0
		
		
		
		
    
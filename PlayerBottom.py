import pygame 
class playerBottom():
	def __init__(self):
		self.playerBottom = pygame.Rect(200, 230, 10, 10)
		self.ascending = False
		self.descending = False
		self.baseJumpHeight = 20
		self.points = 0
		self.jumpHeight = self.baseJumpHeight
		self.jumpSpeed = 1
		self.fallSpeed = 1
	


						
	
	def Collide(self, floor, block):
		if self.playerBottom.colliderect(floor):
			self.playerBottom.top = floor.bottom
			self.descending = False
			self.ascending = False
		for blocks in block:
			if self.playerBottom.colliderect(blocks):
				sound = pygame.mixer.Sound("scream.wav")
				sound.play()
				time.sleep(sound.get_length())
				self.playing = False
				
	def Render(self, screen):
		pygame.draw.rect(screen, (255,0,0), self.playerBottom)
	
	def playerBottomAscend(self):
		self.ascending = True
		
	def playerBottomJump(self, ascending, jumpHeight):
		if jumpHeight != 0:
			if ascending == True:

				self.jumpSpeed += 0.2
				self.playerTop.y += 1 + self.jumpSpeed
				self.jumpHeight -= 1
				
		else:
			self.ascending = False
			self.descending = True
			self.jumpHeight = self.baseJumpHeight
			self.jumpSpeed = 0
	
	def Gravity(self):
		if self.descending:
			self.fallSpeed += 0.2
			self.playerTop.y -= 1 + self.fallSpeed
		else: 
			self.descending = False
			self.fallSpeed = 0			
			
			
			
			
			
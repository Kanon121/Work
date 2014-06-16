import pygame
clock = pygame.time.Clock()
import time
class Player():
	def __init__(self, x, y):
		self.playing = True
		self.rect = pygame.Rect(x, y, 10, 10)
		self.ascending = False
		self.descending = False
		self.baseJumpHeight = 20
		self.points = 0
		self.jumpHeight = self.baseJumpHeight
		self.jumpSpeed = 1
		self.fallSpeed = 1
		
	def Update(self, e, player):
			if e.type == pygame.KEYDOWN:
				if not self.descending and not self.ascending:
					if e.key == pygame.K_UP:
						self.checkPlayerJump("up", player)
						sound = pygame.mixer.Sound("jump.wav")
						sound.play()

					
					
						
	def Collide(self, floor, block, player):
		if player.rect.colliderect(floor):
			player.rect.bottom = floor.top
			self.descending = False
			self.ascending = False

		
		for blocks in block:
			if player.rect.colliderect(blocks):
				sound = pygame.mixer.Sound("scream.wav")
				sound.play()
				time.sleep(sound.get_length())
				self.playing = False

	def playerJump(self, dir):
		pass
	
	
	
	def Render(self, screen, player, player2):
		pygame.draw.rect(screen, (255,0,0), player)
		pygame.draw.rect(screen, (255,0,0), player2)
		pygame.display.flip()




	def checkPlayerJump(self, direction, player):
		if direction == "up":
			self.ascending = True
			while (self.jumpHeight != 0):
				if self.ascending == True:
					self.jumpSpeed += 0.2
					player.rect.y -= 1 + self.jumpSpeed
					self.jumpHeight -= 1
			else:
				self.ascending = False
				self.descending = True
				self.jumpHeight = self.baseJumpHeight
				self.jumpSpeed = 0
	
	
	def Gravity(self, player):
		if self.descending:
			self.fallSpeed += 0.2
			player.rect.y += 1 + self.fallSpeed
		else: 
			self.descending = False
			self.fallSpeed = 0
		

				

	
"""				
def Jump(self, direction):
	
	if direction == 'up':
		jumpSpeed = 
		jumpHeight = 
	else:
		jumpSpeed = 
		jumpHeight = 
	
	
	
p1 = Player()
p2 = Player()

p1.Jump('up')
p2.Jump('down')
				
"""
				
				
				
		
		
    
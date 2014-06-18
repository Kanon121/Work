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
		self.atPeak = 4
		
	def Update(self, e, player):
			if e.type == pygame.KEYDOWN:
				if not self.descending and not self.ascending:
					if e.key == pygame.K_UP:
						player.ascending = True
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


	
	
	
	def Render(self, screen, player, player2):
		pygame.draw.rect(screen, (255,0,0), player)
		pygame.draw.rect(screen, (255,0,0), player2)
		pygame.display.flip()




	def checkPlayerJump(self, player):	
		if self.ascending == True:
			if self.jumpHeight != 0:
				print player.rect.y
				self.jumpSpeed += 0.02
				player.rect.y -= 1 + self.jumpSpeed
				self.jumpHeight -= 1
			else:
				if self.atPeak != 0:
					player.rect.y += 0
					self.atPeak -= 1
				else:
					self.ascending = False
					self.descending = True
					self.jumpHeight = self.baseJumpHeight
					self.jumpSpeed = 1
					self.atPeak = 4
	
	
	def Gravity(self, player):
		if self.descending:
			self.fallSpeed += 0.2
			player.rect.y += 1 + self.fallSpeed
		else: 
			self.descending = False
			self.fallSpeed = 1
		

				

	
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
				
				
				
		
		
    
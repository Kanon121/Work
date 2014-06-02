import pygame
import random
class Blocks():
	
		def __init__(self):
			self.allBlocks = []
			self.H = random.randint(2, 10)
			self.L = random.randint(2, 10)
			self.smallBlock = pygame.Rect(400, 200, self.H, self.L)
			self.medBlock = pygame.Rect(400, 200, 10, 20)
			self.allBlocks.append(self.smallBlock)
			self.newBlockTime = 200
		
		def PlaceFloor(self):
			self.floor = pygame.Rect(0, 210, 400, 20)
		def DrawFloor(self, screen):
			pygame.draw.rect(screen, (0,0,0), self.floor)

			
		def MoveBlock(self):
			for block in self.allBlocks:
				block.bottom = self.floor.top
				block.x -= 1
				if block.right <= 0:
					self.allBlocks.remove(block)

		
		def DrawBlock(self, screen):
			for block in self.allBlocks:
				pygame.draw.rect(screen, (0,0,0), block)
				
		def NewBlock(self):
			self.newBlockTime -= 1
			if self.newBlockTime == 0:
				self.H = random.randint(2, 10)
				self.L = random.randint(2, 10)			
				self.allBlocks.append(self.smallBlock)
				self.newBlockTime = 200


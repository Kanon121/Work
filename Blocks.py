import pygame
import random
class Blocks():
	
		def __init__(self):
			self.allBlocks = []
			self.madeBlocks = []
			self.newBlockTime = 200
			self.oldBlockTime = 200
			self.appendBlocks()
			
			
		def appendBlocks(self):
			smallBlock = 10, 10
			medBlock = 20, 10
			largeBlock = 14, 24
			self.madeBlocks.append(smallBlock)
			self.madeBlocks.append(medBlock)
			self.madeBlocks.append(largeBlock)
		
		
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

				x = random.randint(0,2)
				self.allBlocks.append(pygame.Rect(400, 200, self.madeBlocks[x]))
				
				
				self.oldBlockTime = self.oldBlockTime - 10
				self.newBlockTime = self.oldBlockTime - 10
				print self.oldBlockTime


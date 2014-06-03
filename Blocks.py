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
			largeBlock = 12, 20
			floatingBlock = 10, 10
			self.madeBlocks.append(floatingBlock)
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

				x = random.randint(0,3)
				randBlock = self.madeBlocks[x]
				self.allBlocks.append(pygame.Rect(400, 200, randBlock[0], randBlock[1]))
				
				if self.oldBlockTime >= 40:
					self.oldBlockTime = self.oldBlockTime - 10
					self.newBlockTime = self.oldBlockTime - 10
				else:
					self.oldBlockTime = 40
					self.newBlockTime = 40


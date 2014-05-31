import pygame
class Blocks():
	
		def __init__(self):
			self.blocks = []
			self.smallBlock = pygame.Rect(400, 200, 10, 10)
			self.medBlock = pygame.Rect(400, 200, 10, 20)
			self.blocks.append(self.smallBlock)
			self.newBlockTime = 200
		
		def PlaceFloor(self):
			self.floor = pygame.Rect(0, 210, 400, 20)
		def DrawFloor(self, screen):
			pygame.draw.rect(screen, (0,0,0), self.floor)

			
		def MoveBlock(self):
			for block in self.blocks:
				block.bottom = self.floor.top
				block.x -= 1
				if block.right <= 0:
					block.x = 400
		
		def DrawBlock(self, screen):
			for block in self.blocks:
				pygame.draw.rect(screen, (0,0,0), block)
				
		def NewBlock(self):
			self.newBlockTime -= 1
			if self.newBlockTime == 0:
				self.blocks.append(self.smallBlock)
				self.newBlockTime = 200
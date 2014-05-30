import pygame

class Player():
    def __init__(self):
		self.playing = True
		self.player = pygame.Rect(200, 200, 10, 10)
		self.jumping = False
    
    def Update(self):
		for e in pygame.event.get(): 
			if e.type == pygame.QUIT:
				self.playing = False
			if e.type == pygame.KEYDOWN:
				if not self.jumping:
					if e.key == pygame.K_UP:
						self.PlayerJump()
						
					
    def Render(self, screen):
    	pygame.draw.rect(screen, (255,0,0), self.player)
    	pygame.display.flip()
    	
    def PlayerJump(self):
		self.jumping = True
    		
    
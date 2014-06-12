import Globals as globals 
globals.pygame.init()
globals.pygame.mixer.init()
globals.window.CreateWindow(400, 400)
globals.blocks.PlaceFloor()

while (globals.player.playing):
	globals.clock.tick(80)
	globals.blocks.DrawFloor(globals.window.screen)
	globals.player.Collide(globals.blocks.floor, globals.blocks.allBlocks, globals.player)
	
	for e in globals.pygame.event.get(): 
		if e.type == globals.pygame.QUIT:
			globals.player.playing = False
		else:
			globals.player.Update(e, globals.player)
	        
	globals.player.Gravity(globals.player)
	globals.blocks.NewBlock()
	globals.blocks.MoveBlock()
	globals.blocks.DrawBlock(globals.window.screen)
	globals.player.Render(globals.window.screen, globals.player, globals.player2)
	globals.window.RenderWindow("white")
	
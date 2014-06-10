import Globals as globals 
globals.pygame.init()
globals.pygame.mixer.init()
globals.window.CreateWindow(400, 400)
globals.blocksTop.PlaceFloor()

while (globals.playerTop.playing):
	globals.clock.tick(80)
	
	globals.blocksTop.DrawFloor(globals.window.screen)
	
	globals.playerTop.Collide(globals.blocksTop.floor, globals.blocksTop.allBlocks)
	globals.playerTop.Gravity()
	globals.playerTop.Update()
	
	#Change playerBottom.collide block params
	
	globals.playerBottom.Collide(globals.blocksTop.floor, globals.blocksTop.allBlocks)
	globals.playerBottom.Gravity()
	#globals.playerBottom.Update(globals.playerTop.playing)
	
	
	globals.blocksTop.NewBlock()
	globals.blocksTop.MoveBlock()
	globals.blocksTop.DrawBlock(globals.window.screen)
	
	globals.playerTop.playerTopJump(globals.playerTop.ascending, globals.playerTop.jumpHeight)
	globals.playerTop.Render(globals.window.screen)
	
	globals.playerBottom.playerBottomJump(globals.playerBottom.ascending, globals.playerBottom.jumpHeight)
	globals.playerBottom.Render(globals.window.screen)
	
	globals.pygame.display.flip()
	globals.window.RenderWindow("white")
	
import Globals as globals 
globals.pygame.init()
globals.pygame.mixer.init()
globals.window.CreateWindow(400, 400)
globals.blocks.PlaceFloor()

while (globals.playerTop.playing):
	globals.clock.tick(80)
	globals.blocks.DrawFloor(globals.window.screen)
	globals.playerTop.Collide(globals.blocks.floor, globals.blocks.allBlocks)
	globals.playerTop.Gravity()
	globals.playerTop.Update()
	globals.blocks.NewBlock()
	globals.blocks.MoveBlock()
	globals.blocks.DrawBlock(globals.window.screen)
	globals.playerTop.playerTopJump(globals.playerTop.ascending, globals.playerTop.jumpHeight)
	globals.playerTop.Render(globals.window.screen)
	globals.window.RenderWindow("white")
	
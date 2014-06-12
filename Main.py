import Globals as globals 
globals.pygame.init()
globals.pygame.mixer.init()
globals.window.CreateWindow(400, 400)
globals.blocks.PlaceFloor()

while (globals.player.playing):
	globals.clock.tick(80)
	globals.blocks.DrawFloor(globals.window.screen)
	globals.player.Collide(globals.blocks.floor, globals.blocks.allBlocks, globals.blocks.allBlocks2)
	globals.player.Gravity()
	globals.player.Update()
	globals.blocks.NewBlock()
	globals.blocks.MoveBlock()
	globals.blocks.DrawBlock(globals.window.screen)
	globals.player.playerJump(globals.player.ascending, globals.player.jumpHeight)
	globals.player.Render(globals.window.screen)
	globals.window.RenderWindow("white")
	
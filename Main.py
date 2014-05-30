import Globals as globals 
globals.pygame.init()
globals.window.CreateWindow(400, 400)


while (globals.player.playing):
	globals.clock.tick(20)
	globals.player.Update()
	globals.player.Render(globals.window.screen)
	globals.window.RenderWindow("white")

import pygame
size = width, height = 400, 400
screen = pygame.display.set_mode(size)

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0, 0, 0)
yellow = (255,255,0)
clock = pygame.time.Clock()

 
def DrawWindow():
    screen.fill(black)
    
ADJACENTS = [
(-1, -1),
(-1, 0),
(-1, 1),
(0, -1),
(0, 1),
(1, -1),
(1, 0),
(1, 1)
]
    
    
    
# -#############################- #

class Finding():
    def __init__(self, start_block, end_block, blocks):
        self.start = start_block
        self.current = self.start
        self.end = end_block
        self.open_list = [self.current]
        self.closed_list = []
        self.blocks = blocks
        self.walls = []
        self.tiles = []
        self.path = []
        self.lowestFx = None
        self.found_end = False
        self.parseWalls(self.blocks)
        self.getNeighbors()
        self.beginSearch()
 
        
    def parseWalls(self, blocks):
        for block in blocks:
            if block.is_wall == True:
                self.walls.append(block)
            else:
                self.tiles.append(block)
    
    def getNeighbors(self):
        

        for (i, j) in ADJACENTS:
            check = (self.current.location[0]+i, 
                self.current.location[1]+j)
            
            for block in self.blocks:
                if check == block.location:
                    check = block

                    

                    



            if check in self.open_list:
                oldgx = check.gx
                
                #check.gx = self.current.parent.gx + 10
                Sx = self.current.tile_x
                Sy = self.current.tile_y

                if check.tile_x != Sx and check.tile_y != Sy:
                    check.gx = self.current.parent.gx + 14
                if check.tile_x != Sx and check.tile_y == Sy:
                    check.gx = self.current.parent.gx + 10
                if check.tile_x != Sy and check.tile_x == Sx:
                    check.gx = self.current.parent.gx + 10
        
                if check.gx < oldgx:
                    check.parent = self.current

            
            
            if check not in self.walls and check not in self.closed_list:
                if check not in self.open_list:
                    self.open_list.append(check)
                    check.parent = self.current
                
            if self.current in self.open_list:
                self.open_list.remove(self.current)
            
            self.closed_list.append(self.current)
            

    def getCost(self, block):
        x = abs(block.tile_x - self.end.tile_x)
        y = abs(block.tile_y - self.end.tile_y)
        x,y = x * 10, y * 10
        
        block.hx = x + y

        Sx = block.tile_x
        Sy = block.tile_y
        if self.current.tile_x != Sx and self.current.tile_y != Sy:
            block.gx = block.parent.gx + 14
        if self.current.tile_x != Sx and self.current.tile_y == Sy:
            block.gx = block.parent.gx + 10
        if self.current.tile_x != Sy and self.current.tile_x == Sx:
            block.gx = block.parent.gx + 10

        block.fx = block.hx + block.gx


    def beginSearch(self):
        fx = 10000
        for block in self.open_list:
            self.getCost(block)
            if block.fx < fx:
                self.lowestFx = block
                fx = self.lowestFx.fx
                
        

        
        
        
        self.current = self.lowestFx

        
        for cells in self.open_list:
            cells.color = (200,200,200)
        for cells in self.closed_list:
            cells.color = yellow


        if self.end in self.closed_list:
            previous = self.end
            while self.start not in self.path:
                parent = previous.parent
                previous = parent
                self.path.append(parent)
        else:
            self.getNeighbors()
# -#############################- #




class Tiles():
    def __init__(self,x,y):
        self.rect = pygame.Rect(20,20,20,20)
        self.rect.x = x
        self.rect.y = y
        self.color = white
        tiledata.all_tiles.append(self)
        self.tile_x = x / 20
        self.tile_y = y / 20
        self.location = (self.tile_x, self.tile_y)
        self.gx = 0
        self.hx = 0
        self.fx = 0
        self.parent = None
        self.is_wall = False
        self.FindEdge()
        
        
    def FindEdge(self):
        if self.tile_x == 0 or self.tile_x == 19:
            self.is_wall = True
        if self.tile_y == 0 or self.tile_y == 19:
            self.is_wall = True
        
        
class TileData():
    def __init__(self):
        self.all_tiles = []
        self.length_x = width / 20
        self.tiles_for_x = self.length_x
        self.length_y = height / 20
        self.tiles_for_y = self.length_y
        self.tiles_for_append = self.length_x * self.length_y
        



        
def CreateGrid():
    x, y = 0, 0
    while  tiledata.tiles_for_append != 0:

        while  tiledata.tiles_for_x != 0:
            tile = Tiles(x,y)
            x += 20
            tiledata.tiles_for_x -= 1
        y += 20
        x = 0
        tiledata.tiles_for_y -= 1
        if tiledata.tiles_for_y != 0:
            tiledata.tiles_for_x = tiledata.length_x
        else:
            break

def DrawLines():
    x, y = 0, 0
    xlinesleft = 20
    ylinesleft = 20
    while xlinesleft != 0:
        pygame.draw.line(screen, black, (x,0), (x,400))
        x += 20
        xlinesleft -= 1
    while ylinesleft != 0:
        pygame.draw.line(screen, black, (0,y), (400, y))
        y += 20
        ylinesleft -= 1

running = True
tiledata = TileData()
CreateGrid()
started = False
startcell = None
endcell = None
frames = 0
while running:
    clock.tick(60)

    pos = pygame.mouse.get_pos()
    cellpos = (pos[0] /20, pos[1] / 20)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                for cell in tiledata.all_tiles:
                    if cellpos == cell.location:
                        if not startcell:
                            cell.color = green
                            startcell = cell
                            
                        else:
                            cell.color = red
                            endcell = cell
            if e.button == 2:
                for cell in tiledata.all_tiles:
                    if cell.location == cellpos:
                        cell.is_wall = True
            
            if e.button == 3:
                if not started:
                    if endcell and startcell:
                        find = Finding(startcell, endcell, tiledata.all_tiles)
                        started = True
                    else:   
                        print "Please choose start and end cells"
    if started:
        frames += 1
        if frames == 20:
            frames = 0
            find.beginSearch()
            if find.path != []:
                for cell in find.path:
                    cell.color = blue
                    if cell == startcell:
                        cell.color = green
                    if cell == endcell:
                        cell.color = red
    for cell in tiledata.all_tiles:
        pygame.draw.rect(screen, (cell.color), cell.rect)
        if cell.is_wall:
            pygame.draw.rect(screen, ((100,100,100)), cell.rect)

    DrawLines()
    pygame.display.flip()
    DrawWindow()

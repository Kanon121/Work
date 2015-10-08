import pygame
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep
import sys, math
size = width, height = 200, 200
screen = pygame.display.set_mode(size)
black = 0, 0, 0
clock = pygame.time.Clock()


def DrawWindow():
    screen.fill(black)
    
AllPlayers = []
IDUsed = []
AllBullets = []
class Player:
    def __init__(self, id):
        self.rect = pygame.Rect(10, 10, 10, 10)
        self.color = (255,255,255)
        if id == 1:
            self.color = (255,255,255)
            self.rect.x = 50
        if id == 2:
            self.color = (0,255,0)
            self.rect.x = 10
        self.id = id
        self.speed = 4
        
    def Draw(self):
        pygame.draw.rect(screen, (self.color), self.rect)

        
    def Move(self, dir):
        spx = self.speed
        spy = self.speed
        
        if dir == "up":
            dy = -spy
            dx = 0
        if dir == "down":
            dy = spy
            dx = 0
        if dir == "right":
            dx = spx
            dy = 0
        if dir == "left":
            dx = -spx
            dy = 0   
        self.rect.x += dx
        self.rect.y += dy


def AssociatePlayer(id):
    PosInList = id - 1
    player = AllPlayers[PosInList]
    return player


    
    
    
        
class Bullet():
    def __init__(self, id, x, y):
        guy = AssociatePlayer(id)
        self.rect = pygame.Rect(2, 2, 2, 2)
        self.rect.x = guy.rect.x + 5
        self.rect.y = guy.rect.y + 5
        self.startX = guy.rect.x + 5
        self.startY = guy.rect.y + 5
        self.posX = guy.rect.x + 5
        self.posY = guy.rect.y + 5
        self.speed = 15
        self.destX = x
        self.destY = y
        AllBullets.append(self)

    def Shoot(self):
        diff = (self.startX - self.destX, self.startY - self.destY)
        distance = math.sqrt(diff[0]**2 + diff[1]**2)
        diff_norm = (self.speed * (diff[0] / distance), self.speed * (diff[1] / distance))
        self.posX -= diff_norm[0]
        self.posY -= diff_norm[1]
        self.rect.x = int(self.posX)
        self.rect.y = int(self.posY)

    def Draw(self):
        for b in AllBullets:
            pygame.draw.rect(screen, (255,0,0), b.rect)
	      
def MakePlayer(id):
    if id not in IDUsed:
        guy = Player(id)
        IDUsed.append(id)
        AllPlayers.append(guy)
        
       
class Connector(ConnectionListener):
    
    def __init__(self):
        self.Connect(("localhost", 80))
        self.running = True
        self.id = 0
        self.players = 0
        
    def update(self):
        
        key = pygame.key.get_pressed()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                connector.Send({'action':'DC'})
                connection.Pump()
                self.Pump()
                self.running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                print AllPlayers
                print IDUsed
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    x, y = pygame.mouse.get_pos()
                    connector.Send({'action':'MakeBullet', 'id':self.id, 'mousepos':[x,y]})

        
        if key[pygame.K_w]:
            connector.Send({'action':'Move', 'id':self.id, 'dir':'up'})
        if key[pygame.K_a]:
            connector.Send({'action':'Move', 'id':self.id, 'dir':'left'})
        if key[pygame.K_s]:
            connector.Send({'action':'Move', 'id':self.id, 'dir':'down'})
        if key[pygame.K_d]:
            connector.Send({'action':'Move', 'id':self.id, 'dir':'right'})
            
            
        
        
        
        
        if self.players != 0:
            self.players -= 1
            connector.Send({'action':'MakePlayer', 'id':self.id})
            

            
        for p in AllPlayers:
            p.Draw()
        for b in AllBullets:
            print b
            b.Shoot()
            b.Draw()
        pygame.display.flip()
        DrawWindow()
        clock.tick(30)
    def Network_connected(self, data):
        print "CONNECTED TO SERVER"
        
        
	
    def Network(self, data):
        print data
        pass
    def Network_GetList(self, data):
        self.players = data['list']
        if self.id == 0:
            self.id = data['id']
    def Network_MakePlayer(self, data):
        id = data['id']
        MakePlayer(id)
        
    def Network_Move(self, data):
        dir = data['dir']
        for p in AllPlayers:
            if p.id == data['id']:
                p.rect.cetner = data['currpos']
                p.Move(dir)
                
    def Network_MakeBullet(self, data):
        id = data['id']
        x = data['x']
        y = data['y']
        b = Bullet(id, x, y)
                
  
connector = Connector()    
	  
while connector.running:
    connection.Pump()
    connector.Pump()
    connector.update()
 

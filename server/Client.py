import pygame
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep
import sys
size = width, height = 200, 200
screen = pygame.display.set_mode(size)
black = 0, 0, 0

def DrawWindow():
    screen.fill(black)
    
AllPlayers = []
IDUsed = []
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
        
    def Draw(self):
        pygame.draw.rect(screen, (self.color), self.rect)

        

        
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
        connection.Pump()
        self.Pump()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                connector.Send({'action':'DC'})
                connection.Pump()
                self.Pump()
                self.running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                print AllPlayers
                print IDUsed
        if self.players != 0:
            self.players -= 1
            connector.Send({'action':'MakePlayer', 'id':self.id})
        
        for p in AllPlayers:
            p.Draw()
        pygame.display.flip()
        DrawWindow()

    def Network_connected(self, data):
        print "CONNECTED TO SERVER"
        
        
	
    def Network(self, data):
        #print data
        pass
    def Network_GetList(self, data):
        self.players = data['list']
        if self.id == 0:
            self.id = data['id']
    def Network_MakePlayer(self, data):
        id = data['id']
        MakePlayer(id)
        
connector = Connector()    
 
	  
while connector.running:
    connector.update()
 

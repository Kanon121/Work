from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from time import sleep
import pygame
from time import gmtime, strftime


class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)

    def Network(self, data):
        print data
        
    def Network_DC(self, data):
        print "player disconnected"

    def Network_MakePlayer(self, data):
        num = data['id']
        self._server.MakePlayer(num)
    def Network_Move(self, data):
        num = data['id']
        dir = data['dir']
        self._server.Move(num, dir)
        
class GameServer(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)     
        self.clients = []
        self.id = 0

    def Connected(self, channel, addr):
        self.clients.append(channel)
        self.id += 1
        for c in self.clients:
            c.Send({'action': 'GetList', 'list': 1, 'id':self.id}) 
        
        print "new connection at time: " + strftime("%Y-%m-%d %H:%M:%S")
        
    def MakePlayer(self, id):
        for c in self.clients:
            
            c.Send({'action': 'MakePlayer', 'id':id})
        
    def Move(self, id, dir):
        for c in self.clients:
            c.Send({'action': 'Move', 'id':id, 'dir':dir})

mainServer = GameServer(localaddr=("localhost", 80))
print "LISTENING FOR CONNECTIONS"
while True:
    mainServer.Pump()
    sleep(0.001)

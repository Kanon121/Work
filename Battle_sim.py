from __future__ import division
import pygame
import random
import math

size = 800, 400
screen = pygame.display.set_mode(size)

bullets = []
soldiers = []  
team1 = []
team2 = []

clock = pygame.time.Clock()


def DrawWindow():
    black = 0, 0, 0
    screen.fill(black)

class Bullet():
    def __init__(self, shooter, t, dest):
        self.team = t
        self.rect = pygame.Rect(5,5,5,5)
        self.destX = dest[0]
        self.destY = dest[1]
        self.rect.x = shooter.rect.x
        self.rect.y = shooter.rect.y
        self.startX = shooter.rect.x
        self.startY = shooter.rect.y
        self.positionX = shooter.rect.x
        self.positionY = shooter.rect.y
        bullets.append(self)
        self.speed = 3
    
    def Update(self):
        diff = (self.startX - self.destX, self.startY - self.destY)
        distance = math.sqrt(diff[0]**2 + diff[1]**2)
        diff_norm = (self.speed * (diff[0] / distance), self.speed * (diff[1] / distance))
        self.positionX -= diff_norm[0]
        self.positionY -= diff_norm[1]
        self.rect.x = int(self.positionX)
        self.rect.y = int(self.positionY)

            
            
            
class Soldier():
    def __init__(self, t):
        self.team = t
        self.rect = pygame.Rect(10, 10, 10, 10)
        self.reload = random.randint(100, 500)
        self.SetPos()
        self.WalkReset()
      

    def Shoot(self, t):
        if self.team == 1:
            randomEnemy = random.randint(0, len(team2))
            if randomEnemy != 0:
                randomEnemy -= 1
            chosen = team2[randomEnemy]
            destX = chosen.rect.x
            destY = chosen.rect.y
        if self.team == 2:
            randomEnemy = random.randint(0, len(team1))
            if randomEnemy != 0:
                randomEnemy -= 1
            chosen = team1[randomEnemy]
            destX = chosen.rect.x
            destY = chosen.rect.y
            
        dest = [destX, destY]
        b = Bullet(self, t, dest)
        
      
    def WalkReset(self):
        self.walkCooldown = random.randint(10, 100)
    
    
    def SetPos(self):
        if self.team == 1:
            self.color = (255,255,255)
            ranX = random.randint(10 , 60)
            self.rect.x = ranX
            ranY = random.randint(10, 390)
            self.rect.y = ranY
            
            
        elif self.team == 2:
            self.color = (0,0,255)
            ranY = random.randint(10, 390)
            self.rect.y = ranY
            ranX = random.randint(740, 790)
            self.rect.x = ranX
 


men = 30
while men > 0:
    if men > 16:
        team = 1
    else:
        team = 2
    dude = Soldier(team)
    soldiers.append(dude)
    men -= 1


playing = True
while playing:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            playing = False
    
    
    for s in soldiers:
        if s not in team1 and s not in team2:
            if s.team == 1:
                team1.append(s)
            if s.team == 2:
                team2.append(s)
        
        
        
        
        s.reload -= 1
        s.walkCooldown -= 1
        if s.walkCooldown <= 0:
            s.WalkReset()
            randMove = random.randint(1,3)
            randDistance = random.randint(8,13)
            if s.team == 1:
                if randMove == 1:
                    s.rect.x += randDistance
                if randMove == 2:
                    s.rect.y -= randDistance
                if randMove == 3:
                    s.rect.y += randDistance
            if s.team == 2:
                if randMove == 1:
                    s.rect.x -= randDistance
                if randMove == 2:
                    s.rect.y += randDistance
                if randMove == 3:
                    s.rect.y -= randDistance
      
        if s.reload <= 0:
            s.Shoot(s.team)
            s.reload = random.randint(500,1000)

            
        
            
        pygame.draw.rect(screen, (s.color), s.rect)
    

    
    
    for b in bullets:
        b.Update()
        for s in soldiers:
            if b.rect.colliderect(s.rect):
                if b.team != s.team:
                    if b in bullets:
                        bullets.remove(b)
                    soldiers.remove(s)
                    if s.team == 1:
                        team1.remove(s)
                    if s.team == 2:
                        team2.remove(s)
   
        
        pygame.draw.rect(screen, (255,255,255), b.rect)
    if team1 == [] or team2 == []:
        print "Game Over!"
        playing = False
    
    
    
    clock.tick(60)
    pygame.display.flip()
    DrawWindow()

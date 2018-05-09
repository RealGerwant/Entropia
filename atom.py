import random

class Atom:
    x=1
    y=1
    dx=1
    dy=1

    def RandomVelocity(self,R):
        self.dx = random.randrange(-R,R+1)
        self.dy = random.randrange(-R,R+1)

    def SetPosition(self,x,y):
        self.x =x
        self.y =y

    def MakeMove(self,DeltaTime,Boundries,Radius):
        if (self.x + self.dx * DeltaTime + Radius> Boundries and self.dx > 0):
            self.dx = -self.dx
        if (self.x + self.dx * DeltaTime - Radius< 0 and self.dx <0):
            self.dx = - self.dx
        if (self.y + self.dy * DeltaTime + Radius> Boundries and self.dy > 0):
            self.dy = -self.dy
        if (self.y + self.dy * DeltaTime - Radius< 0 and self.dy <0):
            self.dy = - self.dy
        self.x +=self.dx*DeltaTime
        self.y +=self.dy*DeltaTime


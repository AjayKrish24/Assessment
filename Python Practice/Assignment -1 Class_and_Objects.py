import math
class point:
    count = 0
    def __new__(cls, *args, **kwargs):
        cls.count += 1 
        if(cls.count>5):
            raise TypeError("More than 5 objects are created")
        else:
            return object.__new__(cls)
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b
    def distance(self,p):
        d=math.sqrt((p.x-self.x)**2 + (p.y-self.y)**2)
        return d
    def midpoint(self,p):
        p.x=(self.x+p.x)/2
        p.y=(self.y+p.y)/2
        return p
p=point()
p1=point(4,5)
p2=point(7,9)
p3=point()
p4=point()
p5=point()
print(p1.distance(p))
print(p1.distance(p2))
p=p1.midpoint(p2)
print(p.x,",",p.y)
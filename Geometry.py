import Tkinter as tk
from math import sqrt

INFINITY = 'infinity'
graphWidth=500
graphHeight=500
root = tk.Tk()
graph = tk.Canvas(root, width=graphWidth, height=graphHeight)
graph.pack()

def reciprocal(num):
    return 1/num

class point:
    def __init__(self, (x, y), size=0, color='red'):
        self.x = float(x)
        self.y = float(y)

        self.size = size

        self.color = color #The color of the image

        self.shownX = self.x+graphWidth/2
        self.shownY = graphHeight-(self.y+graphHeight/2)

    def __neg__(self):
        return point((-self.x, -self.y))

    def __abs__(self):
        return point((abs(self.x), abs(self.y)))

    def draw(self):
        graph.create_oval(self.shownX-self.size/2, self.shownY+self.size/2, self.shownX+self.size/2, self.shownY-self.size/2, fill=self.color, outline=self.color)

class NonePoint(None):
    def __init__(*args):
        self.x = None
        self.y = None

        self.size = None

        self.color = None #The color of the image

        self.shownX = None
        self.shownY = None

    def __neg__(self):
        return self

    def __abs__(self):
        return self

    def draw(self):
        pass
    
class line:
    def __init__(self, (p1, p2), width=1, color='red'):
        if p2.x-p1.x == 0:
            self.m = NonePoint()
            print self.m

            self.shownm = -10000

            self.b = point((0, 0))
            self.a = p1.x
        else:
            self.m = (p2.y-p1.y)/(p2.x-p1.x)

            self.shownm = -self.m

            self.b = point((0, p1.y-p1.x*self.m))
            if self.m == 0:
                self.a = NonePoint()
            else:
                self.a = point((-self.b.y/self.m, 0))

        self.width=width
        self.color=color

    def __add__(self, other): #Perpendicular
        if other.m == -reciprocal(self.m):
            return True
        else:
            return False

    def __contains__(self, other):
        if isinstance(other, point):
            if other.y==other.x*self.m+self.b:
                return True
            else:
                return False
        elif isinstance(other, segment):
            if other._p1.y==other._p1.x*self.m+self.b and other._p2.y==other._p2.x*self.m+self.b
                return True
            else:
                return False
        else:
            return False
        
    def __or__(self, other): #Parallel
        if other.m == self.m and other.b != self.b:
            return True
        else:
            return False

    def __getslice(self, i, j):
        if i in self and j in self:
            return segment((i, j), self.width, self.color)
            

    def draw(self):
        graph.create_line(0, self.shownm*(0-graphWidth/2)+graphHeight/2-self.b.y, graphWidth, self.shownm*graphWidth/2+graphHeight/2-self.b.y, width=self.width, fill=self.color)

class segment:
    def __init__(self, (p1, p2), width=1, color='red'):
        if p1.x<=p2.x:
            self._p1 = p1
            self._p2 = p2
        else:
            self._p1 = p2
            self._p2 = p1
        
        if p2.x-p1.x == 0:
            self.m = INFINITY
            print self.m

            self.shownm = -10000

            self.b = point((0, 0))
            self.a = p1.x
        else:
            self.m = (p2.y-p1.y)/(p2.x-p1.x)

            self.shownm = -self.m

            self.b = point((0, p1.y-p1.x*self.m))
            if self.m == 0:
                self.a = p1.y
            else:
                self.a = point((-self.b.y/self.m, 0))

        self.midpoint = point(((p1.x+p2.x)/2, (p1.y+p2.y)/2))
        self.width = width
        self.color = color

        def __len__(self):
            return sqrt((self._p2.x-self.p1.x)**2+(self._p2.y-self._p1.y)**2)

        def __contains__(self, elt):
            if isinstance(elt, point):
                
                
        def draw(self):
            graph.create_line(self._p1.x, self._p1.y, self._p2.x, self._p2.y, width=self.width, fill=self.color)

class triangle:
    def __init__(self, (a, b, c), width=1, color='red'):
        self.vertices = (a, b, c)
        self.sides = (line(a, b), line(b, c), line(c, a))

    def draw(self):
        for x in self.sides: x.draw()

def constructDefaults():
    Origin = point((0, 0), 5, 'black')
    Origin.draw()

    XAxis = line((Origin, point((0, 1))), 2, 'black')
    YAxis = line((Origin, point((1, 0))), 2, 'black')

    XAxis.draw()
    YAxis.draw()

constructDefaults()

def test():
    points = {'A':point((00, 10), 5),
              'B':point((10, 10), 5),
              'C':point((50, 25), 5),
              'D':point((75, 60), 5),
              'E':point((85, 20), 5),
              'F':point((25, 30), 5),
              }

    
    for x in points: points[x].draw()

    l = line((points['A'], points['B']))
    seg = segment
    l.draw()

test()

root.mainloop()

import Tkinter as tk

root = tk.Tk()
winwidth=600
winheight=600
win = tk.Canvas(root, width=winwidth, height=winheight)
win.pack()

def draw_grid(xspacing, yspacing):
    for x in range(winwidth)[::xspacing]:
        win.create_line(x, 0, x, winheight)
    for y in range(winheight)[::yspacing]:
        win.create_line(0, y, winwidth, y)
    
class point:
    def __init__(self, x, y):
        self.x = float(x) #To make division work in lines
        self.y = float(y) #Ditto
        self.shownx = self.x+winwidth/2
        self.showny = self.y*-1+winheight/2
        self.draw()

    def draw(self):
        win.create_oval(self.shownx-2, self.showny-2, self.shownx+2, self.showny+2, fill='red', outline='red')
      
class line:
    def __init__(self, p1, p2):
        self.m = (p2.y-p1.y)/(p2.x-p1.x)
        self.shownm = -1*self.m
        self.yint = p1.y-(p1.x*self.m*-1)
        self.xint = -self.yint/self.m
        self.draw()
        
    def draw(self):
        win.create_line(0, self.shownm*winwidth/-2+winheight/2-self.yint, winwidth, self.shownm*winwidth/2+winheight/2-self.yint, fill='red')

class ellipse:
    def __init__(self, center, r1, r2, rot=0):
        self.center = center
        self.x = center.x
        self.y = center.y
        self.shownx=center.shownx
        self.showny=center.showny
        self.vr = r1
        self.hr = r2
        self.draw()

    def draw(self):
        win.create_oval((self.shownx-self.hr, self.showny-self.vr, self.shownx+self.hr, self.showny+self.vr), outline='red')

class circle(ellipse):
    def __init__(self, center, r):
        self.center = center
        self.x = center.x
        self.y = center.y
        self.shownx = center.shownx
        self.showny = center.showny
        self.r = r
        self.vr = r
        self.hr = r
        self.draw()

#class plane:
#    pass

class ray:
    pass

class segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
        self.draw()

    def draw(self):
        win.create_line(self.p1.shownx, self.p1.showny, self.p2.shownx, self.p2.showny, fill='red')

class vector:
    pass

#draw_grid(20, 20)

pointA=point(0, 0)
pointB=point(100,10)
pointC=point(50, 50)
pointD=point(75, 60)

li=line(pointA, pointB)

el = ellipse(pointA, 10, 20)

circ=circle(pointB, 10)

seg = segment(pointC, pointD)

root.mainloop()

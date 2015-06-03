import Tkinter as tk

graphWidth=500
graphHeight=500
root = tk.Tk()
graph = tk.Canvas(root, width=graphWidth, height=graphHeight)
graph.pack()

class point:
    def __init__(self, (x, y), size=0, color='red'):
        self.x = x
        self.y = y

        self.size = size

        self.color = color #The color of the image

        self.shownX = self.x+graphWidth/2
        self.shownY = graphHeight-(self.y+graphHeight/2)
        self.draw()

    def draw(self):
        graph.create_oval(self.shownX-self.size/2, self.shownY+self.size/2, self.shownX+self.size/2, self.shownY-self.size/2, fill=self.color, outline=self.color)

class line:
    def __init__(self, (p1, p2)):
        pass
origin=point((0, 0), 5)

root.mainloop()

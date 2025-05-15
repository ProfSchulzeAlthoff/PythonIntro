# Nutze die Turtle Malbibliothek
import turtle as tu
# Nutze die Zufallszahlen
import random as rnd

colors = ('red', 'green', 'yellow', 'pink', 'blue')

class turtle_geom:
    def __init__(self,color):
        self._donatello = tu.Turtle()
        self._donatello.pencolor(color)
        self._donatello.shape("turtle")
        self._size = rnd.randrange(10,50)
 
    def move (self):
        x = rnd.randrange(-250,250)
        y = rnd.randrange(-150,150)
        self._donatello.penup()
        self._donatello.goto(x,y)
        self._donatello.pendown()


class rect_turtle (turtle_geom):
    def __init__(self):
        super().__init__(rnd.choice(colors))
        
    def paint(self):
        self.move()
        size = rnd.randrange(10,50)
        for i in range (0,4):
            self._donatello.forward(size)
            self._donatello.left(90)

class triangle_turtle (turtle_geom):
    def __init__(self):
        super().__init__(rnd.choice(colors))
        
    def paint(self):      
        self.move()
        size = rnd.randrange(10,50)  
        for i in range (0,3):
            self._donatello.forward(size)
            self._donatello.left(120)

tu.setup (width=600, height=400)

# 5 triangles and 5 rectangles
geoms = []
for i in range(5):
    geoms.append(rect_turtle())
    geoms.append(triangle_turtle())

for i in range (30):
    geom = rnd.choice(geoms)
    geom.paint()

tu.exitonclick()









def turtle_rect(startx=150, starty=150, size=50):
    # Positioniere an der Startposition
    tu.penup()
    tu.goto(startx, starty)
    tu.pendown()
    # zeichnen in Loop
    for i in range (0,4):
        tu.forward(size)
        tu.left(90)

# Aufruf mit Zufallswerten
# Bildschirm i.d.R. 300 * 400 Pixel
# Wähle daher eine zufällige Startposition zwischen (50,50) und (250,350)
startx = rnd.randrange(50,250)
starty = rnd.randrange(50,350)
# Wähle eine zufällige Größe zwischen 10 und 50 Seitenlänge
size = rnd.randrange(10,50)
turtle_rect(startx, starty, size)

# Fenster erst bei Click schliessen

# Nutze die Turtle Malbibliothek
import turtle as tu
# Nutze die Zufallszahlen
import random as rnd

def turtle_rect(startx=150, starty=150, size=50):
    # Positioniere an der Startposition
    tu.penup()
    tu.goto(startx, starty)
    tu.pendown()
    # zeichnen in Loop
    for i in range (0,4):
        tu.forward(size)
        tu.left(90)

# Initialisieren
tu.setup (width=600, height=400)

for i in range(20):
    # Aufruf mit Zufallswerten
    startx = rnd.randrange(-250,250)
    starty = rnd.randrange(-150,150)
    # Wähle eine zufällige Größe zwischen 10 und 50 Seitenlänge
    size = rnd.randrange(10,50)
    turtle_rect(startx, starty, size)

# Fenster erst bei Click schliessen
tu.exitonclick()











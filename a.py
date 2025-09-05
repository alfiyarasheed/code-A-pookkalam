

import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Digital Onam Pookkalam")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
radius = 200

# --- Write Happy Onam on top ---
t.penup()
t.goto(0, radius + 50)  # position above pookkalam
t.color("white")

# Shadow effect (slight offset in black)
t.goto(-2, radius + 48)
t.color("black")
t.write("Happy Onam", align="center", font=("serif", 36, "bold italic"))

# Main stylish text
t.goto(0, radius + 50)
t.color("gold")
t.write("Happy Onam", align="center", font=("serif", 36, "bold italic"))

# --- Filled Circle Background ---
t.penup()
t.goto(0, -radius)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(radius)
t.end_fill()

# --- Draw 8 petals (lines) ---
t.color("black")
for i in range(8):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(i * 45)
    t.forward(radius)

# --- Large White Diamond inside the circle ---
top    = (0,  radius)
right  = (radius, 0)
bottom = (0, -radius)
left   = (-radius, 0)

diamond_points = [top, right, bottom, left]

t.penup()
t.goto(top)
t.pendown()
t.color("maroon")
t.begin_fill()
for pt in [right, bottom, left, top]:
    t.goto(pt)
t.end_fill()

# --- Large Rose Square (diagonal diameters) ---
diag_points = [
    ( radius / 1.414,  radius / 1.414),   # NE
    (-radius / 1.414,  radius / 1.414),   # NW
    (-radius / 1.414, -radius / 1.414),   # SW
    ( radius / 1.414, -radius / 1.414)    # SE
]

t.penup()
t.goto(diag_points[0])
t.pendown()
t.color("deeppink")   # rose color
t.begin_fill()
for pt in diag_points[1:] + [diag_points[0]]:
    t.goto(pt)
t.end_fill()

# --- Helper functions ---
def draw_and_fill(points, color):
    """Draw a closed polygon with fill"""
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color(color)
    t.begin_fill()
    for pt in points[1:] + [points[0]]:
        t.goto(pt)
    t.end_fill()

def get_midpoints(points):
    """Get midpoints of polygon sides"""
    mids = []
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % len(points)]
        mids.append(((x1+x2)/2, (y1+y2)/2))
    return mids

def scale_polygon(points, scale):
    """Scale polygon towards center"""
    return [(x*scale, y*scale) for (x, y) in points]

# --- Festive Color Palette ---
colors = ["purple", "orange", "white", "gold", "pink", "red"]

# --- Draw alternating layers (square → diamond → square…) ---
current = diag_points  # start from rose square instead of diamond
for i in range(6):  
    color = colors[i % len(colors)]
    draw_and_fill(current, color)

    if i % 2 == 0:
        current = get_midpoints(current)   # diamond
    else:
        current = scale_polygon(current, 0.7)  # smaller square

num_petals = 36  # increase petals for smoother flower
angle_step = 360 / num_petals
outer_radius = radius + 20
petal_radius = (2 * math.pi * outer_radius) / num_petals / 2

for i in range(num_petals):
    angle = i * angle_step
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(outer_radius)
    t.pendown()
    t.color("gold")   
    t.begin_fill()
    t.circle(petal_radius)
    t.end_fill()
t.hideturtle()
turtle.done()


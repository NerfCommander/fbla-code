import pgzrun
from random import randint 
from pgzero.actor import Actor
WIDTH = 400
HEIGHT = 600
DOT_MAX_HEIGHT = 500

dots = []

lines = []

next_dot_clicked = 0

next_dot = 0

for dot in range(0, 14):
    actor = Actor("dot")
    actor.pos = randint(20, DOT_MAX_HEIGHT - 20), \
    randint(20, DOT_MAX_HEIGHT - 20)
    dots.append(actor)

def draw():
    global next_dot_clicked 

    screen.fill("black")
    number = 1 
    for dot in dots:
        screen.draw.text(str(number), \
                        (dot.pos[0], dot.pos[1] + 12))
        dot.draw()

        number = number + 1 
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))
    if next_dot_clicked != 0:
        screen.draw.text(str(next_dot_clicked), \
                (20, 400), color="white")
        next_dot_clicked = 0


def on_mouse_down(pos):
    global next_dot
    global lines
    global next_dot_clicked 

    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot -1].pos, dots[next_dot].pos))
            next_dot_clicked = next_dot
        next_dot = next_dot + 1
    else:
        lines = []
        next_dot_clicked = 0
        next_dot = 0
    

       

pgzrun.go()

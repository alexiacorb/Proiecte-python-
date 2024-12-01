import turtle

turtle_screen = turtle.getscreen()
turtle_actor = turtle.Turtle()
culori = ["blue", "yellow", "red"]
latime, inaltime = 300, 200

for culoare in culori:
    turtle_actor.fillcolor(culoare)
    turtle_actor.begin_fill()
    for i in range(2):
        turtle_actor.forward(latime / 3)
        turtle_actor.right(90)
        turtle_actor.forward(inaltime)
        turtle_actor.right(90)
    turtle_actor.end_fill()
    turtle_actor.forward(latime / 3)

turtle_actor.hideturtle()
turtle_actor.done()

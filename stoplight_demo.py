# Stoplight 
import turtle
import time

wn = turtle.Screen()
wn.title("Stoplight by @Mariskalucia")
wn.bgcolor("grey")

# Draw box around the spotlight
pen = turtle.Turtle()
pen.color("black")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

# Red light
red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("black")
red_light.penup()
red_light.goto(0, 40)

# orange light
orange_light = turtle.Turtle()
orange_light.shape("circle")
orange_light.color("black")
orange_light.penup()
orange_light.goto(0, 0)

# Green light
green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("black")
green_light.penup()
green_light.goto(0, -40)


while True:
    orange_light.color("black")
    red_light.color("red")
    time.sleep(4)

    red_light.color("black")
    green_light.color("green")
    time.sleep(3)

    green_light.color("black")
    orange_light.color("darkorange")
    time.sleep(2)

wn.mainloop()
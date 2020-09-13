# import turtle mode
import turtle

# Set op screen
wn = turtle.Screen()
wn.title("stoplights with classes by @Mariskalucia")
wn.bgcolor("grey")

class Stoplight():
    def __init__(self, x, y):
        # Draw the border
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("black")
        self.pen.goto(x-30, y+60)
        self.pen.pendown()
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)

        self.color = ""
        
        self.red_light = turtle.Turtle()
        self.orange_light = turtle.Turtle()
        self.green_light = turtle.Turtle()

        self.red_light.speed(0) 
        self.orange_light.speed(0) 
        self.green_light.speed(0) 
           
        self.red_light.color("black") 
        self.orange_light.color("black")  
        self.green_light.color("black")  

        self.red_light.shape("circle")
        self.orange_light.shape("circle") 
        self.green_light.shape("circle") 

        self.red_light.penup()
        self.orange_light.penup() 
        self.green_light.penup() 

        self.red_light.goto(x, y + 40)
        self.orange_light.goto(x, y) 
        self.green_light.goto(x, y - 40) 
           

    def change_color(self, color):
        self.red_light.color("black") 
        self.orange_light.color("black")  
        self.green_light.color("black")  

        if color == "red":
            self.red_light.color("red")
            self.color = "red"
        elif color == "orange":
            self.orange_light.color("orange")
            self.color = "orange"
        elif color == "green":
            self.green_light.color("green")
            self.color = "green"
        else:
            print("Error : Unkown Color {}".format(color))

    def timer(self):
        if self.color == "red":
            self.change_color("green")
            wn.ontimer(self.timer, 4000)
        elif self.color == "orange":
              self.change_color("red")
              wn.ontimer(self.timer, 3000)
        elif self.color == "green":
              self.change_color("orange")
              wn.ontimer(self.timer, 2000)
        
        

stoplight = Stoplight(0, 0)
stoplight.change_color("red")
stoplight.timer()

stoplight2 = Stoplight(-100, 0)
stoplight2.change_color("orange")
stoplight2.timer()

stoplight3 = Stoplight(100, 0)
stoplight3.change_color("green")
stoplight3.timer()




wn.mainloop()
from turtle import Turtle, Screen
import math

pi=math.pi

def deg_to_rad(deg):
    return deg*pi/180

def rad_to_deg(rad):
    return rad*180/pi

timmy=Turtle()
screen=Screen()
screen.title("String art with Turtle")

timmy.speed(0)

screen.setup(height=1000,width=1000)

# timmy.penup()
# timmy.goto(-300,300)
# timmy.pendown()

def drawer(turtle, height, width, step_size, initial_angle, dir_y, dir_x):

    if dir_x==1:
        turtle.forward(width)
        turtle.backward(width)
    else:
        turtle.backward(width)
        turtle.forward(width)

    if dir_y==1:    
        turtle.left(90)
        
    else:
        turtle.right(90)

    turtle.forward(height)

    perpendicular=height
    angle=deg_to_rad(initial_angle)
    hypotenuse=perpendicular/math.cos(deg_to_rad(angle))
    base=math.sqrt(hypotenuse*hypotenuse-perpendicular*perpendicular)
    

    while base<=height:

        
        perpendicular=perpendicular-step_size
        hypotenuse=perpendicular/math.cos(angle)
        base=math.sqrt(hypotenuse*hypotenuse-perpendicular*perpendicular)
     
        turtle.left(180)
        turtle.forward(step_size)
        
        
        if (dir_x==1 and dir_y==0) or (dir_x==0 and dir_y==1):
            turtle.right(rad_to_deg(angle))
        elif (dir_x==1 and dir_y==1) or (dir_x==0 and dir_y==0):
            turtle.left(rad_to_deg(angle))
        
        
        turtle.forward(hypotenuse)


        if (dir_x==0 and dir_y==1) or (dir_x==1 and dir_y==0):
            turtle.left(90+rad_to_deg(angle))
        elif (dir_x==0 and dir_y==0) or (dir_x==1 and dir_y==1):
            turtle.right(90+rad_to_deg(angle))
        
        turtle.forward(base)

        if (dir_y==0 and dir_x==1) or (dir_x==0 and dir_y==1):
            turtle.left(90)
        elif (dir_x==1 and dir_y==1) or (dir_x==0 and dir_y==0):
            turtle.right(90)

        turtle.forward(perpendicular)
        angle=math.atan((base+step_size)/(perpendicular-step_size))
        

drawer(timmy, 200, 50, 5, 5, 1, 0)

timmy.home()
drawer(timmy, 200, 50, 5,5,1,1 )


timmy.home()
drawer(timmy, 200, 50, 5,5,0,1 )


timmy.home()
drawer(timmy, 200, 50, 5,5,0,0 )

timmy.penup()
timmy.goto(-200,200)
timmy.pendown()
timmy.seth(0)
drawer(timmy,200,50,5,5,0,1)

timmy.penup()
timmy.goto(200,200)
timmy.pendown()
timmy.seth(0)
drawer(timmy,200,50,5,5,0,0)

timmy.penup()
timmy.goto(-200,-200)
timmy.pendown()
timmy.seth(0)
drawer(timmy,200,50,5,5,1,1)

timmy.penup()
timmy.goto(200,-200)
timmy.pendown()
timmy.seth(0)
drawer(timmy,200,50,5,5,1,0)

timmy.teleport(200,400)
timmy.seth(0)
drawer(timmy,200,50,5,5,0,0)

timmy.teleport(-200,400)
timmy.seth(0)
drawer(timmy,200,50,5,5,0,1)

timmy.teleport(200,0)
timmy.seth(0)
drawer(timmy,200,50,5,5,1,1)


timmy.teleport(-200,0)
timmy.seth(0)
drawer(timmy,200,50,5,5,1,0)

timmy.teleport(0,-400)
timmy.seth(0)
drawer(timmy,200,50,5,5,1,1)


timmy.teleport(0,-400)
timmy.seth(0)
drawer(timmy,200,50,5,5,1,0)

timmy.teleport(400,0)
timmy.seth(0)
drawer(timmy,200,50,5,5,0,0)

timmy.teleport(200,-200)
timmy.seth(0)
drawer(timmy,200,50,5,5,1,1)


timmy.teleport(-400,0)
timmy.seth(0)
drawer(timmy,200,50,5,5,0,1)


timmy.teleport(-200,-200)
timmy.seth(0)
drawer(timmy,200,50,5,5,1,0)

screen.exitonclick()
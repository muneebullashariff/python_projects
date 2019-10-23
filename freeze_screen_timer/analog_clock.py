import turtle
import time

## Create a turtle screen object
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Simple analog clock by muneeb")
wn.tracer(0) # The animation will be shown only when we update it

## Create our drawing pen
pen = turtle.Turtle()
# Hides the pen on the screen but we can draw using it
pen.hideturtle()
# It'll draw as fast as it can
pen.speed(0)
# Width of the lines drawn
pen.pensize(3)

## Function to draw the clock
def draw_clock(hour, minute, seconds, pen):
     
    # Draw the clock face
    pen.up()
    pen.goto(0,210) # x=0, y=210
    pen.setheading(180) # direction 180 degree
    pen.color("green")
    pen.pendown() # to tell to draw
    pen.circle(210) #radius of circle

    # Draw the lines for hours
    pen.up()
    pen.goto(0,0) # center of the screen
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190) # forward 190+20 = 210
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30) # rotate by 30 degree

    # Draw the hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90) # the head of pen is pointing at 90 degree
    angle = (hour/12)*360
    pen.rt(angle)
    pen.pendown() # put down the pen and draw
    pen.fd(100)

    # Draw the minute hand
    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90) # the head of pen is pointing at 90 degree
    angle = (minute/60)*360
    pen.rt(angle)
    pen.pendown() # put down the pen and draw
    pen.fd(180)

    # Draw the second's hand
    pen.penup()
    pen.goto(0,0)
    pen.color("gold")
    pen.setheading(90) # the head of pen is pointing at 90 degree
    angle = (seconds/60)*360
    pen.rt(angle)
    pen.pendown() # put down the pen and draw
    pen.fd(190)

while True:
    # Get the current time
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M")) 
    seconds = int(time.strftime("%S")) 

    # call the function
    draw_clock(hour,minute,seconds,pen)
    wn.update() # Update the turtle drawing

    time.sleep(1) # Sleep for one second
 
    pen.clear() # Clearing the pen

# Used so that the window doesn't get closed
wn.mainloop()

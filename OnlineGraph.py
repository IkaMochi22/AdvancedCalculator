import turtle

# rename turtle for quick typing
t = turtle

x1 = 0
x2 = 0

# Screen setup
ts = turtle.Screen()
ts.setworldcoordinates(-16, -16, 16, 16)

# Draws the axis
def draw_axes():
	t.pencolor('red')
	t.penup()
	t.goto(-15,0)
	t.write("-15")
	t.pendown()
	t.goto(15,0)
	t.write("15")
	t.penup()
	t.goto(0,-15)
	t.write("-15")
	t.pendown()
	t.goto(0,15)
	t.write("15")
	t.goto(0,0)
	t.dot()
	t.write("0")
	t.penup()

def PlotXOne():
	x1 = t.numinput("First x value", "Enter x1")
	t.goto(x1,0)
	t.pencolor('black')
	t.pendown()
	t.dot()
	t.penup()
	t.write(x1)
	t.goto(0,0)

def PlotXTwo():
	x2 = t.numinput("Second x value", "Enter x2")
	t.goto(x2, 0)
	t.pencolor('black')
	t.pendown()
	t.dot()
	t.penup()
	t.write(x2)
	t.goto(0,0)

draw_axes()
answer = t.textinput("How many x intercepts do you want?" , "1 / 2")
if answer == '1':
	PlotXOne()
	t.done
else:
	PlotXOne()
	PlotXTwo()
	






t.exitonclick()
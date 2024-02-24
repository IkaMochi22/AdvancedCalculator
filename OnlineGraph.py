import turtle as t


# Screen setup
ts = t.Screen()
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
	t.home()
	t.dot()
	t.write("0")
	t.penup()

# Plots the first point on the x axis
def PointOne():
	x1 = t.numinput("First x value", "Enter x1")
	y1 = t.numinput("First y value", "Enter y1")
	t.goto(x1,y1)
	t.pencolor('black')
	t.pendown()
	t.dot()
	t.penup()
	t.write((x1, y1))
	t.home()

	return x1, y1

# Plots the second point on the x axis
def PointTwo():
	x2 = t.numinput("Second x value", "Enter x2")
	y2 = t.numinput("Second y value", "Enter y2")
	t.goto(x2,y2)
	t.pencolor('black')
	t.pendown()
	t.dot()
	t.penup()
	t.write((x2, y2))
	t.penup()
	t.goto(x2,y2)
	t.pendown()
	t.goto(x1,y1)
	t.penup()

	return x2, y2

def equation():
	m = (y2 - y1)/(x2 - x1)


# Graph is drawn
t.speed(0)
draw_axes()
t.speed(4)

answer = t.textinput("How many x intercepts do you want?" , "1 / 2")

if answer == '1':
	PointOne()

else:
	x1, y1 = PointOne()
	x2, y2 = PointTwo()


t.exitonclick()
import turtle
import math

def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

def circle(t, r):
	circumference = 2 * math.pi * r
	print('2 * math.pi * r =', circumference )
	n = int(circumference / 3)+1
	print('n - ', n)
	length = circumference / n
	print(length)
	polygon(t, n, length)



bob = turtle.Turtle()
#print(bob)
for i in range(4):
	print('Hi!')


circle(bob, 100)

turtle.mainloop()

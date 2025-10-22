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
	n = 10
	length = circumference / n
	print(length)
	polygon(t, n, length)



bob = turtle.Turtle()
#print(bob)
for i in range(4):
	print('Hi!')


circle(bob, 100)

ln1 = (360.0/10)*2
print(ln1)

bob.lt(ln1)
bob.fd(100*2)
ln1 = (360.0/10)*3
bob.lt(ln1)
ln2 = (2 * math.pi * 100)/10
bob.fd(10)
turtle.mainloop()

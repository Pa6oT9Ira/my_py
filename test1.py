import math
import turtle

bob = turtle.Turtle()
st = 15
angle = (360 / st) / 2

y = 40 * math.sin(angle * math.pi / 180)
print(y)
for i in range(st):
	bob.rt(angle)
	bob.fd(40)
	bob.lt(90+angle)
	bob.fd(2*y)
	bob.lt(90+angle)
	bob.fd(40)
	bob.lt(180-angle)
	bob.lt(angle * 2)



bob.pu()
bob.fd(40*2 + 10)
bob.pd()


bob.hideturtle()
turtle.mainloop()
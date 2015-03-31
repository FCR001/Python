#!/usr/bin/python
# -*- coding: UTF-8 -*-
import turtle
#create window and turtle
window = turtle.Screen()
babbage = turtle.Turtle()
#dibujamos el tallo y el centro
babbage.color("green", "black")
babbage.right(90)
babbage.forward(200)
babbage.left(180)
babbage.forward(300)
babbage.right(90)
babbage.color("black", "blue")
babbage.begin_fill()
babbage.circle(10)
babbage.end_fill()
#Dibujamos los petalos
for i in range(1,24):
	if babbage.color() == ("red", "black"):
		babbage.color("orange", "black")
	elif babbage.color() == ("orange", "black"):	
		babbage.color("yellow", "black")
	else:
		babbage.color("red", "black")	
	babbage.left(15)
	babbage.forward(50)
	babbage.left(157)
	babbage.forward(50)
babbage.home()


window.exitonclick()


#!/usr/bin/env python3 
 # Block
 # Class Block defines a Block module object from the turtle class. 
 # the Block object is what the maze will be made out of.
 #
 # Parameters:
 # turtle.Turtle - child of the turtle's module Turtle class.
 # A Block is a Turtle. 
 
import turtle

class Block (turtle.Turtle):
	def __init__(self): # self refers to the object we are calling the method on. 
		turtle.Turtle.__init__(self) # Must initalize the turtle.Turtle class as well
		self.shape("square")
		self.color("cyan")
		self.penup() # Don't want to leave a trail
		self.speed(0) # Animation speed


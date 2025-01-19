#!/usr/bin/env python3
 
# Player

# Class Player defines a Player module object from the turtle class.
# The Player is what the gamer will control to navigate through the mazes
# Player is a child of the Turtle class

import turtle 

class Player(turtle.Turtle):
	def __init__(self, blocks):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("red")
		self.penup()
		self.speed(0)
		self.blocks = blocks

	# The player can move in four different directions:
	# Up, down, left, or right. Player will move by 24 
	# pixels at a time

	def up(self, blocks): # go to current x cor, then y cor up 24 pixels to move up by ONE
		self.blocks = blocks
		move_x = self.xcor()
		move_y = self.ycor() + 24

		# is there a block in the space we want to move to?
		if (move_x, move_y) not in blocks:
			self.goto(move_x, move_y)

	def down(self, blocks): # same as up, y is -24 go traverse down by ONE
		self.blocks = blocks
		move_x = self.xcor()
		move_y = self.ycor() - 24

		# is there a block in the space we want to move to?
		if (move_x, move_y) not in blocks:
			self.goto(move_x, move_y)

	def left(self, blocks): # change xcor to go left
		self.blocks = blocks
		move_x = self.xcor() - 24
		move_y = self.ycor()

		if (move_x, move_y) not in blocks:
			self.goto(move_x, move_y)

	def right(self, blocks): # and now for right
		self.blocks = blocks
		move_x = self.xcor() + 24
		move_y = self.ycor()

		if (move_x, move_y) not in blocks:
			self.goto(move_x, move_y)

#!/usr/bin/env python3
# playerMove - driver code for user to move the player across the mapi

import turtle

def player_move(player, blocks):
	# The player can move in four different directions:
	# Up, down, left, or right. Player will move by 24 
	# pixels at a time

	def up(player, blocks): # go to current x cor, then y cor up 24 pixels to move up by ONE
		move_x = player.xcor()
		move_y = player.ycor + 24

		# is there a block in the space we want to move to?
		if (move_x, move_y) not in blocks:
			player.goto(move_x, move_y)

	def down(player, blocks): # same as up, y is -24 go traverse down by ONE
		move_x = player.xcor()
		move_y = player.ycor - 24

		# is there a block in the space we want to move to?
		if (move_x, move_y) not in blocks:
			player.goto(move_x, move_y)

	def left(player, blocks): # change xcor to go left
		move_x = player.xcor - 24
		move_y = player.ycor()

		if (move_x, move_y) not in blocks:
			player.goto(move_x, move_y)

	def right(player, blocks): # and now for right
		move_x = player.xcor + 24
		move_y = player.ycor()

		if (move_x, move_y) not in blocks:
			player.goto(move_x, move_y)

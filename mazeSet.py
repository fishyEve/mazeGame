#!/usr/bin/env python3
# mazeSet.py
# Creates level setup for game to function

import turtle


def setup_maze(level[]):
	for y in range(len(level)):
		for x in range(len(level[y])):
			# track character at every x,y coordinate
			character = level[x][y]
			
			# calc screen at x,y coordinates
			x_coord = -288 + (x*24)
			y_coord = 288 - (y*24)

			# are we at a wall?
			if character == "X"
				pen.goto(x_coord, y_coord)
				pen.stamp()

			# Are we player?
			if character == "P":
				player.goto(x_coord, y_coord)
				pen.stamp()



#!/usr/bin/env python3
# mazeSetup.py is the code that will create the physical maze

import turtle
from Block import Block 

def setup_maze(block, level, player, blocks):
	for y in range(len(level)):
		print (y)
		for x in range(len(level[y])):
			#if x == len(level[y]):
				#break
			print(x)
			# retain each spot at each x,y coordinate
			spot = level[y][x]
			# formulas to calculate screen x,y coorindates
			x_coord = -288 + (x * 24)
			y_coord = 288 - (y * 24)

			# If X, there is a wall in place. 
			if spot == "X":
				block.goto(x_coord, y_coord)
				block.stamp()
				turtle.TurtleScreen._RUNNING = True
				blocks.append((x_coord, y_coord)) # add coord of block to list
			# If P, this spot hosts the player.
			if spot == "P":	
				player.goto(x_coord, y_coord)

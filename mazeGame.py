# mazeGame.py is the running driver of the game! 
import turtle
from turtle import *
from Block import Block
from Player import Player
from mazeSetup import setup_maze
from playerMove import player_move

if __name__ == "__main__":
	window = turtle.Screen() #creates screen for maze
	window.bgcolor("black")
	window.title("Maze Game ଘ( ͡° ͜ʖ ͡°)")
	window.setup(700,700) # pixels

	# Create list to store levels 
	levels = [""]
	# Create list to store each block on the map
	global blocks 
	blocks = [0,0]

	# create instance of block from Block() class
	block = Block()

	# open text file containing first level
	#f = open('level_1.txt', 'r')
	# add contents of the file 
	#level_1 =[f.read().splitlines()]

	#f.close()

	# append level to levels list
	#levels.append(level_1)
	#print(level_1)

	level_1 = [
	"XXXXXXXXXXXXXXXXXXXXXXXXX",
	"XP XXXXX             XXXX",
	"X  XXXXX         XXXXXXXX",
	"X     XX      XXXXXXXXXXX",
	"X     XX               XX",
	"X     XX               XX",
	"X     XX             XXXX",
	"X     XX      XXX       X",
	"X     XX       X        X",
	"X             XXX       X",
	"X             XXX       X",
	"X      X      XXX       X",
	"X             XXXXXX    X",
	"X      X      XXX       X",
	"X          XXXXXX       X",
	"X            XXXX       X",
	"X                       X",    
	"XXXXXXX       XX        X",
	"XXXXXXX               XXX",
	"XXXXXXX               XXX",
	"XXXXXXX           XXXXXXX",
	"XXX               XXXXXXX",
	"X   XXX     XXX      XXXX",
	"X   XXX     XX         XX",
	"X   XX       X          X",
	"XXXXXXXXXXXXXXXXXXXXXXXXX"
	]

	levels.append(level_1)


	# create class instances
	pen = Pen()
	player = Player(blocks)

	setup_maze(block, level_1, player, blocks)


	# keyboard binding so user can move player
#	turtle.listen() # have turtle await keyboard input
#	turtle.onkey(player.left(blocks), "Left")
#	turtle.onkey(player.right(blocks), "Right")
#	turtle.onkey(player.up(blocks), "Up")
#	turtle.onkey(player.down(blocks), "Down")

#	window.tracer(0)

	# Keep the game running
	while True:
		#window.update() # Continiously update screen as user moves player
 		# keyboard binding so user can move player
		turtle.listen() # have turtle await keyboard input
		turtle.onkey(player.left(blocks), "Left")
		turtle.onkey(player.right(blocks), "Right")
		turtle.onkey(player.up(blocks), "Up")
		turtle.onkey(player.down(blocks), "Down")
		window.update()




import pygame
from bar import Bar
from ball import Ball
from block import Block

BACKGROUND = (0,0,0)
BAR_COLOR = (255,255,255)
BALL_COLOR = (255,255,255)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (70,0,150)

def initialize_and_run():

	pygame.init()

	screen = pygame.display.set_mode((250,300))

	main_loop(screen)

def bar_movement(bar):
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_LEFT]:
		bar.move_left()
	if pressed[pygame.K_RIGHT]:
		bar.move_right()

def generate_blocks(screen):
	blocks = []
	colors = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
	for i in range(6):
		for j in range(25):
			blocks.append(Block(screen,10*j,60+10*i,colors[i]))
	return blocks
	# supposed to return list of block

def main_loop(screen):
	point = 0
	bar = Bar(screen)
	ball = Ball(screen)
	blocks = generate_blocks(screen)
	running = True
	while running:
		screen.fill(BACKGROUND)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# bar movement
		bar_movement(bar)

		# ball movement + colision detection
		ball.move()
		ball.colide_with_bar(bar)
		ball.colide_with_wall()
		for block in blocks:
			if ball.colide_with_block(block):
				point += 100
		
		#draw
		bar.draw()
		ball.draw()
		for block in blocks:
			block.draw()
		pygame.display.update()

	pygame.quit()


if __name__ == "__main__":
	initialize_and_run()
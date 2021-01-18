import pygame
import math

from bar import Bar
from bar import BarDim
from block import Block

class Ball:
	def __init__(self,screen):
		self._screen = screen
		self._x = 122
		self._y = 150
		self._width = 5
		self._height = 5
		self._color = (255,255,255)
		self._speed = 4
		self._direction = [0,-1] # unit vector



	def move(self):
		translation = [self._speed*unit for unit in self._direction]
		self._x += translation[0]
		self._y += translation[1]
		#print(translation, sum(t**2 for t in translation))

	def draw(self):
		pygame.draw.rect(self._screen, self._color, (self._x,self._y,self._width,self._height))

	def colide_with_bar(self, bar):
		colide = False
		bar_dim = bar.get_dimension()
		bar_x = bar_dim[BarDim.X.value]
		bar_y = bar_dim[BarDim.Y.value]
		bar_width = bar_dim[BarDim.WIDTH.value]
		bar_height = bar_dim[BarDim.HEIGHT.value]
		colide_hor = self._x + self._width >= bar_x and self._x <= bar_x + bar_width
		colide_ver = self._y + self._height >= bar_y and self._y <= bar_y
		colide = colide_hor and colide_ver
		#print(colide)
		if colide:
			self.calculate_direction(bar_x,bar_width)
			
	def colide_with_wall(self):
		if self._x <= 0: 
			self._direction[0] = abs(self._direction[0])
		if self._x >= self._screen.get_width():
			self._direction[0] = -1*abs(self._direction[0])
		if self._y <=0:
			self._direction[1] = abs(self._direction[1])

		#TODO: replace with game over logic
		if self._y >= self._screen.get_height():
			self._direction[1] = -1*abs(self._direction[1])

	def colide_with_block(self,block):
		# possibly change this to vector
		colide = False
		if block.get_is_active():
			block_dim = block.get_dimension()
			colide_hor = self._x + self._width >= block_dim[0] and self._x <= block_dim[0] + block_dim[2]
			colide_ver = self._y + self._height >= block_dim[1] and self._y < block_dim[1] + block_dim[3]
			colide = colide_hor and colide_ver
			if colide:
				block.deactivate()
				touch_hor_top = self._y <= block_dim[1] and self._y + self._height >= block_dim[1]
				touch_hor_bot = self._y <= block_dim[1] + block_dim[3] and self._y + self._height >= block_dim[1] + block_dim[3]
				touch_ver_left = self._x <= block_dim[0] and self._x + self._width >= block_dim[0]
				touch_ver_right = self._x <= block_dim[0] + block_dim[2] and self._x + self._width >= block_dim[0] + block_dim[2]

				#TODO: change to abs
				if touch_hor_top:
				 	self._direction[1] = -1*abs(self._direction[1])
				if touch_hor_bot:
					self._direction[1]  = abs(self._direction[1])
				if touch_ver_left:
				 	self._direction[0] = -1*abs(self._direction[0])
				if touch_ver_right:
				 	self._direction[0] = abs(self._direction[0])
			#colide = touch_hor and touch_ver
			#if colide:
			#	block.deactivate()
			#if colide and not (touch_hor or touch_ver):
			# 	print("error colide_with_block")
		return colide

	def calculate_direction(self,bar_x,bar_width):
		colision_point = self._x + self._width / 2
		relative_colision_point = colision_point - bar_x
		angle = (((relative_colision_point/bar_width)- 0.5)*2)*(math.pi/4)
		self._direction[0] = math.sin(angle)
		self._direction[1] = -1*math.cos(angle)


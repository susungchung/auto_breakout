import pygame

class Block:
	def __init__(self,screen,x,y,color):
		self._screen = screen
		#TODO: set proper x,y coordinate
		self._x = x
		self._y = y
		self._width = 10
		self._height = 10
		self._color = color
		self._is_active = True

	def draw(self):
		if self._is_active:
			pygame.draw.rect(self._screen, self._color, (self._x,self._y,self._width,self._height))

	def deactivate(self):
		self._is_active = False

	def get_is_active(self):
		return self._is_active
	def get_dimension(self):
		return (self._x, self._y, self._width, self._height)
import pygame
from enum import Enum
class BarDim(Enum):
	X = 0
	Y = 1
	WIDTH = 2
	HEIGHT = 3

class Bar:
	def __init__(self,screen):
		self._screen = screen
		self._x = 110
		self._y = 270
		self._width = 30
		self._height = 7
		self._speed = 5
		self._color = (255,255,255)

	def draw(self):
		pygame.draw.rect(self._screen, self._color, (self._x,self._y,self._width,self._height))

	def move_right(self):
		if self._x + self._width < self._screen.get_width():
			self._x += self._speed

	def move_left(self):
		if self._x > 0:
			self._x -= self._speed

	def get_dimension(self):
		return (self._x, self._y, self._width, self._height)

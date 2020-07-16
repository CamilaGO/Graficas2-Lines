"""
Paula Camila Gonzalez Ortega
18398
"""
import struct

def char(c):
	return struct.pack('=c', c.encode('ascii'))

def word(c):
	return struct.pack('=h', c)

def dword(c):
	return struct.pack('=l', c)

def changecolor(r, g, b):
	return bytes([b, g, r])

BLACK = changecolor(0,0,0)
WHITE = changecolor(255,255,255)
RED = changecolor(255, 0, 0)

class Render(object):
	def __init__(self, width, height, r, g, b):
		self.framebuffer = []
		self.clear_color = BLACK
		self.curr_color = RED
		self.glCreateWindow(width, height)
		self.glClearColor(r, g, b)
		self.glclear()

	def glInit():
		#Se inicializan variables
		pass

	def glCreateWindow(self, width, height):
		self.width = width
		self.height = height

	def glViewPort(self, x, y, width, height):
		self.vpWidth = width
		self.vpHeight = height
		self.vpx = x
		self.vpy = y

	def glclear(self):
		self.framebuffer = [
		[self.clear_color for x in range(self.width)]
		for y in range(self.height)
		]

	def glClearColor(self, r, g, b):
		red = round(r*255)
		green = round(g*255)
		blue = round(g*255)
		self.clear_color = changecolor(red, green, blue)

	def glVertex(self, x, y):
		new_x = round((x+1)*(self.vpWidth/2)+self.vpx)
		new_y = round((y+1)*(self.vpHeight/2)+self.vpy)
		#Linea 59 y 58 basadas en https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glViewport.xhtml
		self.framebuffer[new_x][new_y] = self.curr_color
	
	def glColor(self, r=1, g=1, b=1):
		red = round(r*255)
		green = round(g*255)
		blue = round(g*255)
		self.curr_color = changecolor(red, green, blue)

	#Funciones para aplicar la ecuacion de la recta y dibujar lineas
	def drawLine(self, x0, y0, x1, y1):
		dy = abs(y1 - y0)
		dx = abs(x1 - x0)

		offset = 0 
		threshold =  dx

		y = y0
		for x in range(x0, x1):
			if dy > dx:
				self.glVertex(y, x)
			else:
				self.glVertex(x, y)
			
			offset += dy * 2 
			if offset >= threshold:
				y += 1 if y0 < y1 else - 1
				threshold += 2 * dx

	def glLine(self, x0, y0, x1, y1):
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)

		if dy < dx:
			self.drawLine(x0, y0, x1, y1)
		else:
			self.drawLine(y0, x0, y1, x1)

		if x0 > x1:
			self.drawLine(x1, y1, x0, y0)
		else:
			self.drawLine(x0, y0, x1, y1)

	

	def finish(self, filename):
		f = open(filename, 'bw')

		# file header
		f.write(char('B'))
		f.write(char('M'))
		f.write(dword(14 + 40 + self.width * self.height * 3))
		f.write(dword(0))
		f.write(dword(14 + 40))

		# image header
		f.write(dword(40))
		f.write(dword(self.width))
		f.write(dword(self.height))
		f.write(word(1))
		f.write(word(24))
		f.write(dword(0))
		f.write(dword(self.width * self.height * 3))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))

		# pixel data
		for x in range(self.height):
			for y in range(self.width):
				f.write(self.framebuffer[x][y])


		f.close()


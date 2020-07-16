"""
Paula Camila Gonzalez Ortega
18398
"""
from gl import Render, changecolor

posX = 250
posY = 250
width = 1000
height = 1000

bitmap = Render(width, height, 0, 0, 0) #los ultimos tres son los colores son los del background

bitmap.glViewPort(posX, posY, width - 500 , height - 500)

bitmap.glColor(1, 0, 0) #estos colores son los que se usaran en Vertex

bitmap.glLine(0, 0, 1, 1)

bitmap.glVertex(1, 1)

bitmap.glVertex(0, 0)

bitmap.finish('out.bmp')
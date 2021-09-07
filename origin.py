from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(1.0,1.0,0.0,1.0)
    gluOrtho2D(0,500,0,500)

def points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.2,0.5,0.4)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(250,250)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(250,250)
    glutCreateWindow("Plotting Origin")
    glutDisplayFunc(points)
    init()
    glutMainLoop()

main()
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def plot(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    steps=0
    if(abs(dx)>abs(dy)):
        steps=abs(dx)
    else:
        steps=abs(dy)
    xinc=dx/steps
    yinc=dy/steps
    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    for step in range(1,steps+1):
        glVertex2f(x1,y1)
        x1=x1+xinc
        y1=y1+yinc

    glEnd()
    glFlush()

def main():
    x1=int(input("x1: "))
    x2=int(input("x2: "))
    y1=int(input("y1: "))
    y2=int(input("y2: "))
    print("starting window...")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(250,250)
    glutCreateWindow("DDA Algorithm")
    glutDisplayFunc(lambda: plot(x1,y1,x2,y2))
    glutIdleFunc(lambda: plot(x1,y1,x2,y2))
    init()
    glutMainLoop()

main()
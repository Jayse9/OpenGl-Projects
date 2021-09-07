from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-10.0,10.0,-10.0,10.0)

def horizontal(xmin,xmax,y):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    x=xmin
    while(x<=xmax):
        glVertex2f(x,y)
        x=x+0.05
    glEnd()
    glFlush()

def vertical(ymin,ymax,x):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    y=ymin
    while(y<=ymax):
        glVertex2f(x,y)
        y=y+0.05
    glEnd()
    glFlush()

def diagonal(x,y):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    while(x<=y):
        glVertex2f(x,x)
        x=x+0.05
    glEnd()
    glFlush()

def main():
    choice=input("Enter Choice: ")
    if(int(choice)==1):
        xmin=float(input("Enter staring x range: "))
        xmax=float(input("Enter ending x range: "))
        y=float(input("Enter y value: "))
        print("starting window...")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(250,250)
        glutCreateWindow("Horizontal Line")
        glutDisplayFunc(lambda:horizontal(xmin,xmax,y))
        glutIdleFunc(lambda:horizontal(xmin,xmax,y))
        init()
        glutMainLoop()
    elif(int(choice)==2):
        ymin=float(input("Enter staring y range: "))
        ymax=float(input("Enter ending y range: "))
        x=float(input("Enter x value: "))
        print("starting window...")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(250,250)
        glutCreateWindow("Vertical Line")
        glutDisplayFunc(lambda:vertical(ymin,ymax,x))
        glutIdleFunc(lambda:vertical(ymin,ymax,x))
        init()
        glutMainLoop()
    elif(int(choice)==3):
        x=float(input("Enter x co-ordinate: "))
        y=float(input("Enter y co-ordinate: "))
        print("starting window...")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(250,250)
        glutCreateWindow("Diagonal Line")
        glutDisplayFunc(lambda:diagonal(x,y))
        glutIdleFunc(lambda:diagonal(x,y))
        init()
        glutMainLoop()
    else:
        print("Invalid Choice")

main()
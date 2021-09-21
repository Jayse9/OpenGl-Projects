from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def plot(x1,x2,y1,y2):
    m=(y2-y1)/(x2-x1)
    if(m<1):
        c=2*(y2-y1)
        pk=c-(x2-x1)
    else:
        c=2*(x2-x1)
        pk=c-(y2-y1)

    x=x1
    y=y1

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.5,3.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)

    if(m<1):
        for x in range(x1,x2+1):
            glVertex2f(x,y)
            if(pk<0):
                pk=pk+c
            else:
                pk=pk+c-2*(x2-x1)
                y=y+1
    else:
        for y in range(y1,y2+1):
            glVertex2f(x,y)
            if(pk<0):
                pk=pk+c
            if(pk>=0):
                pk=pk+c-2*(y2-y1)
                x=x+1

    glEnd()
    glFlush()

def main():
    x1=int(input("Enter x1: "))
    x2=int(input("Enter x2: "))
    y1=int(input("Enter y1: "))
    y2=int(input("Enter y2: "))
    print("starting window...")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(250,250)
    glutCreateWindow("Bresenham's Algorithm")
    glutDisplayFunc(lambda: plot(x1,x2,y1,y2))
    glutIdleFunc(lambda: plot(x1,x2,y1,y2))
    init()
    glutMainLoop()

main()
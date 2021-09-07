from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def plot(x1,x2,y1,y2):
    dx=x2-x1
    dy=y2-y1
    m=dy/dx
    if(m<1):
        d=dy-(dx/2)
    else:
        d=dx-(dy/2)

    x=x1
    y=y1

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5,0.0,5.0)
    glPointSize(6.5)
    glBegin(GL_POINTS)

    if (m<1):
        for x in range(x1,x2+1):
            glVertex2i(x,y)
            if(d<0):
                d=d+dy
            else:
                d=d+dy-dx
                y=y+1
    else:
        for y in range(y1,y2+1):
            glVertex2i(x,y)
            if(d<0):
                d=d+dx
            else:
                d=d+dx-dy
                x=x+1

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
    glutCreateWindow("Mid-Point Line Drawing Algorithm")
    glutDisplayFunc(lambda: plot(x1,x2,y1,y2))
    glutIdleFunc(lambda: plot(x1,x2,y1,y2))
    init()
    glutMainLoop()

main()
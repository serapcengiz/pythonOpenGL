import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices=(
    (1,1,1),(1,-1,1),
    (-1,-1,1),(-1,1,1),
    (1,1,-1),(1,-1,-1),
    (-1,-1,-1),(-1,1,-1)
)
edges=(
    (0,1,2,3),
    (4,5,6,7),
    (0,1,5,4),
    (2,3,7,6),
    (0,3,7,4),
    (1,2,6,5)
)
colors=(
    (1,0,0) ,(0,1,0),(0,0,1),
    (1,0,1),(1,1,0),(0,1,1)
)

def sq():
    glBegin(GL_QUADS)
    for e,color, in zip(edges,colors):
        glColor(color)
        for vertex in e:
            glVertex3iv(vertices[vertex])
    glEnd()
def main():
    pygame.init()
    display=(600,600)
    pygame.display.set_mode(display,
                            DOUBLEBUF|OPENGL)
    gluPerspective(90,
                   display[0]/display[1],
                   1,150)
    glTranslatef(0,0,-5)
    glRotatef(60,1,0,0)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1,1,2,-1)

        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT|
                GL_DEPTH_BUFFER_BIT)
        sq()
        pygame.display.flip()
        pygame.time.wait(10)
main()
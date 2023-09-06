import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# OpenGL başlatma
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

# Pencereyi oluşturma
def create_window():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

# Üçgeni çizme
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex3fv((0, 1, 0))
    glVertex3fv((-1, -1, 0))
    glVertex3fv((1, -1, 0))
    glEnd()

# Ana döngü
def main():
    create_window()
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_triangle()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

import pygame
import math

#Setting up the variables
WIDTH, HEIGHT = 900, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# Radius of the Brush
radius = 5

#Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
GRAY = (128,128,128)

# Setting Title
pygame.display.set_caption('GFG Paint')

def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

#Figures functions
def draw_rect(screen, color, start, end, width = radius):
    x1, x2 = start[0], end[0]
    y1, y2 = start[1], end[1]
    height = abs(y1 - y2)
    widthr = abs(x1 - x2)
    pygame.draw.rect(screen, color, (x1, min(y1, y2), widthr, height), width)

def draw_circ(screen, colour, pos, center, width=radius):
    x1, y1 = center
    x2, y2 = pos
    radius_circ = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    pygame.draw.circle(screen, colour, center, radius_circ, width)

def draw_square(screen, colour, start, end, width = radius):
    c = 2**0.5
    x, y = start[0], start[1]
    x1, y1 = end[0], end[1]
    d = ((x1-x)**2 + (y1-y)**2)**0.5
    a = d/c
    pygame.draw.rect(screen, colour, (x,min(y,y1), a, a), width)

def draw_right(screen, colour, start, end, width = radius):
    x, y = start[0] , start[1]
    x1, y1 = end[0] , end[1]
    x2, y2 = x, y1
    points = [(x,y) , (x1,y1) , (x2,y2)]
    pygame.draw.polygon(screen, colour, points, width)


def draw_rhombus(screen , colour , start , end , width = radius):
    x, y = start[0], start[1]
    x1, y1 = end[0], end[1]
    d = ((x1-x)**2 + (y1-y)**2) ** 0.5
    xc, yc  = (x + x1)/2, (y+y1) / 2
    xr, yr = xc + d, yc
    xl, yl = xc - d, yc
    points = [(x,y) , (xl,yl) , (x1,y1) , (xr , yr)]
    pygame.draw.polygon(screen, colour, points , width)

def draw_equil(screen, colour, start, end, width = radius):
    x, y = start[0], start[1]
    x1, y1 = end[0], end[1]
    a = ((x1-x)**2 + (y1-y)**2) ** 0.5
    xc, yc = (x + x1)/2, (y+y1) / 2
    xv, yv = xc, yc - a
    points = [(x ,y), (x1,y1), (xv , yv)]
    pygame.draw.polygon(screen, colour, points, width)

def main():
    running = True
    draw_on = False
    last_pos = (0, 0)
    SCREEN.fill(WHITE)
    color = BLACK
    r_last_pos = (0, 0)
    center = (0, 0)

    #Figures variables
    isRect = False
    isCirc = False
    isSquare = False
    isRightTr = False
    isEquil = False
    isRhomb = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if isRect:
                    r_last_pos = event.pos
                elif isCirc:
                    center = event.pos
                elif isSquare:
                    r_last_pos = event.pos
                elif isRightTr:
                    r_last_pos = event.pos
                elif isRhomb:
                    r_last_pos = event.pos
                elif isEquil:
                    r_last_pos = event.pos
                else:
                    #Draw a single circle wheneven mouse is clicked down.
                    pygame.draw.circle(SCREEN, color, event.pos, radius)
                draw_on = True
            #When mouse button released it will stop drawing
            if event.type == pygame.MOUSEBUTTONUP :
                if isRect:
                    draw_rect(SCREEN,  color, r_last_pos , event.pos)
                elif isCirc:
                    draw_circ(SCREEN, color , event.pos, center)
                elif isSquare:
                    draw_square(SCREEN,  color, r_last_pos , event.pos)
                elif isRightTr:
                    draw_right(SCREEN,  color, r_last_pos, event.pos)
                elif isRhomb:
                    draw_rhombus(SCREEN,  color, r_last_pos, event.pos)
                elif isEquil:
                    draw_equil(SCREEN,  color, r_last_pos, event.pos)
                draw_on = False
            #It will draw a continuous circle with the help of roundline function.
            if event.type == pygame.MOUSEMOTION :
                if draw_on :
                    if not isRect and not isCirc and not isSquare and not isRightTr and not isEquil and not isRhomb:
                        pygame.draw.circle(SCREEN, color, event.pos, radius)
                        roundline(SCREEN, color, event.pos, last_pos, radius)
                last_pos = event.pos

            if event.type == pygame.KEYDOWN:
                #Color selection
                if event.key == pygame.K_r:
                    color = RED
                if event.key == pygame.K_g:
                    color = GREEN
                if event.key == pygame.K_b:
                    color = BLUE
                if event.key == pygame.K_c:
                    color = BLACK
                #Eraser
                if event.key == pygame.K_e:
                    color = WHITE
                
                #rectangle
                if event.key == pygame.K_1:
                    isRect = False
                    isCirc = False
                    isSquare = False
                    isRightTr = False
                    isEquil = False
                    isRhomb = False
                    isRect = True
                    if color == WHITE:
                        color = BLACK
                #circle
                if event.key == pygame.K_2:
                    isRect = False
                    isCirc = False
                    isSquare = False
                    isRightTr = False
                    isEquil = False
                    isRhomb = False
                    isCirc = True
                    if color == WHITE:
                        color = BLACK
                #Square
                if event.key == pygame.K_3:
                    isRect = False
                    isCirc = False
                    isSquare = False
                    isRightTr = False
                    isEquil = False
                    isRhomb = False
                    isSquare = True
                    if color == WHITE:
                        color = BLACK
                #Righ triangle
                if event.key == pygame.K_4:
                    isRect = False
                    isCirc = False
                    isSquare = False
                    isRightTr = False
                    isEquil = False
                    isRhomb = False
                    isRightTr = True
                    if color == WHITE:
                        color = BLACK
                #Euilateral
                if event.key == pygame.K_5:
                    isRect = False
                    isCirc = False
                    isSquare = False
                    isRightTr = False
                    isEquil = False
                    isRhomb = False
                    isEquil = True
                    if color == WHITE:
                        color = BLACK
                #Rhombus
                if event.key == pygame.K_6:
                    isRect = False
                    isCirc = False
                    isSquare = False
                    isRightTr = False
                    isEquil = False
                    isRhomb = False
                    isRhomb = True
                    if color == WHITE:
                        color = BLACK        
        pygame.display.flip()

if __name__ == '__main__':
    main()
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

def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

#Figures functions
def draw_rect(canvas, color, start, end, width = radius):
    x1 , x2 = start[0] , end[0]
    y1 , y2 = start[1] , end[1]
    height = abs(y1 - y2)
    widthr = abs(x1 - x2)
    pygame.draw.rect(canvas, color, (x1, min(y1, y2), widthr, height), width)

def draw_circ(screen, colour, pos, center, width=radius):
    x1, y1 = center
    x2, y2 = pos
    radius_circ = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    pygame.draw.circle(screen, colour, center, radius_circ, width)

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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if isRect:
                    r_last_pos = event.pos
                elif isCirc:
                    center = event.pos
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
                draw_on = False
            #It will draw a continuous circle with the help of roundline function.
            if event.type == pygame.MOUSEMOTION :
                if draw_on :
                    if not isRect and not isCirc:
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
                    isRect = True
                    if color == WHITE:
                        color = BLACK
                if event.key == pygame.K_2:
                    isRect = False
                    isCirc = False
                    isCirc = True
                    if color == WHITE:
                        color = BLACK
                
        pygame.display.flip()

if __name__ == '__main__':
    main()
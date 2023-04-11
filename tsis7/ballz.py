import pygame

pygame.init()
width = 1000
lenght = 1000
screen = pygame.display.set_mode((width, lenght))
done = False
ballz_color = (255,0,0)
x, y = 500, 500

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y-20 -25 >= 0: y -= 20
        if pressed[pygame.K_DOWN] and y + 20 + 25 <= lenght: y += 20
        if pressed[pygame.K_LEFT] and x-25-20 >= 0: x -= 20
        if pressed[pygame.K_RIGHT] and x + 20 + 25 <= width: x += 20

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, ballz_color, (x, y), 25)
        pygame.display.flip()

        clock.tick(60)
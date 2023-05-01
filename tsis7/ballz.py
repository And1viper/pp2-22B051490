import pygame

pygame.init()
width = 1000
lenght = 1000
screen = pygame.display.set_mode((width, lenght))
done = False
ballz_color = (255,0,0)
x, y = 500, 500

clock = pygame.time.Clock()

speed = 20

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y-min(speed, y-25)-25 >= 0: y -= min(speed, y-25)
        if pressed[pygame.K_DOWN] and y + min(speed, lenght-y-25) + 25 <= lenght: y += min(speed, lenght-y-25)
        if pressed[pygame.K_LEFT] and x-25-min(speed, x-25) >= 0: x -= min(speed, x-25)
        if pressed[pygame.K_RIGHT] and x + min(speed, width-x-25) + 25 <= width: x += min(speed, width-x-25)

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, ballz_color, (x, y), 25)
        pygame.display.flip()

        clock.tick(60)
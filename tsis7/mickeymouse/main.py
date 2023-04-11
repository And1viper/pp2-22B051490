import pygame
import time

def rotation(surf, image, pos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0], pos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

pygame.init()

width = 1400
length = 1050
screen = pygame.display.set_mode((width, length))
center = (width/2, length/2)

pygame.display.set_caption("Mickey Mouse Clock")
clock_img = pygame.image.load("./images/clock.jpeg")
minute_img = pygame.image.load("./images/right-hand.png")
second_img = pygame.image.load("./images/left-hand.png")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(clock_img, (0, 0))
    curr_time = time.localtime()
    print(curr_time)
    min_angle = curr_time.tm_min * 6 + curr_time.tm_sec / 10.0
    sec_angle = curr_time.tm_sec * 6

    rotation(screen, minute_img, center, -min_angle - 220)
    rotation(screen, second_img, center, -sec_angle - 220)

    pygame.display.flip()
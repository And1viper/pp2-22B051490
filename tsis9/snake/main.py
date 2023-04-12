import random
import pygame
import time
import sys

pygame.init()

#Setting the variables
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SPEED = 5
LEVEL = 0
SCORE = 0
clock = pygame.time.Clock()

#Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
YELLOW = (255,255,0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
PURPLE = (230, 230, 250)

#Setting up the fonts
font = pygame.font.SysFont("Verdana", 30)
font_large = pygame.font.SysFont("Verdana", 60)
game_over = font_large.render("Game Over", True, BLACK)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):
        #draw head part
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        #draw body part
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        #Move body
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x #position body[i] = body[i-1]
            self.body[idx].y = self.body[idx - 1].y
        #Move head
        self.body[0].x += dx
        self.body[0].y += dy

        #Check whether snake leaves the playing area
        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0
    
    #collision with food
    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True

class Food:
    def __init__(self, x, y, colour = GREEN, weight=1):
        self.location = Point(x, y)
        self.weight = weight
        self.colour = colour
        self.spawn_time = 0
        self.display_time = 0


    def draw(self):
        #Color depending on type
        if self.weight == 3:
            self.colour = PURPLE
        elif self.weight == 1:
            self.colour = GREEN
        elif self.weight == 2:
            self.colour = ORANGE
        elif self.weight == -1:
            self.colour = YELLOW

        pygame.draw.rect(
            SCREEN,
            self.colour,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

    #timed food
    def timedFood(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > 7000:
            self.spawn_time = current_time
            self.location = Point(random.randint(1, WIDTH // BLOCK_SIZE - 2), random.randint(1, HEIGHT // BLOCK_SIZE - 2))
            self.display_time = current_time
        if current_time - self.display_time < 4000:
            self.draw()

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRAY, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRAY, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    poison = Food(7, 7, weight = -1)
    t_food = Food(2, 2, weight = 3)
    dx, dy = 0, 0
    direction = ''

    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'down':
                    dx, dy = 0, -1
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction != 'up':
                    dx, dy = 0, +1
                    direction = 'down'
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    dx, dy = 1, 0
                    direction = 'right'
                elif event.key == pygame.K_LEFT and direction != 'right':
                    dx, dy = -1, 0
                    direction = 'left'

        snake.move(dx, dy)
        if snake.check_collision(food):
            global SCORE, SPEED, LEVEL
            for i in range(food.weight):
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
            SCORE += food.weight
            SPEED = 5 * (SCORE//4 + 1)
            LEVEL = 1 * (SCORE//4 + 1)
            #Check the food generation
            while True:
                check_food_col = False
                x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                for cell in snake.body:
                    if x != cell.x and y != cell.y:
                        food.location.x = x
                        food.location.y = y
                        check_food_col = True
                if check_food_col:
                    break
            food.weight = random.randint(1, 2)

        #Collision with posion
        if snake.check_collision(poison):
            snake.body.pop()
            SCORE += poison.weight
            SPEED = 5 * (SCORE//4 + 1)
            LEVEL = 1 * (SCORE//4 + 1)
            #Check the food generation
            while True:
                check_food_col = False
                x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                for cell in snake.body:
                    if x != cell.x and y != cell.y and x != food.location.x and y != food.location.y:
                        poison.location.x = x
                        poison.location.y = y
                        check_food_col = True
                if check_food_col:
                    break
        
        #Collision with timed food
        if snake.check_collision(t_food):
            for i in range(t_food.weight):
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
            SCORE += t_food.weight
            SPEED = 5 * (SCORE//4 + 1)
            LEVEL = 1 * (SCORE//4 + 1)
            #Check the food generation
            while True:
                check_food_col = False
                x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                for cell in snake.body:
                    if x != cell.x and y != cell.y:
                        t_food.location.x = x
                        t_food.location.y = y
                        check_food_col = True
                if check_food_col:
                    break

        #Timed food
        t_food.timedFood()

        #Show the level and score on the screen
        scores = font.render(str(SCORE), True, RED)
        level = font.render(str(LEVEL), True, RED)
        SCREEN.blit(scores, (10, 10))
        SCREEN.blit(level, (WIDTH - 30, 10))

        #Appearence of poison
        if SCORE % 3 == 1:
            poison.draw()
        snake.draw()
        food.draw()
        draw_grid()
        pygame.display.flip()
        clock.tick(SPEED)


if __name__ == '__main__':
    main()
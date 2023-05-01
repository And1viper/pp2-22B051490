import random
import pygame
from config import config
import psycopg2
import sys
import time

name = input("Enter the name: ")

#create databases
def create_databases():
    sql_query_users = "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username varchar(30))"
    sql_query_user_scores = "CREATE TABLE IF NOT EXISTS user_scores (id SERIAL PRIMARY KEY, user_id int, level int, score int, position varchar(1200), direction varchar(10))"
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql_query_user_scores)
        cur.execute(sql_query_users)

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

pygame.init()

#Setting the variables
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SPEED = 5
LEVEL = 0
SCORE = 0
USER_ID = 0
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
BROWN = (139, 69, 19, 255)

#Setting up the fonts
font = pygame.font.SysFont("Verdana", 30)
font_large = pygame.font.SysFont("Verdana", 60)
game_over = font_large.render("Game Over", True, BLACK)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #operator overload for eq
    def __eq__(self, another):
        if self.x == another.x and self.y == another.y:
            return True
        return False

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
        self.direction = "left"

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
    
    #deadly collision, i.e. with walls
    def check_collision_walls(self, walls):
        cnt = 0
        for wall in walls:
            if wall.x != self.body[0].x or wall.y!=  self.body[0].y:
                cnt += 1
        if cnt == len(walls):
            return False
        return True

    #collision with snake
    def check_collision_snake(self):
        cnt = 0
        for i in range(1, len(self.body)):
            if self.body[i].x != self.body[0].x or self.body[i].y!=  self.body[0].y:
                cnt += 1
        if cnt == len(self.body) - 1:
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
    def timedFood(self, poison, food, snake_body, walls_walls):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > 7000:
            self.spawn_time = current_time
            self.location = rand_food(poison, food, self, snake_body, walls_walls)
            self.display_time = current_time
        if current_time - self.display_time < 4000:
            self.draw()
        else:
            self.location = Point(-1,-1)

class Wall():
    def __init__(self):
        self.walls = []
    
    def load_wall(self, level=0):
        self.walls = []
        path = "./levels/l"+str(level)+".txt"
        with open(path, 'r') as f:
            wall_body = f.readlines()
        
        for i, line in enumerate(wall_body):
            for j, value in enumerate(line):
                if value == '#':
                    self.walls.append(Point(j, i))
    
    def draw(self):
        self.load_wall(LEVEL)
        for wall in self.walls:
            pygame.draw.rect(SCREEN, BROWN, (wall.x * BLOCK_SIZE, wall.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRAY, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, GRAY, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

#From list to str parser
def list_to_str(lst):
    string = ""
    for item in lst:
        string += "" + str(item.x) +"," + str(item.y) + ";"
    return string[:len(string)-1]

#From str to list parser
def str_to_list(string):
    lst = []
    points = string.split(";")
    for point in points:
        point_splitted = point.split(",")
        x = int(point_splitted[0])
        y = int(point_splitted[1])
        lst.append(Point(x, y))
    return lst

#Get all the information about user
def get_values(username, snake):
    global LEVEL, SCORE, USER_ID

    sql_query_exist = "SELECT * FROM users INNER JOIN user_scores ON users.id = user_scores.user_id WHERE username = %s"
    sql_query_new_user = ''' INSERT INTO users (username)
                    VALUES (%s) '''
    sql_query_new_user_scores = ''' INSERT INTO user_scores (user_id, level, score, position, direction)
                    VALUES (%s, %s, %s, %s, %s) '''
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute(sql_query_exist, (username,))
        result = cur.fetchone()

        if result:
            USER_ID = result[0]
            LEVEL = int(result[4])
            SCORE = int(result[5])
            snake.body = str_to_list(result[6])
            snake.direction = str(result[7])

        else:
            cur.execute(sql_query_new_user, (username,))
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            result = cur.fetchone()
            USER_ID = result[0]
            cur.execute(sql_query_new_user_scores, (USER_ID, 0, 0, "10,10;11,10", "left"))
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#Score update
def update_score(lvl, score, snake_body, snake_direction):
    global USER_ID
    sql_query = "UPDATE user_scores SET level = %s, score = %s, position = %s, direction = %s WHERE user_id = %s"
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql_query, (lvl, score, list_to_str(snake_body), snake_direction, USER_ID))
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#random food generation
def rand_food(poison, food, t_food, snake, walls):
    x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
    y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
    food_block = Point(x,y)
    while food_block in snake or food_block in walls or food_block == poison.location or food_block == food.location or food_block == t_food.location:
        food_block.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        food_block.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
    return food_block


def main():
    global SCORE, SPEED, LEVEL
    #databases
    create_databases()

    running = True
    pause = False
    is_started_moving = False
    snake = Snake()
    food = Food(5, 5)
    poison = Food(7, 7, weight = -1)
    t_food = Food(12, 12, weight = 3)
    walls = Wall()
    dx, dy = 0, 0
    get_values(name, snake)
    INIT_LEVEL = LEVEL

    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause
                    if pause:
                        update_score(LEVEL, SCORE, snake.body, snake.direction)
                elif event.key == pygame.K_UP and snake.direction != 'down':
                    is_started_moving = True
                    dx, dy = 0, -1
                    snake.direction = 'up'
                elif event.key == pygame.K_DOWN and snake.direction != 'up':
                    is_started_moving = True
                    dx, dy = 0, +1
                    snake.direction = 'down'
                elif event.key == pygame.K_RIGHT and snake.direction != 'left':
                    is_started_moving = True
                    dx, dy = 1, 0
                    snake.direction = 'right'
                elif event.key == pygame.K_LEFT and snake.direction != 'right':
                    is_started_moving = True
                    dx, dy = -1, 0
                    snake.direction = 'left'
                       
        if pause:
            continue
        
        #Update all variables
        if LEVEL - INIT_LEVEL == 1:
            INIT_LEVEL = LEVEL
            food.location = rand_food(poison, food, t_food, snake.body, walls.walls)
            poison.location = rand_food(poison, food, t_food, snake.body, walls.walls)
            t_food.location = rand_food(poison, food, t_food, snake.body, walls.walls)

        SPEED = 5 * (SCORE//4 + 1)
        LEVEL = 1 * (SCORE//4 + 1)

        #Until the first key is pressed don't move
        if is_started_moving:
            snake.move(dx, dy)

        if snake.check_collision(food):
            for i in range(food.weight):
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
            SCORE += food.weight
            #Check the food generation
            food.location = rand_food(poison, food, t_food, snake.body, walls.walls)
            food.weight = random.randint(1, 2)

        #Collision with posion
        if snake.check_collision(poison) and SCORE % 3 == 1:
            snake.body.pop()
            SCORE += poison.weight
            #Check the food generation
            poison.location = rand_food(poison, food, t_food, snake.body, walls.walls)
        
        #Collision with timed food
        if snake.check_collision(t_food):
            for i in range(t_food.weight):
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
            SCORE += t_food.weight
            #Check the food generation
            t_food.location = rand_food(poison, food, t_food, snake.body, walls.walls)
            

        #Game over conditions
        if snake.check_collision_walls(walls.walls) or snake.check_collision_snake() or SCORE < 0:
            time.sleep(1)
            update_score(0, 0, [Point(10,10), Point(11,10)], "left")
            SCREEN.fill(WHITE)
            SCREEN.blit(game_over, (WIDTH//2-150, HEIGHT//2-50))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()

        #MAX LEVEL
        if LEVEL >= 3:
            LEVEL = 2

        walls.draw() 
        #Timed food
        t_food.timedFood(poison, food, snake.body, walls.walls)

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
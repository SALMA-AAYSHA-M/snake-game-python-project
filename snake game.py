import turtle
import random

w = 800
h = 500
food_size = 15
delay = 100

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset():
    global snake, snake_dir, food_position, pen, score
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    score = 0
    update_score()
    move_snake()

def move_snake():
    global snake_dir, score

    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]

    if new_head in snake[:-1]:
        game_over()
    else:
        snake.append(new_head)

        if not food_collision():
            snake.pop(0)

        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h

        pen.clearstamps()

        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()
        turtle.ontimer(move_snake, delay)

def food_collision():
    global food_position, score
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        score += 1
        update_score()
        return True
    return False

def get_random_food_position():
    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"

def update_score():
    score_pen.clear()
    score_pen.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

def game_over():
    pen.clear()
    pen.goto(0, 0)
    pen.write("Game Over", align="center", font=("Arial", 36, "normal"))
    score_pen.goto(0, -50)
    score_pen.write(f"Final Score: {score}", align="center", font=("Arial", 24, "normal"))

screen = turtle.Screen()
screen.setup(w, h)
screen.title("SNAKE GAME")
screen.bgcolor("violet")
screen.setup(500, 500)
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("black")
food.shapesize(food_size / 20)
food.penup()

score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(0, h / 2 - 40)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset()
turtle.done()

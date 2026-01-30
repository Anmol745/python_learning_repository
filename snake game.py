import turtle
import time
import random

# ---------------- CONFIG ----------------
delay = 0.1
score = 0
high_score = 0

# ---------------- SCREEN SETUP ----------------
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# ---------------- SNAKE HEAD ----------------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ---------------- FOOD ----------------
food = turtle.Turtle()
food.speed(0)
food.shape(random.choice(["square", "circle", "triangle"]))
food.color(random.choice(["red", "green", "black"]))
food.penup()
food.goto(0, 100)

segments = []

# ---------------- SCOREBOARD ----------------
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Candara", 24, "bold"))

# ---------------- FUNCTIONS ----------------
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# ---------------- KEYBOARD BINDINGS ----------------
wn.listen()wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# ---------------- MAIN GAME LOOP ----------------
while True:
    wn.update()

    # Border collision
    if (
        head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Candara", 24, "bold"))

    # Food collision
    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Candara", 24, "bold"))

    # Move body
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}",
                      align="center", font=("Candara", 24, "bold"))

    time.sleep(delay)

wn.mainloop()

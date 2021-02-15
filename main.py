from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def play():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Snake Snake")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(.1)
        snake.move()

    # Detect Collision with food
        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            snake.extend()
            food.refresh()
            print("nom nom nom")

    # Detect Collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset_score()
            snake.reset_snake()
            answer = screen.textinput("Replay?", "Y/N").lower()
            if answer == "y":
                screen.clear()
                play()
            else:
                screen.bye()

    # Detect Collision with Tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                scoreboard.reset_score()
                snake.reset_snake()
                answer = screen.textinput("Replay?", "Y/N").lower()
                if answer == "y":
                    screen.clear()
                    play()
                else:
                    screen.bye()
    screen.exitonclick()



play()

# TODO: Create a snake body
# TODO: Move the snake
# TODO: Control the snake (keyboards)
# TODO: Detect collision with the food
# TODO: Create a scoreboard
# TODO: Detect collision with the wall
# TODO: Detect collision with tail


""""
notes:
difference between time.sleep() and turtle.delay():
time.sleep()- using sleep() to halt the code execution for a given number of seconds
turtle.delay() - is used to return or set the drawing delay in milliseconds.

difference between turtle.left() and turtle.setheading(180):
Turn turtle left by angle units, Angle orientation depends on the turtle mode.
Set the orientation of the turtle, Angle orientation is not depends on the turtle mode.


Why are the onkey functions outside the while loop?
because the events are on the screen.  Once they are added they are listening for a key press
all the time,no matter what you draw.
When you add listeners inside the loop you are adding the listeners again each time through the loop.
It works but it's not efficient.

"""""

import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

win = Screen()
win.setup(width=600, height=600)
win.bgcolor("black")
win.title("Snake Game")
win.tracer(0)  # turns automatic screen updates off and also sets the update() delay.

snake = Snake()
food = Food()
scoreboard = Scoreboard()

win.listen()  # listen to all possible types of player inouts
win.onkeypress(snake.turn_up, "Up")
win.onkeypress(snake.turn_down, "Down")
win.onkeypress(snake.turn_left, "Left")
win.onkeypress(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    snake.move()
    time.sleep(0.1)  # the program waits one second after each segment moves and so on

    #  When automatic updates are off, you need to explicitly call update()
    #  when you want the screen to reflect the current state of the drawing.
    win.update()

    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall:
    if abs(snake.head.xcor()) > 270 or abs(snake.head.ycor()) > 270:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail:
    # if head collides with any segment in the tail --> trigger game over
    for segment in snake.body_snake[2:]:  # Iterate over the segments except of the head
        if snake.head.distance(segment) < 20:
            scoreboard.reset()
            snake.reset()

win.exitonclick()

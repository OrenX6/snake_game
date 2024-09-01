from turtle import Turtle

# if we want to tweak our game we don't have to dig through the body of our code,
# we just change our constants accordingly.

SNAKE_SIZE = 3  # initial size
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def play_again():
    return True


class Snake:
    """
    A class to represent a snake.

    Attributes:
    ----------
    body_snake : list
      snake body (segments) - each item is Turtle object
    head : Turtle object
        family name of the person

    """

    # What should happen when you initialized a new snake object
    def __init__(self):  # default constructor

        self.body_snake = []  # default attribute - may be changed in the future
        self.create_snake()
        self.head = self.body_snake[0]

    # three segments snake will show up on the screen
    def create_snake(self):
        """
        create the initial segments on the screen and update the snake body.
        """

        for i in range(SNAKE_SIZE):
            x = i * (- MOVE_DISTANCE)
            self.add_segment((x, 0))

    def add_segment(self, position):
        """
        create one segment for each call

        :param position:
        :return: None
        """
        segment = Turtle(shape="square")
        segment.color("black", "blue")
        segment.penup()
        segment.goto(position)  # updated and changed during the runtime
        self.body_snake.append(segment)

    def extend(self):
        """
        add one segment at the end of the snake body
        """
        self.add_segment(self.body_snake[-1].position())

    def reset(self):
        """
        reset the snake body - delete all segments and create new ones
        :return:
        """
        for square in self.body_snake:
            square.hideturtle()
        self.body_snake.clear()
        self.create_snake()
        self.head = self.body_snake[0]

    def move(self):
        """
        move each segment of the snake body
        """

        for i in range(len(self.body_snake) - 1, 0, -1):
            self.body_snake[i].goto(self.body_snake[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


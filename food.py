import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):  # override
        super().__init__()
        self.shape("circle")  # method of turtle class
        self.penup()
        # stretch the turtle along its length and along its width (default size: 20x20)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10x10
        self.color("red")
        self.speed("fastest")  # drawing speed
        self.refresh()

    def refresh(self):
        """
         create a new random  location (x,y) and get the food to go to that new random location
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

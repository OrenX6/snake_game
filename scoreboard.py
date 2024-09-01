from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')  # more convenient to change (if we want)


class Scoreboard(Turtle):

    def __init__(self):  # override
        super().__init__()
        self.score = 0
        with open("data.txt") as data:  # file object
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto((0, 270))
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        delete the previous scoreboard from the screen and update the new one
        """
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        reset the score points to zero and update the highest score.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER !', align=ALIGNMENT, font=FONT)
        self.sety(-30)

    def increase_score(self):
        """
        increase the score by one point
        """
        self.score += 1
        self.update_scoreboard()



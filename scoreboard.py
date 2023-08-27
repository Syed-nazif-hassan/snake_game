from turtle import Turtle


ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("scores_list.txt") as file:
            self.data = int(file.read())
        self.score = 0
        self.high_score = self.data
        self.color("white")
        self.penup()
        self.goto(-260, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} high score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("scores_list.txt", mode="w")
            file.write(f"{self.high_score}")
            file.close()
        self.score = 0
        self.update_scoreboard()

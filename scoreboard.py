from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 17, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("purple")
        self.penup()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()




    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("green")
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)



    def increase_score(self):
        self.score += 1
        self.update_scoreboard()





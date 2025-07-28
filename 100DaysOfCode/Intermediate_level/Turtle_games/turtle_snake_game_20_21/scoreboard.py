from turtle import Turtle
BOARD_POSITION = (0, 260)
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
GAMEOVER_FONT = ("Courier", 20, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(BOARD_POSITION)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        
        
    def update_score(self):
        self.clear()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAMEOVER_FONT)

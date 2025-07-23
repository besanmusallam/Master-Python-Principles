from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")
GAMEOVER_FONT = ("Courier", 40, "bold")

class ScoreBoard(Turtle):

    def __init__(self, number, BOARD_POSITION):
        super().__init__()
        self.clear()
        self.hideturtle()
        self.score = 0
        self.number = number
        self.penup()
        self.board_position = BOARD_POSITION
        self.color("white")
        self.goto(self.board_position)
        self.write(self.score, align=ALIGNMENT, font=FONT)
        
        
    def update_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # def winner(self):
    #     self.goto(0, 0)
    #     self.write(f"Player {self.number} is the winner", align=ALIGNMENT, font=GAMEOVER_FONT)

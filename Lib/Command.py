from random import choice


class Command:
    user_move = ""

    def __init__(self, um):
        self.user_move = um
    
    def computerMove(self):
        print(choice(['Paper','Scissor','Rock']))

    def hello(self):
        print("hello")
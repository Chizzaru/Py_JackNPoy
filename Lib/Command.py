from random import choice
import sys


class Command:
    user_move = ""

    def __init__(self, um):
        self.user_move = um
    
    def computerMove(self):
        cmove = choice(['Paper','Scissor','Rock'])
        umove = ""
        if int(self.user_move) == 1:
            umove = 'Paper'
        elif int(self.user_move) == 2:
            umove = 'Scissor'
        elif int(self.user_move) == 3:
            umove = 'Rock'
        else:
            print('ERROR : Selection out of range!')
            sys.exit()
        
        
        print("\nYou picked \"" + umove + "\", Computer picked \"" + cmove + "\"\n")
        
        if cmove == umove:
            print("DRAW")
        elif umove == 'Paper' and cmove == 'Scissor':
            print('YOU LOSE')
        elif umove == 'Rock' and cmove == 'Paper':
            print('YOU LOSE')
        elif umove == 'Scissor' and cmove == 'Rock':
            print('YOU LOSE')
        elif umove == 'Scissor' and cmove == 'Paper':
            print('YOU WIN')
        elif umove == 'Rock' and cmove == 'Scissor':
            print('YOU WIN')
        elif umove == 'Paper' and cmove == 'Rock':
            print('YOU WIN')
        


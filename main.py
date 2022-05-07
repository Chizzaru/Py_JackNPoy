import sys
sys.path.append(".")

from Lib.Command import Command
from Lib.Choices import Choices

if __name__ == "__main__":
    Choices.printChoices()
    umove = input("Type the number of move you choose : ")
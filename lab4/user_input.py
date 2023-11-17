import termcolor
from termcolor import COLORS

class UserInput:
    def __init__(self):
        self.text = "Test"
        self.color = 'red'
        self.size = 1
        self.char = '@'

    def get_user_input(self):
        try:
            self.text = str(input("Enter text: "))
            self.color = input("Enter color: ")
            if self.color not in termcolor.COLORS:
                raise ValueError
            self.size = int(input("Enter size modifier: "))
            self.char = input("Enter char: ")
        except ValueError:
            self.text = "Test"
            self.color = 'red'
            self.size = 1
            self.char = '@'
            
        return self.text, self.color, self.size, self.char

        
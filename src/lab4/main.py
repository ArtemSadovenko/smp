from dictinary import init_dictionary
from termcolor import COLORS, colored
from drawer import Drawer
from user_input import UserInput


def main():
    ask = 'y'
    user_input = UserInput()

    while ask == 'y':
        text, color, size, char = user_input.get_user_input()
        drawer = Drawer(text, color, size, char)
        res = drawer.draw()
        print(res)
        isSave = input("Save the art? (y/n)")
        if(isSave == 'y'):
            with open("lab4\text_out.txt", 'w') as f:
                f.write(res)
        ask = input("draw again?(y/n)")

if __name__ == "__main__":
    main()
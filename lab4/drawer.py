from dictinary import init_dictionary
import termcolor
from termcolor import COLORS, colored

class Drawer:
    def __init__(self, text, color, size, char):
        self.text = text
        self.color = color
        self.size = size
        self.char = char
        self.dictionary = init_dictionary()

    def draw(self):
        art = self.create_msg(self.prepare_for_print(self.text), self.char, self.text)
        with open("text.txt", 'w') as file:
            file.write(art)

        res = ''

        with open('text.txt', 'r') as f:
            for line in f:
                output = "".join([self.size * c for c in line.strip()])
                for _ in range(self.size):
                    res = res + output + '\n'

        if(self.char != ' '):
            modified = ''
            for letter in res:
                if letter == ' ' or letter == '\n':
                    modified += letter
                else:
                    modified += self.char
            res = modified

        return colored(res, self.color)

    def prepare_for_print(self, text):
        letter_list = list() 
        char_arr = list()
        dic = init_dictionary()
        arr = list()

        for char in text:
            arr.append(dic[char])

            
        for j in range(5):
            for i in range(len(text)):
                letter_list.append(arr[i][j])

        for mas in letter_list:
            for i in mas:
                char_arr.append(i)
            char_arr.append(0)

        return char_arr
    
    def create_msg(self, arr, char, text):
        res = ""
        for i in range(len(arr)):
            if(i % (6*len(text)) == 0):
                res += '\n'
            if(arr[i] == 1):
                res += char
            else:
                res += ' '

        return res

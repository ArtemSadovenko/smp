from termcolor import colored, COLORS

class DrawRectangle:
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color

    def cline(self, n, x, y, cde):
        print(
            colored(
            f"{str(cde[0]).rjust(n + 1)}" +
            f"{cde[1] * (9 * x - 1)}" +
            f"{cde[0]}" +
            f"{str(cde[2]).rjust(y + 1) if len(cde) > 2 else ''}"
        , self.color))

    def draw_rectangle(self):
        self.cline(self.y + 1, self.x, 0, '+-')

        for i in range(1, self.y):
            self.cline(self.y - i + 1, self.x, i - 1, '/ |')

        self.cline(0, self.x, self.y, '+-|')

        for _ in range(4 * self.z - self.y - 3):
            self.cline(0, self.x, self.y, '| |')

        self.cline(0, self.x, self.y, '| +')

        for i in range(self.y - 1, 0, -1):
            self.cline(0, self.x, i, '| /')

        self.cline(0, self.x, 0, "+-\n")
        
    def proect(self):
        for i in range(0, self.y):
            print("")
            for j in range(0, self.x):
                if (i == 0 or i == self.y-1) and (j == 0 or j == self.x-1):
                    print(colored("+", self.color), end="")
                elif i == 0 or i == self.y-1:
                    print(colored("-", self.color), end="")
                elif j == 0 or j == self.x-1:
                    print(colored("|", self.color), end="")
                else:
                    print(" ", end="")



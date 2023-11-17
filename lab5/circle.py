# import math
# from math import *
# class CircleDrawer:
#     def __init___(self, radius):
#         self.shades = shades = ['.', ':', '!', '*', 'o', 'e', '&', '#', '%', '@']

    
#     def draw(self):
#         for i in range(int(math.floor(-self.r)), int(math.ceil(self.r) + 1)):
#             x = i + 0.5
#             line = ''

#             for j in range(int(math.floor(-2 * r)), int(math.ceil(2 * r) + 1)):
#                 y = j / 2 + 0.5
#                 if x * x + y * y <= r * r:
#                     vec = normalize((x, y, math.sqrt(r * r - x * x - y * y)))
#                     b = dotp(light, vec) ** k + ambient
#                     intensity = int((1 - b) * (len(shades) - 1))
#                     line += shades[intensity] if 0 <= intensity < len(shades) else shades[0]
#                 else:
#                     line += ' '

#             print(line)


#     def normalize(self, v):
#         length = math.sqrt(sum(x ** 2 for x in v))
#         return tuple(x / length for x in v)

import math
from termcolor import colored, COLORS

class DrawSphere:
    def __init__(self, ambient, color, r, k):
        self.shades  = ['.', ':', '!', '*', 'o', 'e', '&', '#', '%', '@']
        self.ambient = ambient
        self.light =  [30.0, 30.0, -50.0]
        self.r = r
        self.k = k
        self.color = color

    def dotp(self, v1, v2):
        d = sum(x * y for x, y in zip(v1, v2))
        return max(-d, 0.0)

    def draw_sphere(self):
        res = ''
        for i in range(int(math.floor(-self.r)), int(math.ceil(self.r) + 1)):
            x = i + 0.5
            line = ''

            for j in range(int(math.floor(-2 * self.r)), int(math.ceil(2 * self.r) + 1)):
                y = j / 2 + 0.5
                if x * x + y * y <= self.r * self.r:
                    vec = self.normalize((x, y, math.sqrt(self.r * self.r - x * x - y * y)))
                    b = self.dotp(self.light, vec) ** self.k + self.ambient
                    intensity = int((1 - b) * (len(self.shades) - 1))
                    line += self.shades[intensity] if 0 <= intensity < len(self.shades) else self.shades[0]
                else:
                    line += ' '
            res += line
            res += '\n'
            print(colored(line, self.color))
        return res

    def normalize(self, v):
        length = math.sqrt(sum(x ** 2 for x in v))
        return tuple(x / length for x in v)
    
    def proect(self):
        ambient = self.k
        self.k = 0.0
        for i in range(int(math.floor(-self.r)), int(math.ceil(self.r) + 1)):
            x = i + 0.5
            line = ''

            for j in range(int(math.floor(-2 * self.r)), int(math.ceil(2 * self.r) + 1)):
                y = j / 2 + 0.5
                if x * x + y * y <= self.r * self.r:
                    vec = self.normalize((x, y, math.sqrt(self.r * self.r - x * x - y * y)))
                    b = self.dotp(self.light, vec) ** self.k + self.ambient
                    intensity = int((1 - b) * (len(self.shades) - 1))
                    line += self.shades[intensity] if 0 <= intensity < len(self.shades) else self.shades[0]
                else:
                    line += ' '

            print(colored(line, self.color))
        self.k = ambient




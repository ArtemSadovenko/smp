from circle import DrawSphere
from rectangle import DrawRectangle
from termcolor import colored, COLORS

def rec_input():
    try:
        x = int(input("Enter the width (x) of the rectangle: "))
        y = int(input("Enter the height (y) of the rectangle: "))
        z = int(input("Enter the depth (z) of the rectangle: "))
        color = input("Enter the color of the rectangle: ")

        if color not in COLORS:
            raise ValueError("Invalid color")

        return x, y, z, color

    except ValueError as e:
        print(f"Error: {e}. Using default values.")
        return 5, 5, 3, 'green'  # Default values

def shp_input():
        try:
            ambient = float(input("Enter the ambient value (default is 0.7): ") or 0.7)
            r = float(input("Enter the radius of the sphere (default is 20): ") or 20)
            k = float(input("Enter the k value (default is 4): ") or 4)
            color = input("Enter the color of the sphere (default is green): ") or 'green'

            if color not in COLORS:
                raise ValueError("Invalid color")

            return ambient, r, k, color
        except ValueError as e:
            print(f"Error: {e}. Using default values.")

def main():
    draw_sp = DrawSphere(0.7, 'red', 5, 6)
    draw_sp.draw_sphere()
    draw_sp.proect()
    # draw_rec = DrawRectangle(3,3,3,'red')
    # draw_rec.draw_rectangle()
    # draw_rec.proect()
    # key = True
    # while(key):
    #     ch = input("Draw sphere or rectangle?(s/r)")
    #     if(ch == 's' or ch == 'r'):
    #         key = False
    # if(ch == 's'):
    #     ambient, r, k, color = shp_input()
    #     draw_sp = DrawSphere(ambient, color, r, k)
    #     res = draw_sp.draw_sphere()
    #     # print(colored(res, draw_sp.color))
    #     draw_sp.proect()
    #     isSave = input("Save the art? (y/n)")
    #     if(isSave == 'y'):
    #         with open("shere.txt", 'w') as f:
    #             f.write(res)
    # else:
    #     x, y, z, color = rec_input()
    #     draw_rec = DrawRectangle(x, y, z, color)
    #     draw_rec.draw_rectangle()
    #     draw_rec.proect()
    #     isSave = input("Save the art? (y/n)")
    #     if(isSave == 'y'):
    #         with open("rec.txt", 'w') as f:
    #             f.write(res)


if __name__ == "__main__":
    main()

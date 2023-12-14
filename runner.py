import sys
import os

# Get the absolute path to the directory containing runner.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from src import *
from src.lab1 import lab1 as lab1
from src.lab2 import  main as lab2
from src.lab3 import drawer as lab3 
from src.lab4 import main as lab4
from src.lab5 import main as lab5
from src.lab6 import main as lab6
from src.lab7 import main as lab7


def main():
    print('Choose lab:')
    print('1. Lab1')
    print('2. Lab2')
    print('3. Lab3')
    print('4. Lab4')
    print('5. Lab5')
    print('6. Lab6')    
    print('7. Lab7')
    

    user_input = input('Enter option number: ')

    while(user_input not in ['1','2','3','4','5','6','7']):
        user_input = input('Enter option number: ')
    
    if user_input == '1':
        print(f"Lab1: {(lab1.main())}")
    if user_input == '2':
        print(f"Lab2: {lab2.main()}")
    if user_input == '3':
        print(f"Lab3: {lab3.main()}")
    if user_input == '4':
        print(f"Lab4: {lab4.main()}")
    if user_input == '5':
        print(f"Lab5: {lab5.main()}")
    if user_input == '6':
        print(f"Lab6: {lab6.main()}")
    if user_input == '7':
        print(f"Lab6: {lab7.main()}")
     
if __name__ == "__main__":
    main()

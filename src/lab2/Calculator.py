import math

class Calculator:
    def __init__(self):
        self.history = []
        self.result = 0.0
        self.use_history = False
        self.use_result = False
        self.decNum = 2

    def get_user_input(self):
        ask = True
        while ask:
            try:
                if self.use_result and self.is_result_exists:
                    num1 = self.result
                else:
                    num1 = float(input("Enter num1: "))
                operator = input("Choose operation (+, -, *, /, ^, sqrt, %): ")
                if operator not in ('+', '-', '*', '/', '^', 'sqrt', '%'):
                    print("Bad request")
                    return None, None, None
                num2 = float(input("Enter num2: "))

                return num1, operator, num2

            except ValueError:
                print("Enter float")

    def calculate_result(self, num1, operator, num2):
        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            elif operator == '^':
                result = num1 ** num2
            elif operator == 'sqrt':
                result = math.sqrt(num1)
            elif operator == '%':
                result = num1 % num2

            self.result = result
            self.is_result_exists = True

            return result

        except ZeroDivisionError:
            print("Zero Division")
            return -1
            

    def run_calculator(self):
        while True:
            num1, operator, num2 = self.get_user_input()
            if num1 is None or operator is None or num2 is None:
                continue

            result = self.calculate_result(num1, operator, num2)
            print(f"{result:.{self.decNum}f}")

            info = f'{num1}{operator}{num2}={result}'
            self.history.append(info)
            if self.use_history:
                print("History:", self.history)

            if input("Continue? (Y/N)? ").lower() != 'y':
                break

            if input("Advanced? (Y/N)").lower == "y":
                self.use_result = input("Default use old result? (Y/N)").lower == 'y'
                self.use_history = input("Default use history? (Y/N)").lower == 'y'
                self.decNum = int(input("Set decimal places: "))

            self.is_result_exists = True
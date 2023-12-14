import math

history = [] 
result = 0.0
useHistory = False
useRes = False
decNum = 2

def main():
    while True:
            try:
                if(useRes and isResultExists): 
                    num1 = result
                else:
                    num1 = float(input("Enter num1: "))
                operator = input("Choose operation (+, -, *, /, ^, sqrt, %): ")
                if operator not in ('+', '-', '*', '/', '^', 'sqrt', '%'):
                    print("Bad request")
                    continue
                num2 = float(input("Enter num2: "))

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
                info = f'{num1}{operator}{num2}={result}'
                history.append(info)
                print("Result:", f"{result:.{decNum}f}")

                if(useHistory):
                    print("History: ", history)
            

                if input("Contue? (Y/N)? ").lower() != 'y':
                    break
                if input("Advanced? (Y/N)") == "Y":
                    useRes = input("Default use old result? (Y/N)") == 'Y'
                    useHistory = input("Default use history? (Y/N)") == 'Y'
                    decNum = int(input("Set dec num: "))
                isResultExists = True
            except ValueError:
                print("Enter float")
            except ZeroDivisionError:
                print("Zero Division")
            except Exception as e:
                print("Error:", e)

if __name__ == '__main__':
    main()
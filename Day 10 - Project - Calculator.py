logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def div(num1, num2):
    return num1 / num2


def mul(num1, num2):
    return num1 * num2


def validateFloat(num):
    while True:
        try:
            return float(num)
        except ValueError:
            num = input("Incorrect numbers format. Try again: ")


def validateOperator(operator):
    validoperators = ["+", "-", "/", "*"]
    while True:
        if operator in validoperators:
            return operator
        else:
            operator = input("Incorrect operator. Try again: ")


def calculateResults(num1, num2, operator):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return sub(num1, num2)
    elif operator == "/":
        return div(num1, num2)
    else:
        return mul(num1, num2)


print(logo)
programRunning = True
while programRunning:
    firstNum = validateFloat(input("Enter the first number: "))
    print("+\n-\n/\n*")
    while True:
        operation = validateOperator(input("Pick an operation: "))
        secondNum = validateFloat(input("Enter the second number: "))
        if operation == "/" and secondNum == 0:
            print("Cannot divide by zero. Try again.")
            continue
        calculation = calculateResults(firstNum, secondNum, operation)
        print(f"{firstNum} {operation} {secondNum} = {calculation}")

        continueCalculation = input(f"Type 'y' to continue calculating with {calculation}, type 'n' to start a new "
                                    f"calculation, or type anything else to quit: ").lower()
        if continueCalculation == "y":
            firstNum = calculation
            continue
        elif continueCalculation == "n":
            break
        else:
            programRunning = False
            break


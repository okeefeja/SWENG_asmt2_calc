from js import console, document
import math

class Calculator:
    def __init__(self, argument):
        self.argument = argument
        
calculator = Calculator("")
answer = Element("display-text")
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
sign = ["enter", "AC"]

def numbers_clicked(args):
    input = args.target.innerText
    Element("display-text").element.innerHTML += input
    calculator.argument += input
    
def sign_clicked(args):
    if args.target.id == "enter":
       calculate()
    elif args.target.id == "AC":
        clear_all()
    elif args.target.id not in sign:
        operator = args.target.innerText
        if args.target.id == "logs":
            Element("display-text").element.innerHTML += "<span>" + "log(" + "<span>"
        else:
            Element("display-text").element.innerHTML += "<span>" + operator + "</span>"
        if args.target.id == "logs":
            calculator.argument += "log("
        elif args.target.id == "divide":
            calculator.argument += "/"
        elif args.target.id == "multiply":
            calculator.argument += "*"
        elif args.target.id == "minus":
            calculator.argument += "-"
        elif args.target.id == "plus":
            calculator.argument += "+"
        else:
            calculator.argument += operator
            
        
def calculate():
    console.log(calculator.argument)
    result = evaluate(calculator.argument)
    calculator.argument = ""
    Element("display-text").element.innerHTML = ""
    Element("answer").element.innerText = result

        
def clear_all():
    calculator.argument = ""
    Element("display-text").element.innerHTML = ""
    Element("answer").element.innerText = ""

#----------------------------------------------------------------

def evaluate(inputString):
    values = []
    operators = []
    i = 0
    while i < len(inputString):
        if(inputString[i] == 'l'):
            i, log = calculateLog(i, inputString)
            values.append(log)
        elif inputString[i] == '(':
            operators.append(inputString[i])
        elif inputString[i].isdigit():
            numberString = ""
            while (i < len(inputString) and (inputString[i].isdigit() or inputString[i] == '.')):
                numberString += inputString[i]
                i += 1
            values.append(float(numberString))
            i -= 1
        elif inputString[i] == ')':
            while len(operators) != 0 and operators[-1] != '(':
                value2 = values.pop()
                value1 = values.pop()
                operator = operators.pop()
                values.append(applyOp(value1, value2, operator))
            operators.pop()
        else:
            while (len(operators) != 0 and precedence(operators[-1]) >= precedence(inputString[i])):       
                value2 = values.pop()
                value1 = values.pop()
                operator = operators.pop()
                values.append(applyOp(value1, value2, operator))
            operators.append(inputString[i])
        i += 1
    while len(operators) != 0:
        value2 = values.pop()
        value1 = values.pop()
        operator = operators.pop()      
        values.append(applyOp(value1, value2, operator))
    return round(values[-1], 3)

def calculateLog(i, inputString):
    i += 4
    closeLocation = i
    while(inputString[closeLocation] != ')'):
        closeLocation += 1
    expression = inputString[i:closeLocation]
    number = evaluate(expression)
    result = math.log10(number)
    i = closeLocation + 1
    return i, result

def precedence(operator):
    if operator == '+' or operator == '-'   : return 1
    if operator == '*' or operator == '/'   : return 2
    if operator == '^'                      : return 3
    return 0

def applyOp(a, b, operator):
    if operator == '+': return a + b
    if operator == '-': return a - b
    if operator == '*': return a * b
    if operator == '/': return a / b
    if operator == '^': return pow(a, b)


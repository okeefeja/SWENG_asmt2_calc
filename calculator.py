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
            Element("display-text").element.innerHTML += "<span>" + "log("
        elif args.target.id == "exponent":
            Element("display-text").element.innerHTML += "<span>" + "exp("
        else:
            Element("display-text").element.innerHTML += "<span>" + operator + "</span>"
        if args.target.id == "logs":
            calculator.argument += "log("
        elif args.target.id == "exponent":
            calculator.argument += "exp("
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

def evaluate(inputString):
    values = []
    operators = []
    i = 0
    lastWasNumber = False
    lastWasBracket = False
    while i < len(inputString):
        if(inputString[i] == 'l'):
            i, log = calculateLogExp("log", i, inputString)
            values.append(log)
            lastWasNumber = True
            lastWasBracket = False
        elif(inputString[i] == 'e'):
            i, exp = calculateLogExp("exp", i, inputString)
            values.append(exp)
            lastWasNumber = True
            lastWasBracket = False
        elif inputString[i] == '(':
            if lastWasNumber == True:
                operators.append('*')
            operators.append(inputString[i])
            lastWasNumber = False
            lastWasBracket = False
        elif ((inputString[i] == '-' and inputString[i + 1].isdigit()) or inputString[i].isdigit()):
            numberString = ""
            if(inputString[i] == '-'):
                numberString += '-'
                i += 1
            while (i < len(inputString) and (inputString[i].isdigit() or inputString[i] == '.')):
                numberString += inputString[i]
                i += 1
            values.append(float(numberString))
            if(lastWasBracket == True):
                operators.append('*')
            lastWasNumber = True
            lastWasBracket = False
            i -= 1
        elif inputString[i] == ')':
            lastWasNumber = False
            lastWasBracket = True
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

def calculateLogExp(calculation, i, inputString):
    i += 4
    closeLocation = i
    openBrackets = 0
    while(inputString[closeLocation] != ')' or openBrackets != 0):
        if(inputString[closeLocation] == '('):
            openBrackets += 1
        if(inputString[closeLocation] == ')'):
            openBrackets -= 1
        closeLocation += 1
    expression = inputString[i:closeLocation]
    number = evaluate(expression)
    result = 0
    if(calculation == "log"):
        result = math.log10(number)
    else:
        result = math.exp(number)
    i = closeLocation
    return i, result

def precedence(operator):
    if operator == '+' or operator == '-'   : return 1
    if operator == '*' or operator == '/'   : return 2
    if operator == '^'                      : return 3
    return 0

def applyOp(a, b, operator):
    if operator == '+': return float(a) + float(b)
    if operator == '-': return float(a) - float(b)
    if operator == '*': return float(a) * float(b)
    if operator == '/': return float(a) / float(b)
    if operator == '^': return pow(float(a), float(b))


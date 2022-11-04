from js import console, document

class Calculator:
    def __init__(self, argument):
        self.argument = argument
        
calculator = Calculator("")
answer = Element("display-text")
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
sign = ["enter", "AC"]

def numbers_clicked(args):
    Element("answer").element.innerText = ""
    input = args.target.innerText
    Element("display-text").element.innerHTML += input
    calculator.argument += input
    
def sign_clicked(args):
    if args.target.id == "enter":
       calculate()
    elif args.target.id == "AC":
        clear_all()
    elif args.target.id not in sign:
        Element("answer").element.innerText = ""
        operator = args.target.innerText
        Element("display-text").element.innerHTML += "<span>" + operator + "</span>"
        calculator.argument += operator
            
        
def calculate():
    console.log(calculator.argument)
    answer = evaluate(calculator.argument)
    Element("answer").element.innerText = answer

        
def clear_all():
    calculator.argument = ""
    Element("display-text").element.innerHTML = ""
    Element("answer").element.innerText = ""

#----------------------------------------------------------------

def evaluate(argument):
    return addition(argument[0], argument[2])

def addition(first, second):
    return float(first) + float(second)
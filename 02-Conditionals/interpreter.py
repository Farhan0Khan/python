def main():
    expression = input('Enter the Expression: ')
    determineTheOutput(expression)

def determineTheOutput(e):
    x , operator , y = e.split(' ')
    result = calculate(int(x) , operator , int(y))
    print(f"Result = {result}")

def calculate(x , o , y):
    match o:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y


main()

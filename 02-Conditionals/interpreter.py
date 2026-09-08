
def main():
    expression = input('Expression: ')
    result = interpret(expression)
    print(result)

def interpret(v):
    return eval(v)

main()
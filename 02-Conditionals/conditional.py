def main():
    number = int(input('What is x?'))
    if isEven(number):
        print('Even')
    else:
        print('Odd')

def isEven(v):
    return v % 2 == 0
main()
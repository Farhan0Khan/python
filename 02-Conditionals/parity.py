def main():
    x = int(input("What's x ? "))
    if isEven(x):
        print('Even')
    else:
        print("Odd")


def isEven(x):
    return x % 2 == 0

main()

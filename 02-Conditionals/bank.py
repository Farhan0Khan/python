def main():
    greet = input('Greeting: ')
    checkGMessage(greet)

def checkGMessage(g):
    if g == 'hello' or g == 'Hello':
        print('$0')
    elif g.startswith('h'):
        print('$20')
    else:
        print('$100')

if __name__ == '__main__':
    main()
    
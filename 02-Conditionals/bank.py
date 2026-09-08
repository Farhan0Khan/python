def main():
    message = str(input('Greeting: '))
    if isHello(message):
        print('$0')
    else:
        print('$20')



def isHello(m):
    if m == 'Hello' or m == 'hey' or m == 'hello':
        return True
    else:
        return False 

main()
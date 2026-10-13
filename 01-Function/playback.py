def main():
    char = input('Write a sentence: ')
    playTheSpaces(char)

def playTheSpaces(c):
    c = c.replace(' ' , '...')
    print(c)

main()
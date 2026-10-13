def main():
    greet = input("what's your greeting message: ")
    convertGreet(greet)

def convertGreet(g):
    g = g.replace(':)' , '🙂')
    g = g.replace(':(' , '😒')
    print(g)

main()
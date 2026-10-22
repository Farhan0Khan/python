def main():
    age = checkAge(int(input("What's Your age ? ")))

    if age:
        print('You Are eligible to vote')
    else:
        print('You are not eligible to vote')

def checkAge(a):
    return a >= 18

    
main()
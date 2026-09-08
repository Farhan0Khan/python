def main():
    answer = str(input('What is the Great Question of life? '))
    if checkAnswer(answer):
        print('Yes')
    else:
        print('No')

def checkAnswer(a):
    return a == '42' or a == 'forty-two' or a == 'forty two' 
        
main()
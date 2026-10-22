def main():
    ans = input("What's the great question of life , the Universe and Everything ? ")
    determine_ans(ans)

def determine_ans(a):
    if a == '42' or a == 'forty two' or a == 'forty-two':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
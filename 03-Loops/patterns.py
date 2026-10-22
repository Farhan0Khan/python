#1 program to print *

'''def main():
    star(getNumber())

def getNumber():
    while True:
        n = int(input("What's n ? "))
        if n > 0:
            return n

def star(n):
    for i in range(n):
        print('*', end=" " , sep="")

main()'''

#2 program to add from n to m

'''def main():
    cast(getNumber())

def getNumber():
    while True:
        n = int(input("What's n? "))
        m = int(input("What's m? "))
        if n < m:
            return n , m
        else:
            print('m must be greater that n')

def cast(n):
    list(n)
    sum = 0
    i = n[1]
    while i >= n[0]:
        sum += i
        i -= 1

    print(f"Sum = {sum}")

main()

'''

#3 write a program to print 
'''
    ****
    ****
    ****
    ****
'''

'''def main():
    star(getNumber())

def getNumber():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def star(n):
    for i in range(n):
        for j in range(n):
            print("*" , sep="" , end=" ")
        print(end="\n")
main()'''


#4 print
'''
    1
    12
    123
    1234
'''

'''n = int(input("What's n? "))

for i in range(n):
    for j in range(1, i+2):
        print(j, end=" ")
    print(end="\n")'''


#5 print
'''
    1
    22
    333
    4444
'''

'''n = int(input("What's n? "))

for i in range(n):
    for j in range(i+1):
        print(i + 1, end=" ")
    print(end="\n")'''


#6 print
'''
    0
    12
    345
    6798
'''
'''count = 0
for i in range(4):
    for j in range(i+1):
        print(count, end=' ')
        count += 1
    print()
'''

#7 print

'''
            1
        1   2   1
    1   2   3   2   1

'''
'''n = 4

for i in range(n):
    for j in range((n - (i+1))):
        print(' ' , end=" ")
    for k in range(1,i+2):
        print(k, end=" ")
    for l in range(1,i+1):
        print(l , end=" ")

    print()'''


#8 print

'''
            1
        2   1  
    3   2   1  

'''
'''n = 4

for i in range(n):
    for j in range(n - (i+1)):
        print(" " , end=" ")
    for k in range(i+1,0,-1):
        print(k, end=" ")
    print()'''








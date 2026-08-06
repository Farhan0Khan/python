# conditionals

# x = input('Name: ')

# if x == 'farhan' or x == 'Farhan':
#     print('You are Great')
#     # if chaining conditions:
#        # print('statement)
# elif x == 'samosa':
#     print('farhan loves it')
# else:
#     print('Not great')


# loops

# range parameter 
# single -> start
# double -> start stop
# triple -> start, stop , step

for i in range(2, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(10 , -1, -1):
    print(i)

for i in [2, 3,4 , 54]:
    print(i)

x = [2, 3, 4, 5, 6, 7, 78]

for i in range(len(x)):
    print(x[i])

for i, element in enumerate(x):
    print(i , element)

i = 0
while i < 10:
    print('run')
    i += 1

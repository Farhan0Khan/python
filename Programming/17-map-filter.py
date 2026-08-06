x = [1, 2, 3, 4, 5, 6]

mp = map(lambda i: i * 2, x)
print(list(mp))

fil = filter(lambda i: i % 2 == 0,x)
print(list(fil))
# list are mutables

x = [4, True , 'hi']
y = x # reference
# y = x[:] copy

x[0] =1200
print(x)
print(x.append('hello'))
print(x.entend([4,5, 6, 6, 6]))
print(x.pop())
print(x.pop(1))
print(x[0])

print(x)
print(len(x))
print(len(y))
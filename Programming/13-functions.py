def func():
    print('Run successfully')
func()

def arith(x, y, z=None):
    print('proccessing', x, y)
    return x + y, x * y, x % y

result1, result2 , result3 = arith(5, 10)
print(result1)
print(result2)
print(result3)


def fun1(x):
    def fun2():
        print(x)
    return fun2

ans = fun1(3)
ans()

# *args (arguments) or **kwargs (keyword arguments)

x = [12, 12 ,23, 145, 46]
print(x)
print(*x) #unpack


def argkey(*args, **kwargs):
    print(args, kwargs)

argkey(1, 2, 3, 4 , one=1,  two=2)
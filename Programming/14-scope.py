x = 'farhan' # global

def func(name):
    global x
    x = name 

print(x)
func('change')
print(x)
x = [0, 1, 2, 3, 4, 5,6 ,7, 8, 9]
y = ['hello', 'hi', 'bye', 'tata bye bye', 'khatam']
s = "hello"

# sliced = [start:stop:step] fro three parameters
# sliced = [start:stop] fro two parameters

sliced = x[2:] # start from 2 index and end at the last index
sliced = x[:4] # strat at the beginnig and stop at index 4
sliced1 = x[0:10:2] # start at 0 index stop at 10 index and step by 2
sliced3 = x[10:0:-1] # start from 10 index stop at o index and step by -1
sliced4 = x[::-1]  # start at first index stop at last index step by -1

print(sliced)
print(sliced1)
print(sliced3)
print(sliced4)
print(s[::-1])
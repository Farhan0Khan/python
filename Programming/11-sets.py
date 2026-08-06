x = set()
s = {4, 32, 3, 4, 5}
s2 = { 12 , 12, 12 ,1, 2, 3,4}

s.add(7)
s.update([4,8])
s.update([10, 12]),
s.remove(3)
s.pop()
# s.clear() remove all elements


print(x)
print(s)
print(s2)

print(type(x))
print(type(s))
print(type(s2))

print(s.union(s2))
print(s.intersection(s2))
print(s.difference(s2))

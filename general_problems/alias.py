a = 15

b = 15

print(a is b)

a = [15]

b = [15]

print(a is b)

c = b

print(c is b)

b += [1]

print(b, c)
print(b is c)

b = b + [1]
print(b, c)
print(b is c)

print(b[:0])
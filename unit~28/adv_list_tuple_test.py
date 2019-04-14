start, end = map(int, input().split())
a = []

for i in range(start, end+1):
    b = 2**i
    a.append(b)

a.pop(-2)
a.pop(1)

print(a)

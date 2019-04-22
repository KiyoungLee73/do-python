def plus_ten(x):
    return x+10

print(list(map(plus_ten, [1,2,3])))

print(plus_ten(1))

plus_ten2 = lambda x: x + 10

print(plus_ten2(1))

print((lambda x: x + 10)(1))

y = 10
print((lambda x: x + y)(1))

print(list(map(lambda x: x + 10, [1,2,3])))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))
print(list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a)))

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x * y, a, b)))

print('1.jpg'.find('.'))
print('10.jpg'.find('.'))

# Exam
files = input().split()

print(list(map(lambda x: x.zfill(len(x) + 2) if x.find('.') == 1 else x.zfill(len(x) + 1) if x.find('.') == 2 else x, files)))
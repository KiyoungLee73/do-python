def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        #print(total)
        return total
    return mul_add
 
c = calc()
print(c(3), c(2), c(1))
print(c(1), c(2), c(3))



def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count
 
c = counter()
for i in range(10):
    print(c(), end=' ')


def countdown(n):
    i = n+1
    def count():
        nonlocal i
        i -= 1
        return i
    return count

n = int(input())
 
c = countdown(n)
for i in range(n):
    print(c(), end=' ')


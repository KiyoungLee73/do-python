x, y = map(int, input().split())

def calc(var1, var2):
    return var1+var2, var1-var2, var1*var2, var1/var2

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
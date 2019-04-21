# def hello(count):
#     if count == 0:
#         return
    
#     print('Hello, world!', count)
#     count -= 1
#     hello(count)

# hello(5)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(4))


# def is_palindrome(word):
#     #for i in len(word)//2:
#     if word[0] != word[-1]:
#         return False
#     if len(word) < 2:
#         return True
#     s = word[1:-1]
#     print(s)
#     is_palindrome(s)
    

# print(is_palindrome('hello'))
# print(is_palindrome('level'))


def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))


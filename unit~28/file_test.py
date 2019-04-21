file = open('hello.txt', 'w')
file.write('Hello, world !')
file.close()

file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()

with open('hello.txt', 'r') as hello_file:
    s = hello_file.read()
    print(s)

with open('hello.txt', 'w') as hello_file:
    for i in range(3):
        hello_file.write('Hello, world ! {0}\n'.format(i))

lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

with open('hello.txt', 'w') as hello_file:
    hello_file.writelines(lines)

with open('hello.txt', 'r') as hello_file:
    lines2 = hello_file.readlines()
    print(lines2)

with open('hello.txt', 'r') as hello_file:
    for line in hello_file:
        print(line.strip('\n'))







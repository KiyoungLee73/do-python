a = list(map(int, input().split(';')))

a.sort(reverse=True)

for i in a:
    print('%9s' % format(i, ','))

import copy

col, row = map(int, input().split())

info = []
for i in range(row):
    info.append(list(input()))

infocopy = copy.deepcopy(info)

for i in range(len(infocopy)):
    for j in range(len(infocopy[i])):
        near_count = 0
        if i-1 >= 0 and i - 1 < col and j-1 >= 0 and j-1 < row:
            if infocopy[i-1][j-1] == '*':
                near_count = near_count + 1
        if i-1 >= 0 and i - 1 < col and j >= 0 and j < row:
            if infocopy[i-1][j] == '*':
                near_count = near_count + 1
        if i-1 >= 0 and i - 1 < col and j+1 >= 0 and j+1 < row:
            if infocopy[i-1][j+1] == '*':
                near_count = near_count + 1
        if i >= 0 and i < col and j-1 >= 0 and j-1 < row:
            if infocopy[i][j-1] == '*':
                near_count = near_count + 1
        if i >= 0 and i < col and j+1 >= 0 and j+1 < row:
            if infocopy[i][j+1] == '*':
                near_count = near_count + 1
        if i+1 >= 0 and i + 1 < col and j-1 >= 0 and j-1 < row:
            if infocopy[i+1][j-1] == '*':
                near_count = near_count + 1
        if i+1 >= 0 and i + 1 < col and j >= 0 and j < row:
            if infocopy[i+1][j] == '*':
                near_count = near_count + 1
        if i+1 >= 0 and i + 1 < col and j+1 >= 0 and j+1 < row:
            if infocopy[i+1][j+1] == '*':
                near_count = near_count + 1
        if infocopy[i][j] == '*':
            print('*', end='')
        else:
            print(near_count, end='')
        near_count = 0
    print()

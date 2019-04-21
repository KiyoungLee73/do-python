with open('words.txt', 'r') as file:
    count = 0
    for word in file:
        s = word.strip('\n')
        if len(s) <= 10:
            count = count + 1
    print(count)


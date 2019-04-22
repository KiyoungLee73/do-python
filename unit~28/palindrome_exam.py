with open('words.txt', 'r') as file:
    for line in file:
        s = line.replace('\n', '')
        if s == ''.join(reversed(s)):
            print(s)
        
with open('words.txt', 'r') as file:
    one_line = file.readlines()
    lines = one_line[0].split()
    for line in lines:
        s = line.replace('.', '')
        s = s.replace(',', '')
        
        if s.find('c') >= 0:
            print(s)
        
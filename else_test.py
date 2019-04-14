x1, x2, x3, x4 = map(int, input().split())

if (x1 >= 0 and x1 <= 100 and x2 >= 0 and x2 <= 100 and x3 >= 0 and x3 <= 100 and x4 >= 0 and x4 <= 100):
    avg_record = (x1+x2+x3+x4)/4
    if (avg_record > 80):
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')

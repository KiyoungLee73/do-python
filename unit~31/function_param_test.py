# def print_numbers(a, b, c):
#     print(a)
#     print(b)
#     print(c)

# x = [10, 20, 30]
# print_numbers(*x)

# def print_number(*args):
#     for arg in args:
#         print(arg)

# print_number(10)
# print_number(10, 20, 30, 40)

# def personal_info(name, age, address):
#     print('이름: ', name)
#     print('나이: ', age)
#     print('주소: ', address)

# personal_info('홍길동', 30, '서울')
# personal_info(name='홍길동', age=30, address='서울')
# personal_info(age=30, name='홍길동', address='서울')

# x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
# personal_info(*x)
# personal_info(**x)

# def personal_infos(**kwargs):
#     for kw, arg in kwargs.items():
#         print(kw, ': ', arg)

# personal_infos(**x)


# korean, english, mathematics, science = 100, 86, 81, 91

# def get_max_score(*args):
#     return max(args)

# max_score = get_max_score(korean, english, mathematics, science)
# print('높은 점수:', max_score)
 
# max_score = get_max_score(english, science)
# print('높은 점수:', max_score)


korean, english, mathematics, science = map(int, input().split())

def get_average(**kwargs):
    count = 0
    total = 0
    for kw, arg in kwargs.items():
        count = count + 1
        total = total + arg
    
    return total/count 

def get_min_max_score(*args):
    return min(args), max(args)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))







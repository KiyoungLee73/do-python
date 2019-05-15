# Dup

input_data = 'ABC, QWER, BCD, QWER, BDC, BDC, QWER, ABD, XYZ, BCD, XYZ, IU'

# Answer #1
data = map(str, input_data.split(', '))

dic_data = {}

for a in data:
    if a in dic_data:
        dic_data[a] = dic_data[a] + 1
    else:
        dic_data[a] = 1

for b in dic_data.keys():
    if dic_data[b] > 1:
        print('{}={}'.format(b,dic_data[b]))

# Answer #2
data2 = map(str, input_data.split(', '))

result_data = list()
result_str = ''

for c in data2:
    if result_data.count(c) == 0:
        result_data.append(c)
    else:
        del(result_data[result_data.index(c)])
        result_data.append(c)

print(result_data)

result_str = ''
loop_cnt = 0
for d in result_data:
    if loop_cnt != 0:
        result_str = result_str + ', '    
    result_str = result_str + d 
    loop_cnt += 1

print(result_str)
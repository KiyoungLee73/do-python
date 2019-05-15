# Music

data = [{'C':'1 1 3 4 6 7 1'}
        , {'D':'3 4 6 1 2'}
        , {'G':'6 6'}
        , {'F':'2 5 3 1 5'}
        , {'A':'1 2 1 2 3 1 2 1 2 3'}
        , {'E':'5 5 5 5 5'}
        ]

# Answer #1
max_cnt = 0
max_val = ''
temp_list = list()
temp_cnt = 0

for a in data:
    for b in a:
        #print(b)
        #print(a[b])
        temp_list = map(int, a[b].split())
        for c in temp_list:
            temp_cnt += c
        if temp_cnt > max_cnt:
            max_cnt = temp_cnt
            max_val = b
        temp_cnt = 0
print(max_val)
#print(max_cnt)
        
# Answer #2
import copy

temp_str = ''
temp_str_list = list()
temp_list2 = list()
temp_list3 = list()
temp_idx = 0
result_str = ''

for a in data:
    for b in a:
        temp_list = map(int, a[b].split())
        #print(a[b])
        #print(b)
        temp_str = temp_str.zfill(max_cnt)
        
        for d in temp_str:
            temp_str_list.append(d)

        for c in temp_list:
            temp_idx += c
            temp_str_list[temp_idx-1] = b
            #print(temp_idx-1)
            
        temp_idx = 0
        temp_list2.append(temp_str_list)

        #print(temp_str_list)
        del(temp_str_list)
        temp_str_list = list()

temp_list3 = copy.deepcopy(temp_list2)

temp_list3[0] = temp_list2[0]
temp_list3[1] = temp_list2[1]
temp_list3[2] = temp_list2[5]
temp_list3[3] = temp_list2[3]
temp_list3[4] = temp_list2[2]
temp_list3[5] = temp_list2[4]

for i in range(25):
    for j in range(6):
        #print(temp_list3[j][i], end='')
        result_str += temp_list3[j][i]
    #print(', ', end='')
    result_str += ', '

print(result_str.replace('000000, ', '').replace('0', '').strip(', '))

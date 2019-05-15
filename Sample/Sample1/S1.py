#Compress

str1 = 'AAAQABBBCCCCCDAAACCDDDDB'
#str1 = 'APPLE'

# Answer
prev_str = ''
dup_cnt = 1
loop_cnt = 0
result_str = ''

for a in str1:
    if prev_str != a:
        if loop_cnt != 0:
            result_str += str(dup_cnt)
        result_str += a
        dup_cnt = 1
    else:
        dup_cnt += 1
    prev_str = a
    loop_cnt += 1
result_str += str(dup_cnt)

if len(result_str) >= len(str1):
    print(str1)
else:
    print(result_str)



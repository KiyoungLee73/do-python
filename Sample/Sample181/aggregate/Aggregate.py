# 부분 배열의 개수를 구하는 기능
#
# @param		arraySize			배열 크기
# @return							부분 배열의 개수
def getNumberOfSubArrays(arraySize):
    numberOfSubArrays = 0
    ########################여기부터 구현 (1) ---------------->
    ls_sub_array = list()
    start_pos = ''
    end_pos = ''
    sub_array_size = 0
    count = 0

    for k in range(1, arraySize + 1, 1):
        sub_array_size = k
        #print('sub_array_size : ' + str(sub_array_size))
        for start_i in range(1, arraySize + 2 - sub_array_size, 1):
            for start_j in range(1, arraySize + 2 - sub_array_size, 1):
                #print('start i, j : ' + str(start_i) + ', ' + str(start_j))
                end_i = start_i + sub_array_size - 1
                end_j = start_j + sub_array_size - 1
                
                start_pos = str(start_i) + ',' + str(start_j)
                end_pos = str(end_i) + ',' + str(end_j)
                ls_sub_array.append([start_pos, end_pos])

                count += 1
    #print(count)
    numberOfSubArrays = count

    ############################# <-------------- 여기까지 구현 (1)
    return numberOfSubArrays

# 최대값을 찾는 기능
#
# @param		inputData			입력데이터(NxN배열)
# @return							최대값
def getMaximumValue(inputData):
    maximumValue = 0
    ########################여기부터 구현 (2) ---------------->

    arraySize = len(inputData)
    ls_sub_array = list()
    start_pos = ''
    end_pos = ''
    sub_array_size = 0
    count = 0

    for k in range(1, arraySize + 1, 1):
        sub_array_size = k
        #print('sub_array_size : ' + str(sub_array_size))
        for start_i in range(1, arraySize + 2 - sub_array_size, 1):
            for start_j in range(1, arraySize + 2 - sub_array_size, 1):
                #print('start i, j : ' + str(start_i) + ', ' + str(start_j))
                end_i = start_i + sub_array_size - 1
                end_j = start_j + sub_array_size - 1
                
                start_pos = str(start_i) + ',' + str(start_j)
                end_pos = str(end_i) + ',' + str(end_j)
                ls_sub_array.append([start_pos, end_pos])

                count += 1
    
    start_idx = list()
    end_idx = list()
    max_val = 0
    for start_end in ls_sub_array:
        start_idx_str, end_idx_str = start_end[0], start_end[1]
        start_idx = start_idx_str.split(',')
        end_idx = end_idx_str.split(',')
        #print(start_idx)
        #print(end_idx)

        # Max 계산
        temp_sum = 0
        for pos_i in range(int(start_idx[0]), int(end_idx[0])+1, 1):
            for pos_j in range(int(start_idx[1]), int(end_idx[1])+1, 1):
                temp_sum = temp_sum + inputData[pos_i-1][pos_j-1]

        if temp_sum > max_val:
            max_val = temp_sum
        
        temp_sum = 0

        #print(max_val)
        maximumValue = max_val
    ############################# <-------------- 여기까지 구현 (2)
    return maximumValue

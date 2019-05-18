# 단순비교 방식의 유사도 측정 기능
#
# @param		inputData			입력데이터(유전자 문자열)
# @return							유사도
def measureSimpleComparison(inputData):
    similarity = 0
    ######################여기부터 구현 (1) ---------------->
    #문자열 통합 길이 구하기
    str1, str2 = map(str, inputData.split(','))
    str1_len = len(str1)
    str2_len = len(str2)
    total_len = str1_len + (str2_len - 1)*2
    loop_len = str1_len + str2_len - 1


    fixedStr1 = str1.center(total_len, '0')
    fixedStr2 = str2.ljust(total_len).replace(' ', '0')

    compareStr1 = list(fixedStr1)
    compareStr2 = list('0' for i in range(total_len))

    checkList = list()

    import copy
    temp_ls = list()
    for i in range(loop_len):
        count = 0
        pos = 0
        for j in fixedStr2:
            pos = (count+i)%total_len
            compareStr2[pos] = j
            count += 1
        temp_ls = copy.deepcopy(compareStr2)
        checkList.append(temp_ls)

    #유사도 판단
    maxResemble = 0
    for i in checkList:
        tempResemble = 0
        for j in range(len(i)):
            if i[j] == compareStr1[j] and  compareStr1[j] != '0' and i[j] != '0':
                tempResemble += 1
        
        if tempResemble > maxResemble:
            maxResemble = tempResemble

    similarity = maxResemble
    ############################# <-------------- 여기까지 구현 (1)
    return similarity

# 행렬비교 방식의 유사도 측정 기능
#
# @param		inputData				입력데이터(유전자 문자열)
# @param		similarityMatrix		입력데이터(유사도 측정 행렬)
# @return								가장 큰 유사도
def measureSortComparison(inputData, similarityMatrix):
    maxSimilarity = 0
    ######################여기부터 구현 (2) ---------------->
    #문자열 통합 길이 구하기
    str1, str2 = map(str, inputData.split(','))
    str1_len = len(str1)
    str2_len = len(str2)
    total_len = str1_len + (str2_len - 1)*2
    loop_len = str1_len + str2_len - 1

    fixedStr1 = str1.center(total_len, '0')
    fixedStr2 = str2.ljust(total_len).replace(' ', '0')

    compareStr1 = list(fixedStr1)
    compareStr2 = list('0' for i in range(total_len))

    checkList = list()

    import copy
    temp_ls = list()
    for i in range(loop_len):
        count = 0
        pos = 0
        for j in fixedStr2:
            pos = (count+i)%total_len
            compareStr2[pos] = j
            count += 1
        temp_ls = copy.deepcopy(compareStr2)
        checkList.append(temp_ls)

    #유사도 판단
    maxResemble = 0

    compare = {'A':0, 'C':1, 'G':2, 'T':3, '0':4}

    for i in checkList:
        tempResemble = 0
        for j in range(len(i)):
            i[j] == compareStr1[j]  # A = C
            tempResemble += similarityMatrix[compare.get(i[j])][compare.get(compareStr1[j])]
        if tempResemble > maxResemble:
            maxResemble = tempResemble    
    
    maxSimilarity = maxResemble
    ############################# <-------------- 여기까지 구현 (2)
    return maxSimilarity

# 입력문자열을 배열로 만드는 기능 (솔루션용 기능, 제공파일에 없음)
#
# @param		firstStr			첫번째 문자열
# @param		secondStr			두번째 문자열
# @return							배열
def getInputArr(firstStr, secondStr):
    rowSize = len(firstStr) + len(secondStr) - 1
    inputArr = [[" " for row in range(rowSize)] for col in range(2)]
    index = 0
    for c in firstStr:
        inputArr[0][index] = c
        index += 1

    index = rowSize - len(secondStr)
    for c in secondStr:
        inputArr[1][index] = c
        index += 1
    return inputArr

# 인덱스를 가져오는 기능(솔루션용 기능, 제공파일에 없음)
#
# @param		str			문자열
# @return					인덱스
def getIndexNum(str):
    num = 0
    if str == "A":
        num = 0
    elif str == "C":
        num = 1
    elif str == "G":
        num = 2
    elif str == "T":
        num = 3
    elif str == " ":
        num = 4
    return num
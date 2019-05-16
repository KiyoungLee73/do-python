# 단순비교 방식의 유사도 측정 기능
#
# @param		inputData			입력데이터(유전자 문자열)
# @return							유사도
def measureSimpleComparison(inputData):
    similarity = 0
    ######################여기부터 구현 (1) ---------------->
    inputDataArr = inputData.split(",")
    firstStr = inputDataArr[1]
    secondStr = inputDataArr[0]
    inputArr = getInputArr(firstStr, secondStr)
    rowSize = len(firstStr) + len(secondStr) - 1

    iniSimilarity = 0
    for index in range(rowSize):
        if inputArr[0][index] != " " and inputArr[1][index] != " ":
            if inputArr[0][index] == inputArr[1][index]:
                iniSimilarity += 1
    if similarity < iniSimilarity:
        similarity = iniSimilarity
    firstStrLengthEnd = len(firstStr)
    for i in range(rowSize - len(firstStr)):
        for j in range(firstStrLengthEnd-1, -1, -1):
            inputArr[0][j+1] =inputArr[0][j]
            if j == 0:
                inputArr[0][j] = " "
        firstStrLengthEnd += 1

        tmpSimilarity = 0
        for index in range(rowSize):
            if inputArr[0][index] != " " and inputArr[1][index] != " ":
                if inputArr[0][index] == inputArr[1][index]:
                    tmpSimilarity += 1
        if similarity < tmpSimilarity:
            similarity = tmpSimilarity

    secondStrLengthStart = rowSize - len(secondStr)
    for i in range(rowSize - len(secondStr)):
        for j in range(secondStrLengthStart, rowSize):
            inputArr[1][j-1] = inputArr[1][j]
            if j == rowSize-1:
                inputArr[1][j] = " "
        secondStrLengthStart -= 1
        tmpSimilarity = 0
        for index in range(rowSize):
            if inputArr[0][index] != " " and inputArr[1][index] != " ":
                if inputArr[0][index] == inputArr[1][index]:
                    tmpSimilarity += 1
        if similarity < tmpSimilarity:
            similarity = tmpSimilarity
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
    tmpMax = float('-inf')
    inputDataArr = inputData.split(",")
    firstStr = inputDataArr[1]
    secondStr = inputDataArr[0]
    inputArr = getInputArr(firstStr, secondStr)
    rowSize = len(firstStr) + len(secondStr) - 1

    iniSimilarity = 0
    for index in range(rowSize):
        rowIndex = getIndexNum(inputArr[0][index])
        colIndex = getIndexNum(inputArr[1][index])
        iniSimilarity += similarityMatrix[rowIndex][colIndex]


    if tmpMax < iniSimilarity:
        tmpMax = iniSimilarity

    firstStrLengthEnd = len(firstStr)
    for i in range(rowSize - len(firstStr)):
        for j in range(firstStrLengthEnd-1 , -1, -1):
            inputArr[0][j+1] =inputArr[0][j]
            if j == 0:
                inputArr[0][j] = " "
        firstStrLengthEnd += 1

        tmpSimilarity = 0
        for index in range(rowSize):
            rowIndex = getIndexNum(inputArr[0][index])
            colIndex = getIndexNum(inputArr[1][index])
            tmpSimilarity += similarityMatrix[rowIndex][colIndex]
        if tmpMax < tmpSimilarity:
            tmpMax = tmpSimilarity

    secondStrLengthStart = rowSize - len(secondStr)
    for i in range(rowSize - len(secondStr)):
        for j in range(secondStrLengthStart, rowSize):
            inputArr[1][j-1] = inputArr[1][j]
            if j == rowSize-1:
                inputArr[1][j] = " "
        secondStrLengthStart -= 1
        tmpSimilarity = 0
        for index in range(rowSize):
            rowIndex = getIndexNum(inputArr[0][index])
            colIndex = getIndexNum(inputArr[1][index])
            tmpSimilarity += similarityMatrix[rowIndex][colIndex]

        if tmpMax < tmpSimilarity:
            tmpMax = tmpSimilarity
    maxSimilarity = tmpMax
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
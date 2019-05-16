# 단순비교 방식의 유사도 측정 기능
#
# @param		inputData			입력데이터(유전자 문자열)
# @return							유사도
def measureSimpleComparison(inputData):
    similarity = 0
    ######################여기부터 구현 (1) ---------------->
    
    


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
# 배열을 정렬하는 기능
#
# @param		inputData		입력데이터(이차원배열)
# @return						정렬된 배열
def getSortedArray(inputData) :
    sortedArray = []
    ########################여기부터 구현 (1) ---------------->
    size = len(inputData)

    import copy
    tempSortedArray = copy.deepcopy(inputData)
    switchArray = copy.deepcopy(inputData)

    # 나머지 구하기
    for i in range(size):
        for j in range(size):
            tempSortedArray[i][j] = inputData[i][j]%10

    # 오름차순 정렬
    for i in range(size):
        tempSortedArray[i].sort()

    # 가로세로 스위치
    for i in range(size):
        for j in range(size):
            switchArray[j][i] = tempSortedArray[i][j]

    # 오름차순 정렬
    for i in range(size):
        switchArray[i].sort()

    # 가로세로 스위치 (원복)
    for i in range(size):
        for j in range(size):
            tempSortedArray[j][i] = switchArray[i][j]

    sortedArray = tempSortedArray
    ############################# <-------------- 여기까지 구현 (1)
    return sortedArray

# 배열합을 계산하는 기능
#
# @param		sortedArray		정렬된 배열
# @return						배열합
def getArrSum(sortedArray) :
    arrSum = 0
    ########################여기부터 구현 (2) ---------------->
    import copy
    tempSortedArray = copy.deepcopy(sortedArray)

    size = len(tempSortedArray)

    # 체크할 각 셀위치 돌기
    for i in range(size):
        for j in range(size):
            chkStr = sortedArray[i][j]
            changedFlag = 'N'
            # 위
            if i-1 < 0:
                pass
            else:
                if chkStr == sortedArray[i-1][j]:
                    tempSortedArray[i-1][j] = 0
                    changedFlag = 'Y'
            # 아래
            if i+1 >= size:
                pass
            else:
                if chkStr == sortedArray[i+1][j]:
                    tempSortedArray[i+1][j] = 0
                    changedFlag = 'Y'
            # 좌
            if j-1 < 0:
                pass
            else:
                if chkStr == sortedArray[i][j-1]:
                    tempSortedArray[i][j-1] = 0
                    changedFlag = 'Y'
            # 우
            if j+1 >= size:
                pass
            else:
                if chkStr == sortedArray[i][j+1]:
                    tempSortedArray[i][j+1] = 0
                    changedFlag = 'Y'
            #원값 바꾸기
            if changedFlag == 'Y':
                tempSortedArray[i][j] = 0
    sumVal = 0
    for i in range(size):
        for j in range(size):
            sumVal += tempSortedArray[i][j]
    
    arrSum = sumVal
    ############################# <-------------- 여기까지 구현 (2)
    return arrSum
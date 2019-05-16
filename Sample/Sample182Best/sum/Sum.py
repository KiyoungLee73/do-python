# 배열을 정렬하는 기능
#
# @param		inputData		입력데이터(이차원배열)
# @return						정렬된 배열
def getSortedArray(inputData) :
    sortedArray = []
    ########################여기부터 구현 (1) ---------------->
    arraySize = len(inputData)
    sortedArray = [[0 for col in range(arraySize)] for row in range(arraySize)]
    for i in range(arraySize):
        for j in range(arraySize):
            sortedArray[i][j] = inputData[i][j]%10
    for i in range(arraySize):
        for j in range(arraySize):
            for k in range(j+1, arraySize):
                if sortedArray[i][j] > sortedArray[i][k]:
                    tmp = sortedArray[i][j]
                    sortedArray[i][j] = sortedArray[i][k]
                    sortedArray[i][k] = tmp
    for i in range(arraySize):
        for j in range(arraySize):
            for k in range(j+1, arraySize):
                if sortedArray[j][i] > sortedArray[k][i]:
                    tmp = sortedArray[j][i]
                    sortedArray[j][i] = sortedArray[k][i]
                    sortedArray[k][i] = tmp
    ############################# <-------------- 여기까지 구현 (1)
    return sortedArray

# 배열합을 계산하는 기능
#
# @param		sortedArray		정렬된 배열
# @return						배열합
def getArrSum(sortedArray) :
    arrSum = 0
    ########################여기부터 구현 (2) ---------------->
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    arraySize = len(sortedArray)
    for i in range(arraySize):
        for j in range(arraySize):
            if sortedArray[i][j] != 0:
                flag = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if nx < arraySize and nx >= 0 and ny < arraySize and ny >= 0:
                        if sortedArray[i][j] == sortedArray[nx][ny]:
                            flag = 1
                            break
                if flag == 0:
                	arrSum += sortedArray[i][j]
    ############################# <-------------- 여기까지 구현 (2)
    return arrSum

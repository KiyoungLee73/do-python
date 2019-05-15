# 부분 배열의 개수를 구하는 기능
#
# @param		arraySize			배열 크기
# @return							부분 배열의 개수
def getNumberOfSubArrays(arraySize):
    numberOfSubArrays = 0
    ########################여기부터 구현 (1) ---------------->
    for i in range(arraySize):
        numberOfSubArrays += ((i+1)*(i+1))
    ############################# <-------------- 여기까지 구현 (1)
    return numberOfSubArrays

# 최대값을 찾는 기능
#
# @param		inputData			입력데이터(NxN배열)
# @return							최대값
def getMaximumValue(inputData):
    maximumValue = 0
    ########################여기부터 구현 (2) ---------------->
    maximumValue = float('-inf')
    arraySize = len(inputData)
    for i in range(arraySize):
        for j in range(arraySize):
            loop = arraySize-j if arraySize-i > arraySize-j else arraySize-i
            for index in range(1, loop+1):
                tmpMaxValue = 0
                tmpI = i
                for tmpIndex in range(tmpI, tmpI+index):
                    for tmpIndex2 in range(j, j+index):
                        tmpMaxValue += inputData[tmpIndex][tmpIndex2]
                if tmpMaxValue > maximumValue:
                    maximumValue = tmpMaxValue
    ############################# <-------------- 여기까지 구현 (2)
    return maximumValue

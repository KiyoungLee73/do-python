#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Aggregate.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from Aggregate import *

def main():
    global backup, netWork
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()
    printInput(inputData)

    # 부분 배열의 개수를 구하는 기능
    numberOfSubArrays = getNumberOfSubArrays(len(inputData))
    printNumberOfSubArrays(len(inputData), numberOfSubArrays)

    # 최대값을 찾는 기능
    maximumValue = getMaximumValue(inputData)
    printMaximumValue(len(inputData), maximumValue)

def loadData():
    global backup, netWork

    ######################
    # 제공 데이터 세트 1
    ######################
    # inputData = [
    #         [-1, 0, 7, 9],
    #         [-6, 2, -3, 5],
    #         [3, -6, 0, -5],
    #         [7, 8, -7, 2]
    # ]

    ######################
    # 제공 데이터 세트 2
    ######################

    inputData = [
        [1, -3, 0, 2, 5],
        [-3, 0, 8, -3, 7],
        [9, -1, -2, 6, 0],
        [-2, -5, 9, 7, 6],
        [3, 2, 4, 7, -5]
    ]

    return inputData

def printInput(inputData):
    printLineInitial()
    for i in range(len(inputData)):
        for j in range(len(inputData)):
            print(inputData[i][j], end=" ")
        print()
    printLine()

def printNumberOfSubArrays(size, numberOfSubArrays) :
    print("[{}x{}배열의 부분 배열 개수]: ".format(size, size),end="")
    if(numberOfSubArrays == 0):
        print("결과값이 없습니다.")
    else:
        print("{}개".format(numberOfSubArrays))
    printLine()


def printMaximumValue(size, maximumValue) :
    print("[{}x{}배열의 부분 배열내의 최대합]: ".format(size, size), end="")
    if(maximumValue == 0):
        print("결과값이 없습니다.")
    else:
        print(maximumValue)
    printLine()

def printLineInitial():
    print("[초기 입력 데이터]")

def printLine():
    print("--------------------------------------------------------------------------")


## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()
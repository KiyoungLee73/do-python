#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Sum.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from sum.Sum import *

def main():
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()
    printInput(inputData)

    # 배열을 정렬하는 기능
    sortedArray = getSortedArray(inputData)
    printSortedArray(sortedArray)

    # 배열합을 계산하는 기능
    arrSum = getArrSum(sortedArray)
    printArrSum(arrSum)


def loadData():
    ######################
    # 제공 데이터 세트 1
    ######################
    inputData = [
        [77, 78, 12, 30],
        [33, 78, 9, 7],
        [5, 71, 84, 25],
        [9, 37, 0, 27]
    ]



    ######################
    # 제공 데이터 세트 2
    ######################

    # inputData = [
    #     [11, 32, 57, 65, 34],
    #     [53, 16, 3, 93, 22],
    #     [35, 22, 73, 64, 14],
    #     [12, 24, 34, 45, 91],
    #     [9, 51, 35, 28, 75]
    # ]

    return inputData

def printInput(inputData):
    printLineInitial()
    arrSize = len(inputData)
    for i in range(arrSize):
        for j in range(arrSize):
            print(inputData[i][j], end= " ")
        print()
    printLine()


def printSortedArray(sortedArray) :
    print("[정렬된 배열]")
    if(len(sortedArray) == 0):
        print("결과값이 없습니다.")
    else:
        arrSize = len(sortedArray)
        for i in range(arrSize):
            for j in range(arrSize):
                print(sortedArray[i][j], end=" ")
            print()
    printLine()

def printArrSum(arrSum) :
    print("[배열합]: ", end="")
    if (arrSum == 0):
        print("결과값이 없습니다.")
    else:
        print(arrSum)
    printLine()

def printLineInitial():
    print("[초기 입력 데이터]")

def printLine():
    print("--------------------------------------------------------------------------")


## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()
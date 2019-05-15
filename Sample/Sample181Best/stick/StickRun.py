#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Stick.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from stick.Stick import *

def main():

    global numberOfLayers
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()

    # N개의 삼각형을 만들기 위한 막대 개수를 구하는 기능
    numberOfStickForTriangle = getNumberOfStickForTriangle(inputData)
    printNumberOfStickForTriangle(inputData, numberOfStickForTriangle)

    # N층의 피라미드를 만들기 위한 막대 개수를 구하는 기능
    numberOfStickForPyramid = getNumberOfStickForPyramid(numberOfLayers)
    printNumberOfStickForPyramid(numberOfLayers, numberOfStickForPyramid)

def loadData():
    global numberOfLayers

    ######################
    # 제공 데이터 세트 1
    ######################

    inputData = 6
    numberOfLayers = 4


    ######################
    # 제공 데이터 세트 2
    ######################

    # inputData = 8
    # numberOfLayers = 7

    return inputData


def printNumberOfStickForTriangle(inputData, numberOfStickForTriangle) :
    print("[{}개의 삼각형을 만들기 위한 막대 개수]: ".format(inputData), end="")
    if(numberOfStickForTriangle == 0):
        print("결과값이 없습니다.")
    else:
        print(numberOfStickForTriangle)
    printLine()


def printNumberOfStickForPyramid(numberOfLayers, numberOfStickForPyramid) :
    print("[{}층의 피라미드를 만들기 위한 막대 개수]: ".format(numberOfLayers), end="")
    if(numberOfStickForPyramid == 0):
        print("결과값이 없습니다.")
    else:
        print(numberOfStickForPyramid)
    printLine()

def printLine():
    print("--------------------------------------------------------------------------")


## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()
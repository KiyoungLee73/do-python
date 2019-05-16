#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Operation.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from Operation import *

def main():
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()
    printInput(inputData)

    # 문자열 분리 기능
    strList = getStrList(inputData)
    printStrList(strList)

    # 새로운 문자열을 생성하는 기능
    newStr = getNewStr(strList)
    printNewStr(newStr)

def loadData():
    ######################
    # 제공 데이터 세트 1
    ######################
    # inputData = "A37D2CB5E8F"

    ######################
    # 제공 데이터 세트 2
    ######################

    inputData = "F7T123GCZ5Q"

    return inputData

def printInput(inputData):
    printLineInitial()
    print(inputData)
    printLine()

def printStrList(strList) :
    print("[문자로 구성된 문자열]: ", end="")
    if len(strList) == 0:
        print("결과값이 없습니다.")
    else:
        print(strList[0])
    print("[숫자로 구성된 문자열]: ", end="")
    if len(strList) == 0:
        print("결과값이 없습니다.")
    else:
        print(strList[1])
    printLine()

def printNewStr(newStr) :
    print("[결과로 생성된 문자열]: ", end="")
    if newStr == "":
        print("결과값이 없습니다.")
    else:
        print(newStr)
    printLine()

def printLineInitial():
    print("[초기 입력 데이터]")

def printLine():
    print("--------------------------------------------------------------------------")


## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()
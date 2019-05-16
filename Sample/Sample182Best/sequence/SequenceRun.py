#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Sequence.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from sequence.Sequence import *

def main():
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()

    # 연속수 목록 검색 기능
    sequenceList = getSequenceList(inputData)
    printsSquenceList(inputData, sequenceList)

    # 가장 큰 수 생성 기능
    maxNum = getMaxNum(sequenceList)
    printMaxNum(sequenceList, maxNum)

def loadData():
    ######################
    # 제공 데이터 세트 1
    ######################
    inputData = [
        "2234", "123", "5678", "456", "8978", "3321", "12", "345", "689"
    ]

    ######################
    # 제공 데이터 세트 2
    ######################

    # inputData = [
    #     "3425", "689", "456", "2345", "1254", "7754", "3255", "345"
    # ]

    return inputData


def printsSquenceList(inputData, sequenceList) :
    print("[연속수 목록]")
    print("입력: ", end="")
    for str in inputData:
        print(str, end=" ")
    print()
    print("출력: ", end="")
    if(len(sequenceList) == 0):
        print("결과값이 없습니다.")
    else:
        for str in sequenceList:
            print(str, end=" ")
        print()
    printLine()

def printMaxNum(sequenceList, maxNum) :
    print("[가장 큰 수]")
    print("입력: ", end="")
    if (len(sequenceList) == 0):
        print("입력값이 없습니다.")
    else:
        for str in sequenceList:
            print(str, end=" ")
        print()
    print("출력: ", end="")
    if (maxNum == 0):
        print("결과값이 없습니다.")
    else:
        print(maxNum)
    printLine()

def printLine():
    print("--------------------------------------------------------------------------")


## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()
#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Recovery.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from recovery.Recovery import *

def main():

    global backup, netWork
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()

    # 데이터 1차 복원 기능
    firstRecovery = getFirstRecovery(inputData, backup)
    printFirstRecovery(inputData, firstRecovery)

    # 데이터 2차 복원 기능
    secondRecovery = getSecondRecovery(firstRecovery, netWork)
    printSecondRecovery(firstRecovery, secondRecovery)

def loadData():
    global backup, netWork

    ######################
    # 제공 데이터 세트 1
    ######################
    inputData = "we1re3hewo34ddre67com21rue"
    backup = "1eare4hewor5dd8eamcome3rue"
    netWork =[
        "wear",
        "ethe",
        "worl",
        "ddre",
        "amco",
        "metr",
        "ue  "
    ]


    ######################
    # 제공 데이터 세트 2
    ######################

    # inputData = "ote12lkja23dhbgfl1ejkhf3uhe"
    # backup = "otek3lkjaopdhbgfl1ejkhf1uhe"
    # netWork = [
    #     "otek",
    #     "plkj",
    #     "aopd",
    #     "hbgf",
    #     "lkej",
    #     "khft",
    #     "uhe "
    # ]

    return inputData


def printFirstRecovery(inputData, firstRecovery) :
    print("[1차 복원된 데이터]")
    print("입력: {}".format(inputData))
    print("출력: ", end="")
    if(firstRecovery == ""):
        print("결과값이 없습니다.")
    else:
        print(firstRecovery)
    printLine()


def printSecondRecovery(firstRecovery, secondRecovery) :
    print("[2차 복원된 데이터]")
    print("입력: ", end="")
    if(firstRecovery == ""):
        print("결과값이 없습니다.")
    else:
        print(firstRecovery)
    print("출력: ", end="")
    if (secondRecovery == ""):
        print("결과값이 없습니다.")
    else:
        print(secondRecovery)
    printLine()

def printLine():
    print("--------------------------------------------------------------------------")


## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()
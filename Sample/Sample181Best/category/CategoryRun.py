#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Category.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from category.Category import *

def main():
    global categories, categoryStr
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()
    printInput(inputData)

    # 상위 카테고리를 검색하는 기능
    topCategory = getTopCategory(inputData, categories)
    printTopCategory(topCategory)

    # 하위 카테고리의 개수를 계산하는 기능
    numberOfSubcategories = getNumberOfSubcategories(inputData, categoryStr)
    printNumberOfSubcategories(numberOfSubcategories)


def loadData():
    global categories, categoryStr

    ######################
    # 제공 데이터 세트 1
    ######################

    inputData = [
        ["M", "B"],
        ["M", "C"],
        ["M", "K"],
        ["B", "E"],
        ["C", "F"],
        ["C", "G"],
        ["C", "H"],
        ["K", "I"],
        ["K", "J"],
        ["E", "D"],
        ["F", "L"],
        ["F", "A"],
        ["H", "N"],
        ["H", "O"],
        ["J", "P"],
        ["J", "Q"]
    ]



    categories = [
        "F", "N"
    ]
    categoryStr = "J"



    ######################
    # 제공 데이터 세트 2
    ######################

    # inputData = [
    #     ["Z", "B"],
    #     ["Z", "W"],
    #     ["Z", "V"],
    #     ["B", "E"],
    #     ["W", "F"],
    #     ["W", "G"],
    #     ["V", "H"],
    #     ["V", "I"],
    #     ["V", "J"],
    #     ["E", "K"],
    #     ["F", "L"],
    #     ["G", "M"],
    #     ["G", "N"],
    #     ["H", "O"],
    #     ["I", "P"],
    #     ["J", "Q"]
    # ]
    #
    # categories = [
    #     "I", "O"
    # ]
    # categoryStr = "G"

    return inputData


def printInput(inputData):
    printLineInitial()
    print("상위 카테고리\t하위 카테고리")
    for strArr in inputData:
        for str in strArr:
            print("{}\t\t\t\t".format(str),end="")
        print()

    printLine()

def printTopCategory(topCategory) :

    print("[입력으로 제공되는 두 개의 카테고리]: ", end="")
    for category in categories:
        print(category, end=" ")
    print()

    print("[두 개의 카테고리를 포함하는 상위 카테고리 중 최하위 카테고리]: ", end="")
    if topCategory == "":
        print("결과값이 없습니다.")
    else:
        print(topCategory)
    printLine()

def printNumberOfSubcategories(numberOfSubcategories) :
    print("[입력으로 제공되는 카테고리]: {}".format(categoryStr))
    print("[하위 카테고리의 개수]: ", end="")
    if numberOfSubcategories == 0:
        print("결과값이 없습니다.")
    else:
        print(numberOfSubcategories)
    printLine()


def printLine():
    print("--------------------------------------------------------------------------")

def printLineInitial():
    print("[초기 입력 데이터]")

## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()
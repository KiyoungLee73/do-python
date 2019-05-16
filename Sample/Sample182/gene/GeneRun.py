#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Gene.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from Gene import *

def main():
    global similarityMatrix

    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()
    printInput(inputData)

    # 단순비교 방식의 유사도 측정 기능
    similarity = measureSimpleComparison(inputData)
    printSimpleComparison(similarity)

    # 행렬비교 방식의 유사도 측정 기능
    maxSimilarity = measureSortComparison(inputData, similarityMatrix)
    printSortComparison(maxSimilarity)

def loadData():
    global similarityMatrix

    similarityMatrix = [
        [5, -1, -2, -1, -3],
        [-1, 6, -3, -2, -4],
        [-2, -3, 7, -1, -2],
        [-1, -2, -1, 8, -1],
        [-3, -4, -2, -1, 0]
    ]
    ######################
    # 제공 데이터 세트 1
    ######################

    inputData = "AGTCATG,GTTAG"

    ######################
    # 제공 데이터 세트 2
    ######################

    # inputData = "ATTCGG,GTAT"

    return inputData


def printInput(inputData):
    printLineInitial()
    print("유전자 문자열: {}".format(inputData))
    printLine()

def printSimpleComparison(similarity) :
    print("[단순비교 방식의 유사도 측정]")
    print("유사도:", end=" ")
    if similarity == 0:
        print("결과값이 없습니다.")
    else:
        print(similarity)
    printLine()

def printSortComparison(maxSimilarity) :
    print("[행렬비교 방식의 유사도 측정]")
    print("유사도:", end=" ")
    if maxSimilarity == 0:
        print("결과값이 없습니다.")
    else:
        print(maxSimilarity)
    printLine()

def printLineInitial():
    print("[초기 입력 데이터]")

def printLine():
    print("--------------------------------------------------------------------------")

## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()
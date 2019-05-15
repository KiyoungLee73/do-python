# N개의 삼각형을 만들기 위한 막대 개수를 구하는 기능
#
# @param		inputData			입력데이터(삼각형 개수)
# @return							막대 개수

def getNumberOfStickForTriangle(inputData) :
    numberOfStickForTriangle = 0
    ########################여기부터 구현 (1) ---------------->
    numberOfStickForTriangle = 3 + (inputData -1) * 2
    ############################# <-------------- 여기까지 구현 (1)
    return numberOfStickForTriangle


# N층의 피라미드를 만들기 위한 막대 개수를 구하는 기능
#
# @param		numberOfLayers			입력데이터(피라미드 층수)
# @return								막대 개수
def getNumberOfStickForPyramid(numberOfLayers) :
    numberOfStickForPyramid = 0
    ########################여기부터 구현 (2) ---------------->
    total_1 = 0
    total_2 = 0
    total = 0
    for i in range(numberOfLayers, 0, -1):
        total_1 = total_1 + (3 + (2 * i - 2)*2)

    for j in range(numberOfLayers - 1):
        total_2 = total_2 + j + 1

    total = total_1 - total_2
    numberOfStickForPyramid = total
    ############################# <-------------- 여기까지 구현 (2)
    return numberOfStickForPyramid

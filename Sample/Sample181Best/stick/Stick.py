# N개의 삼각형을 만들기 위한 막대 개수를 구하는 기능
#
# @param		inputData			입력데이터(삼각형 개수)
# @return							막대 개수

def getNumberOfStickForTriangle(inputData) :
    numberOfStickForTriangle = 0
    ########################여기부터 구현 (1) ---------------->
    numberOfStickForTriangle = 3 + (inputData - 1) * 2
    ############################# <-------------- 여기까지 구현 (1)
    return numberOfStickForTriangle


# N층의 피라미드를 만들기 위한 막대 개수를 구하는 기능
#
# @param		numberOfLayers			입력데이터(피라미드 층수)
# @return								막대 개수
def getNumberOfStickForPyramid(numberOfLayers) :
    numberOfStickForPyramid = 0
    ########################여기부터 구현 (2) ---------------->
    totalSum = 0
    sum = 0
    for i in range(1,numberOfLayers+1):
        totalSum += 3 + (2 * i - 2) * 2
        if i <= numberOfLayers-1:
            sum += i
    numberOfStickForPyramid = totalSum - sum
    ############################# <-------------- 여기까지 구현 (2)
    return numberOfStickForPyramid
